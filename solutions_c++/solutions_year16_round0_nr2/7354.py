/*
 * codeforces2.cpp
 *
 *  Created on: 19-Mar-2016
 *      Author: bajaj
 */




#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <deque>


using namespace std;

typedef long long int LL;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

vector<vii> AdjList;    // graph representation
vector< pair<int, ii> > EdgeList; // edgelist for kruskal algorithm


#define inp_s ios_base::sync_with_stdio(false)
#define cinnull cin.tie(NULL)

#define DRT() int test_case; cin>>test_case;while(test_case--)
#define FOR(i,a,b) for(LL i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) for(int i=0;i<n;i++)
#define rdarr(a,n) REP(i,n) cin >> a[i];


LL min(LL a, LL b){
	return a < b ? a : b;
}

LL max(LL a, LL b){
	return a > b ? a : b;
}

int max(int a, int b){
	return a > b ? a : b;
}


int main(){

	freopen("/Users/bajaj/Downloads/B-large.in", "r", stdin);
	freopen("/Users/bajaj/Downloads/output_codejam.txt", "w", stdout);

	int t;
	cin>>t;

	for(int ti=1;ti<=t;ti++){

		int count = 0 ;
		string s;

		cin>>s;

		for(int i=0;i<s.length();i++){

			if(i==s.length()-1){
				if(s[i]=='-'){
					count++;
				}
				break;
			}

			if(s[i]!=s[i+1])count++;

		}

		cout<<"Case #"<<ti<<": ";


		cout<<count;


		cout<<"\n";


	}




	return 0;

}
