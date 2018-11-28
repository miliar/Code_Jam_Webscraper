#include <iostream>
#include <cassert>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef string str;

template <typename T>
ostream& operator<<(ostream& os, deque<T> vector){
	if(vector.size()==0)
		return os;
	os << vector[0];
	for(ll i=1;i<vector.size();++i)
		os << " " << vector[i];
	return os;
}

//goes through the selection possibilites of k elements of the array between begin and end,
//where between selectBegin aand selectEnd pointers to the currently selected elements are
template <typename T>
bool next_selection(T* begin, T* end, T** selectBegin, T** selectEnd){
	if(*(selectEnd-1)<end-1){
		(*(selectEnd-1))++;
		return true;
	}
	else if(selectBegin+1==selectEnd){
		*selectBegin=begin;
		return false;
	}
	else{
		bool result=next_selection(begin,end-1,selectBegin,selectEnd-1);
		*(selectEnd-1)=1+*(selectEnd-2);
		return result;
	}
}

//select from elements, indicatet by the ones "1" in the binary representation
template <typename T>
deque<T> getSelection(deque<T> elements, ll binaryRepresentationOfSelection){
	deque<T> result;
	for(ll i=0;i<elements.size();++i)
		if( (binaryRepresentationOfSelection>>i)%2 )
			result.push_back(elements[i]);
	return result;
}

//calculating faculty of n
ll facll(ll n){
	if(n)
		return n*facll(n-1);
	return 1;
}

//calculating faculty of n, floating point calulations
ld facld(ll n){
	if(n)
		return (ld)n * facld(n-1);
	return 1.;
}

//calculating the power of base to the exp
ll powll(ll base, ll exp){
	ll result=1;
	for(ll i=0;i<exp;++i)
		result*=base;
	return result;
}

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
#define pi 3.14159265358979323846264338328L

void init(){
}

typedef v(ll) otype;
otype calcFunction(string input) {
	otype result;
	v(int) S;
	cout << "hey" << endl;
	forn(i, 26) {
		S.pb(0);
	}
	forn(i, input.length()) {
		S[int(input[i])-'A']++;
		cout << input[i] << endl;
	}
	v(ll) digitsCount;
	forn(i, 10) {
		digitsCount.pb(0);
	}
	// 0
	digitsCount[0]=S['Z'-'A'];
	S['E'-'A']-=digitsCount[0];
	S['R'-'A']-=digitsCount[0];
	S['O'-'A']-=digitsCount[0];

	// 2
	digitsCount[2]=S['W'-'A'];
	S['T'-'A']-=digitsCount[2];
	S['O'-'A']-=digitsCount[2];

	// 8
	digitsCount[8]=S['G'-'A'];
	S['E'-'A']-=digitsCount[8];
	S['I'-'A']-=digitsCount[8];
	S['H'-'A']-=digitsCount[8];
	S['T'-'A']-=digitsCount[8];

	// 6
	digitsCount[6]=S['X'-'A'];
	S['S'-'A']-=digitsCount[6];
	S['I'-'A']-=digitsCount[6];

	// 7
	digitsCount[7]=S['S'-'A'];
	S['E'-'A']-=digitsCount[7];
	S['V'-'A']-=digitsCount[7];
	S['E'-'A']-=digitsCount[7];
	S['N'-'A']-=digitsCount[7];

	// 5
	digitsCount[5]=S['V'-'A'];
	S['F'-'A']-=digitsCount[5];
	S['I'-'A']-=digitsCount[5];
	S['E'-'A']-=digitsCount[5];

	// 4
	digitsCount[4]=S['U'-'A'];
	S['F'-'A']-=digitsCount[4];
	S['O'-'A']-=digitsCount[4];
	S['R'-'A']-=digitsCount[4];

	// 9
	digitsCount[9]=S['I'-'A'];
	S['N'-'A']-=digitsCount[9];
	S['N'-'A']-=digitsCount[9];
	S['E'-'A']-=digitsCount[9];

	// 1
	digitsCount[1]=S['O'-'A'];
	S['N'-'A']-=digitsCount[1];
	S['E'-'A']-=digitsCount[1];

	// 3
	digitsCount[3]=S['T'-'A'];

	forn(i, 10) {
		forn(j, digitsCount[i]) {
			result.pb(i);
		}
	}
	return result;
}

//#define IFSTRUCT	//remove comment on this line, to activate if-structure
int main() {
	init();
	ofstream outfile("output.txt");
	ll tests = 0;
	cin >> tests;
	fore(test, 1, tests){
		//read input
		string input;
		cin >> input;
		//write output

		otype result=calcFunction(input);
		outfile << "Case #" << test << ": ";
		cout << "Case #" << test << ": ";
#ifndef IFSTRUCT
		forn(i, result.size()) {
			outfile << result[i];
			cout << result[i];
		}
		outfile << endl;
		cout << endl;
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
