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
	fr(k,1,t)
	{
		string s;
		cin>>s;
		int flip=0;
		int n=s.size(),ans=0;
		frd(i,n-1,0)
		{
			if(s[i]=='-' && flip==0)ans++,flip++;
			else if(s[i]=='+' && flip)ans++,flip=0;
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
