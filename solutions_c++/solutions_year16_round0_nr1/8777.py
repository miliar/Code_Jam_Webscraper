#include <iostream>
#include <vector>
#include <unordered_set>
#include <cmath>

using namespace std;

void intToStr(int a,std::vector<char> &v){
	int sz = log10(a)+1;
	v.resize(sz);
	// ptr = (char *)malloc(sz);
	for(int i=0;i<sz;++i){
	// while(a){
		v[sz-i-1] = '0' + a % 10;
		a = a / 10;
	}
}

// void printVector(std::vector<char> &v){
// 	for(auto ch:v)
// 		cout<<ch;
// 	cout<<"\n";
// }

int main(){
	int T;
	cin >> T;
	for(int i=0;i<T;++i){
		int s1[] = {'0','1','2','3','4','5','6','7','8','9'};
		int total = 10;
		int input,k=2,input2;
		cin >> input;
		input2 = input;
		
		if(input == 0){
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA\n";
			continue;
		}

		while(total){
			std::vector<char> v;
			intToStr(input,v);
			// printVector(v);
			for(int j=0;j<v.size() && total ;++j){
				if(s1[v[j]-'0'] != -1){
					--total;
					s1[v[j]-'0'] = -1;
				}
			}
			if(total)
			input = input2*(k++);
		}
		cout<<"Case #"<<i+1<<": "<<input<<"\n";	
	}
}