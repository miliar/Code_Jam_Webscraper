#include <iostream>
#include <cmath>
#include <string>

std::string expand(const std::string &s, int n){
	std::string result; 
	result.reserve(s.size()*n+1);
	for(int K=0; K<n; ++K)
		result += s;
	return result;
}

int sign(int n){
	if(n>0) return 1;
	if(n<0) return -1;
	return 0;
}

int multiply(int a, int b){
	if(a==0) return b;
	if(a==42) return -b;

	int result[3][3] = {
		{42,3,-2},
		{-3,42,1},
		{2,-1,42}
	};
	int m = result[abs(a)-1][b-1];
	int r = m*sign(a);
	if(r==-42) return 0;
	return r;
}
int multiply_back(int a, int b){
	if(a==0) return b;
	if(a==42) return -b;

	int result[3][3] = {
		{42,3,-2},
		{-3,42,1},
		{2,-1,42}
	};
	int m = result[b-1][abs(a)-1];
	int r = m*sign(a);
	if(r==-42) return 0;
	return r;
}

/*
- 1  i  j  k
1 1  i  j  k
i i -1  k  -j
j j -k -1  i
k k  j -i  -1
 */

//-1 -> 42
//1 -> 0
//i -> 1
//j -> 2
//k -> 3
template<class Iter>
int form(Iter begin, Iter end, char c){
	int now = 0;
	int index = 0;
	for(; begin not_eq end; ++begin, ++index){
		now = multiply(now, *begin);
		if(now==c) break;
	}
	return index;
}

template<class Iter>
int form_back(Iter begin, Iter end, char c){
	int now = 0;
	int index = 0;
	for(; begin not_eq end; ++begin, ++index){
		now = multiply_back(now, *begin);
		if(now==c) break;
	}
	return index;
}

void transform(std::string &s){
	for(int K=0; K<s.size(); ++K){
		switch(s[K]){
			case 'i': s[K] = 1; break;
			case 'j': s[K] = 2; break;
			case 'k': s[K] = 3; break;
		}
	}
}

template<class Iter>
int reducir(Iter begin, Iter end){
	int now = 0;
	for(; begin not_eq end; ++begin)
		now = multiply(now, *begin);
	return now;
}

int main(int argc, char **argv){
	int casos;
	std::cin>>casos;
	for(int K=1; K<=casos; ++K){
		int characters, repetition;
		std::cin>>characters>>repetition;
		std::string input; std::cin>>input;
		std::string s = expand(input, repetition);
		transform(s);

		int redux = reducir(s.begin(), s.end());
		bool can;
		if(redux==42){
			int indexi = form(s.begin(), s.end(), 1)+1;
			int indexk = s.size()-form_back(s.rbegin(), s.rend(), 3)-1;
			can = indexi<indexk;
			//if(can)
				//std::cerr << "@@" << reducir(s.begin()+indexi, s.begin()+indexk) << '\n';
		}
		else can=false;
		std::cout << "Case #" << K << ": " << (can?"YES":"NO") << '\n';
	}
	return 0;
}


