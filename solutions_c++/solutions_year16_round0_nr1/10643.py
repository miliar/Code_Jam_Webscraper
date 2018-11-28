//#include<bits/stdc++.h>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define fr(i,m,n) for(i=m;i<n;i++)
#define ifr(i,m,n) for(i=m;i>n;i--)
#define ll long long
#define ull unsigned ll
#define sci(X) scanf("%d",&X)
#define pf printf
#define var(x) x i=0,j=0,k=0,tmp=0,tmp1=0,tmp2=0,tmp3=0,tmp4=0,tmp5=0,flag=0,T=0,N,Q
#define pb push_back
#define vi vector<int>
#define vii vector<pair<int,int> >
#define vvii vector<vector<pair<int,int> > >
#define vl vector<ll>
#define vll vector<pair<ll,ll> >
#define all(c) c.begin(), c.end() 
#define sz(a) int((a).size()) 
#define present(container, element) (container.find(element) != container.end()) 
#define vpresent(container, element) (find(all(container),element) != container.end()) 
#define br cout<<"\n"
using namespace std;

bool arr[10];

bool check()
{
  return arr[0] && arr[1] && arr[2] && arr[3] && arr[4] && arr[5] && arr[6] &&  arr[7] && arr[8] && arr[9];
}

int main()
{
var(int);
 cin>>T;
 j = 1;
 fr(j,1,T+1)
   {
     memset(arr,false,10);
     cout<<"Case #"<<j<<": ";
     cin>>N;
     if(N==0)
       cout<<"INSOMNIA\n";
     else
       { k = 0;
	 while(!check())
	   {
	     k++;
	   int x = N*k;
	   while(x)
	   {
	     arr[x%10]=true;
	     x/=10;
	   }
	   }
	 cout<<k*N<<"\n";
       }
   }
}
