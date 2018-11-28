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

#define put insert

unordered_set<ll> curSelection;
ld curProbs[200];
ld newProbs[200];
v(ld) P;
ll K;
ll N;
bool doPrint=false;

void clearProbs(){
	forn(i,200){
		curProbs[i]=0.;
		newProbs[i]=0.;
	}
	curProbs[0]=1.;
}

void transferProbs(){
	forn(i,200){
		curProbs[i]=newProbs[i];
		newProbs[i]=0.;
	}
}

void init(){
}

void calcProbs(){
	clearProbs();
	foreach(elem,curSelection){
		ll idx=*elem;
		ld p=P[idx];
		newProbs[0]=(1-p)*curProbs[0];
		fornn(i,1,200){
			newProbs[i]=p*curProbs[i-1]+(1-p)*curProbs[i];
		}
		transferProbs();
	}
}

p(ll,ll) dotest(){
	forn(i,N){
		if(curSelection.count(i)==0)
			continue;
		curSelection.erase(i);
		calcProbs();
		curSelection.put(i);
		if (abs(curProbs[K/2-1]-curProbs[K/2])<eps){
			continue;
		}
		else if(curProbs[K/2-1]<curProbs[K/2]){
			forn(j,i){
				if(curSelection.count(j)==0){
					return mp(i,j);
				}
			}
		}
		else if(curProbs[K/2-1]>curProbs[K/2]){
			fornn(j,i+1,N){
				if(curSelection.count(j)==0){
					return mp(i,j);
				}
			}
		}
	}
	return mp(0,0);
}

typedef ld otype;
otype calcFunction() {
	curSelection.clear();
	clearProbs();
	otype result=0;
	forn(i,K/2){
		curSelection.put(i);
		curSelection.put(N-i-1);
	}
	bool testgood=false;
	while(!testgood){
		p(ll,ll) swapids=dotest();
		if(swapids.x==swapids.y)
			testgood=true;
		else{
			curSelection.erase(swapids.x);
			curSelection.put(swapids.y);
		}
	}
	/*
	foreach(elem,curSelection)
		cout << *elem << endl;
	*/
	calcProbs();
	return curProbs[K/2];
}

//#define IFSTRUCT	//remove comment on this line, to activate if-structure for default value trigger
int main() {
	init();
	ofstream outfile("output.txt");
	cout << setprecision(10);
	outfile << setprecision(10);
	ll tests = 0;
	cin >> tests;
	fore(test, 1, tests){
		//read input
		cin >> N >> K;
		P.clear();
		clearProbs();
		forn(i,N){
			ld p;
			cin >> p;
			P.pb(p);
		}
		sort(all(P));
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
		if(result>=0){
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