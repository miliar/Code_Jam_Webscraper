#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <stdlib.h>
#include <math.h>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
#define ll long long 
#define _ ios::sync_with_stdio(false);
#define mem(x,a) memset(x,(a),(int)(sizeof(x)))
#define pii pair<int,int>
#define fr(i,a,n) for(int i=(a);i<=(n);i++)
#define frd(i,a,n) for(int i=(a);i>=(n);i--)
#define nl printf("\n")
#define pb push_back
#define mp make_pair 
#define F first 
#define S second
#define V vector
ll mod=1e9+7;
int main() {_
		int t;cin>>t;
		for(int T=1;T<=t;T++)
		{
			unsigned ll k,c,s;
			cin>>k>>c>>s;
			unsigned ll add=1;
			fr(i,1,c-1)add=add*k;
			//cout<<add<<endl;
			cout<<"Case #"<<T<<": "<<"1 ";
			for(ll i=1;i<s;i++)
			{
				cout<< (1LL +i*add)<<" ";
				//add+=add; 
			}
			nl;
		}
	return 0;
}
