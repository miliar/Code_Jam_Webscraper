//input and output
#include <iostream>
#include <iomanip>
#include <fstream>
//working with strings
#include <cstring>
#include <sstream>
//debugging with assert
#include <cassert>
//datastructures
#include <deque>
#include <list>
#include <set>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
//math operations and pairs, rand, atoi, atof and standard stuff
#include <cstdlib>
#include <cmath>
#include <numeric>
//for sorting and other stuff
#include <algorithm>

template <typename T>
std::ostream& operator<<(std::ostream& os, std::deque<T> vector){
	if(vector.size()==0)
		return os;
	os << vector[0];
	for(unsigned long long i=1;i<vector.size();++i)
		os << " " << vector[i];
	return os;
}

//goes through the selection possibilites of k elements of the vector
//use: ++si for next selection and *si for a vector of the currently selected elements
//use: for(SelectionIterator<T> si(vector,k);!si.final();++si){something with *si}
template <typename T>
class SelectionIterator{
private:
	unsigned long long k;
	unsigned long long n;
	std::deque<T> vector;
	std::deque<T> selection;
	std::deque<unsigned long long> selectionNumbers;
	bool finalState;
public:
	SelectionIterator<T>(std::deque<T> vector, unsigned long long k):k(k), n(vector.size()), vector(vector), finalState(false){
		for(unsigned long long i=0;i<k;++i){
			selection.push_back(vector[i]);
			selectionNumbers.push_back(i);
		}
	}

	void operator++(){
		for(unsigned long long i=k-1;i<k;--i){
			if(selectionNumbers[i]==n+i-k)
				continue;
			else{
				++selectionNumbers[i];
				selection[i]=vector[selectionNumbers[i]];
				for(unsigned long long j=i+1;j<k;++j){
					selectionNumbers[j]=selectionNumbers[i]+j-i;
					selection[j]=vector[selectionNumbers[j]];
				}
				return;
			}
		}
		finalState=true;
	}

	std::deque<T> operator*(){
		return selection;
	}

	bool final(){
		return finalState;
	}
};

//select from elements, indicated by the ones "1" in the binary representation
template <typename T>
std::deque<T> getSelection(std::deque<T> elements, unsigned long long binaryRepresentationOfSelection){
	std::deque<T> result;
	for(unsigned long long i=0;i<elements.size();++i)
		if( (binaryRepresentationOfSelection>>i)%2 )
			result.push_back(elements[i]);
	return result;
}

//calculating faculty of n, only valid for n<=20
unsigned long long facll(unsigned long long n){
	if(n)
		return n*facll(n-1);
	return 1;
}

//calculating faculty of n, floating point calulations
long double facld(unsigned long long n){
	if(n)
		return (long double)n * facld(n-1);
	return 1.;
}

//calculating the power of base to the exp
long long powll(long long base, unsigned long long exp){
	long long result=1;
	for(unsigned long long i=0;i<exp;++i)
		result*=base;
	return result;
}

using namespace std;

typedef long long ll;
typedef long double ld;
typedef string str;

#define mp make_pair
#define x first
#define y second
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define hash unordered_map
#define sz size()
#define bn begin()
#define ed end()

#define v(type) deque<type >
#define p(type1,type2) pair<type1, type2 >
#define it(container) typeof((container).begin())
#define all(x) (x).begin(), (x).end()
#define select(x,i) (x).begin()+(i), (x).begin()+(i)+1
#define foreach(cit,container) for(typeof((container).begin()) cit = (container).begin(); cit != (container).end(); cit++)
#define foreachc(c,cit,container) ll c=0;for(typeof((container).begin()) cit = (container).begin(); cit != (container).end(); c++, cit++)
#define forn(i, n) for (ll i = 0; i < (ll)(n); ++i)
#define fornn(i, a, b) for (ll i = (ll)(a); i < (ll)(b); ++i)
#define fore(i, a, b) for (ll i = (ll)(a); i <= (ll)(b); ++i)

#define inf 9000000000000000000L
#define eps 1e-15
#define pi 3.14159265358979323846264338328L

ll N;
ll R;
ll P;
ll S;

void init(){
}

typedef str otype;
otype calcFunction() {
	otype result="";
	ll curP=1;
	ll curR=1;
	ll curS=0;
	fornn(n,1,N){
		ll newP=curP+curS;
		ll newR=curR+curP;
		ll newS=curS+curR;
		curP=newP;
		curR=newR;
		curS=newS;
	}
	ll counter=0;
	forn(i,3){
		if(P==curP && R==curR && S==curS)
			break;
		ll temp=curP;
		curP=curR;
		curR=curS;
		curS=temp;
		++counter;
	}
	if(counter==3)
		return "";
	switch(counter){
		case 0:
		result="PR";
		break;
		case 1:
		result="PS";
		break;
		case 2:
		if(N==1)
			result="RS";
		else
			result="SR";
	}
	fornn(n,1,N){
		str newResult="";
		forn(i,result.sz){
			switch(result[i]){
				case 'P':
				newResult+="PR";
				break;
				case 'S':
				newResult+="PS";
				break;
				case 'R':
				if(n==N-1)
					newResult+="RS";
				else
					newResult+="SR";
			}
		}
		result=newResult;
	}
	fore(i,1,N){
		v(str) subs;
		ll len=powll(2,i);
		ll sublen=powll(2,i-1);
		forn(k,powll(2,N-i)){
			str s1=result.substr(k*len,sublen);
			str s2=result.substr(k*len+sublen,sublen);
			if(s2<s1){
				result.replace(k*len,sublen,s2);
				result.replace(k*len+sublen,sublen,s1);
			}
		}
	}
	return result;
}

#define IFSTRUCT	//remove comment on this line, to activate if-structure for default value trigger
int main() {
	init();
	ofstream outfile("output.txt");
	cout << setprecision(10);
	outfile << setprecision(10);
	ll tests = 0;
	cin >> tests;
	fore(test, 1, tests){
		//read input
		cin >> N >> R >> P >> S;
		//calc result
		otype result=calcFunction();
		//write output
		outfile << "Case #" << test << ": ";
		cout << "Case #" << test << ": ";
#ifndef IFSTRUCT
		outfile << result << endl;
		cout << result << endl;
#endif /*IFSTRUCT*/
#ifdef IFSTRUCT
		if(result.sz>0){
			outfile << result << endl;
			cout << result << endl;
		}
		else{
			str errorWord = "IMPOSSIBLE";
			outfile << errorWord << endl;
			cout << errorWord << endl;
		}
#endif /*IFSTRUCT*/
	}
	outfile.close();
	return 0;
}