#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
#define tr(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define all(c) c.begin(),c.end()
#define mod 1000000007
#define itor(c) typeof(c.begin())
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define si set<int>
#define msi multiset<int>
#define sp set<pair<int,int> >
#define vp vector<pair<int,int> >
#define pb push_back
#define mp make_pair

using namespace std;

int main()
{
ios::sync_with_stdio(false);
int i,j,k,l,a,b,c,d,t,flag=0,n,test,k;
cin>>test;
for(t=1;t<=test;t++){
	int ans=0;
	cin>>a>>b>>k;
	for(i=0;i<a;i++){
		for(j=0;j<b;j++){
			if(i&j<k){
			ans++;	
				
			}
			
			
		}
		
	}
	cout<<"Case #"<<t<<": "<<ans;

}
    return 0;
}