//input and output
#include <iostream>
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
//for sorting and other stuff
#include <algorithm>

template <typename T>
std::ostream& operator<<(std::ostream& os, std::deque<T> vtor){
	if(vtor.size()==0)
		return os;
	os << vtor[0];
	for(unsigned long long i=1;i<vtor.size();++i)
		os << " " << vtor[i];
	return os;
}

//goes through the selection possibilites of k elements of the vtor
//use: ++si for next selection and *si for a vtor of the currently selected elements
//use: for(SelectionIterator<T> si(vtor,k);!si.final();++si){something with *si}
template <typename T>
class SelectionIterator{
private:
	unsigned long long k;
	unsigned long long n;
	std::deque<T> vtor;
	std::deque<T> selection;
	std::deque<unsigned long long> selectionNumbers;
	bool finalState;
public:
	SelectionIterator<T>(std::deque<T> vtor, unsigned long long k):k(k), n(vtor.size()), vtor(vtor), finalState(false){
		for(unsigned long long i=0;i<k;++i){
			selection.push_back(vtor[i]);
			selectionNumbers.push_back(i);
		}
	}

	void operator++(){
		for(unsigned long long i=k-1;i<k;--i){
			if(selectionNumbers[i]==n+i-k)
				continue;
			else{
				++selectionNumbers[i];
				selection[i]=vtor[selectionNumbers[i]];
				for(unsigned long long j=i+1;j<k;++j){
					selectionNumbers[j]=selectionNumbers[i]+j-i;
					selection[j]=vtor[selectionNumbers[j]];
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

#define v(type) deque<type >
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

void init(){
}

ll sum(v(ll) Pi){
	ll res=0;
	forn(i, Pi.sz)
		res+=Pi[i];
	return res;
}

ll maxIdx(v(ll) Pi){
	ll res=0;
	ll max=Pi[0];
	fornn(i,1,Pi.sz){
		if(max<Pi[i]){
			max=Pi[i];
			res=i;
		}
	}
	return res;
}

typedef v(str) otype;
otype calcFunction(ll N, v(ll) Pi) {
	otype result;
	if(N==2){
		forn(i,sum(Pi)/2){
			result.pb("AB");
		}
	return result;
	}
	while(sum(Pi)>2){
		ll maxId=maxIdx(Pi);
		str cur;
		result.pb(cur+(char)('A'+maxId));
		Pi[maxId]-=1;
	}
	str last;
	ll maxId=maxIdx(Pi);
	last+=('A'+maxId);
	Pi[maxId]-=1;
	maxId=maxIdx(Pi);
	last+=('A'+maxId);
	result.pb(last);
	return result;
}

//#define IFSTRUCT	//remove comment on this line, to activate if-structure for default value trigger
int main() {
	init();
	ofstream outfile("output.txt");
	ll tests = 0;
	cin >> tests;
	fore(test, 1, tests){
		//read input
		ll N;
		v(ll) Pi;
		cin >> N;
		forn(i,N){
			ll pi;
			cin >> pi;
			Pi.pb(pi);
		}
		//write output

		otype result=calcFunction(N,Pi);
		outfile << "Case #" << test << ": ";
		cout << "Case #" << test << ": ";
#ifndef IFSTRUCT
		outfile << result << endl;
		cout << result << endl;
#endif /*IFSTRUCT*/
#ifdef IFSTRUCT
		if(result>=0){
			outfile << result << endl;
			cout << result << endl;
		}
		else{
			str errorWord = "FALSE";
			outfile << errorWord << endl;
			cout << errorWord << endl;
		}
#endif /*IFSTRUCT*/
	}
	outfile.close();
	return 0;
}