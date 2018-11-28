// A_SenateEvacuation.cpp

#include <iostream>
#include <vector>
#include <iomanip>
#include <queue>
#include <string>
#include <math.h>
#include <functional>
#include <sstream>
#include <cstring>
#include <set>
#include <map>
#include <cstdio>
#include <bitset>
#include <algorithm>  
//#include <bits/stdc++.h>

using namespace std;

//Shortcuts for "common" data types in contests
typedef long long int ll;
typedef pair<int, int > pii;
typedef vector<int > vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;

//  ans = a ? b : c;          //To simplify: if(a) ans = b; else ans = c
//  ans += val;             //To simplify: ans = ans + val;
//  index = (index + 1)%n;      
//  index = (index + n - 1)%n;
//  int ans = (int)((double)d + 0.5); //For rounding to the nearest integer
//  ans = min(ans, new_computation);  //min/max shortcut

#define INF 1000000000
#define rep(i, a, b) for(int i = a; i < b; i++)
#define S(x) scanf("%d", &x)
#define S2(x, y) scanf("%d%d", &x, &y)
#define S3(x, y, z) scanf("%d%d%d", &x, &y, &z)
#define P(x) printf("%d\n", x)
#define all(v) v.begin(), v.end()
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

typedef struct party{

	char let;
	int people;

}party;

bool operator<(const party& a, const party& b) {
  
  return a.people < b.people;
}

int main(){

	int cases, size, totPeople;
	S(cases);

	for1(i, cases){

		totPeople = 0;

		S(size);

		party tot[size];

		forn(j, size){

			S(tot[j].people);
			totPeople += tot[j].people;
			tot[j].let = j + 65;
		}

		priority_queue<party> myQ (tot, tot + size);

		string ans = "";

		while(!myQ.empty()){

			ans += myQ.top().let;

			int temp = myQ.top().people;
			char myLet = myQ.top().let;

			//cout<<"myLet = "<<myLet<<endl;
			temp--;
			totPeople--;

			party newP;
			newP.people = temp;
			newP.let = myLet;

			myQ.pop();

			if(newP.people > 0)
				myQ.push(newP);

			if(myQ.top().people > (double) (0.5)*totPeople){

				ans += myQ.top().let;

				int temp2 = myQ.top().people;
				char myLet2 = myQ.top().let;

				//cout<<"myLet2 = "<<myLet2<<endl;
				temp2--;
				totPeople--;

				party newP2;
				newP2.people = temp2;
				newP2.let = myLet2;

				myQ.pop();

				if(newP2.people > 0)
					myQ.push(newP2);
			}

			ans += " ";
		}

		cout<<"Case #"<<i<<": "<<ans;
		printf("\n");
	}

	return 0;
}