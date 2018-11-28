#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

typedef long long ll;
typedef unsigned int ui;
typedef pair<int,int> pii;


#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(int i = (a) - 1; i >= (b); --i)
#define clear(a, b) memset(a, b, sizeof(a))
#define size(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define pb push_back
#define mp make_pair

int mat[4];
int fin[4];

void solve(){
	int a1 ;
	cin>>a1;
	a1--;
	int temp;
	FOR(i,0,4)
		FOR(j,0,4)	
			if(i==a1) cin >> mat[j];
			else cin >> temp;
	
	int a2;
	cin>>a2;
	a2--;
	FOR(i,0,4)
		FOR(j,0,4)	
			if(i==a2) cin >> fin[j];
			else cin >> temp;

	int matches = 0;
	int k = 0;
	FOR(i,0,4)
		FOR(j,0,4)
			if(mat[i] == fin[j]){
			 matches++;
			 k = mat[i];
			}
		
	switch(matches){
		case 0:		cout<<"Volunteer cheated!"<<endl;
					break;
		case 1:		cout<<k<<endl;
					break;
		default:	cout<<"Bad magician!"<<endl;
	}
}

int main()
{
	int t = 0;
	cin >> t;
	FOR(i,0,t)	{
		cout<<"Case #"<<(i+1)<<": ";
		solve();
	}

	return 0;
};
