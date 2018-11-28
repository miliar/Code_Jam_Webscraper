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

	freopen("/Users/bajaj/Downloads/A-large.in", "r", stdin);
	freopen("/Users/bajaj/Downloads/output_codejam.txt", "w", stdout);

	int t;
	cin>>t;

	for(int ti=1;ti<=t;ti++){

		LL n;
		cin>>n;
		LL sum = n;
		int arr[10] = {0};
		int count = 0;
		LL ans = n;
		FOR(i,1,300){
			sum = n*i;
			while(sum!=0){

				int rem = sum%10;
				sum = sum/10;
				if(arr[rem] == 0){
					arr[rem]=1;
					count++;
				}

			}
			if(count==10){
				ans = n * i;
				break;
			}

		}

		cout<<"Case #"<<ti<<": ";

		if(count!=10){
			cout<<"INSOMNIA";
		}
		else{
			cout<<ans;
		}

		cout<<"\n";


	}




	return 0;

}
