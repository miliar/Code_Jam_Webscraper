
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define MAX 100100
#define mod 1000000007
#define MS0(x) memset(x, 0, sizeof(x))
#define ll long long int
#define in(x) scanf("%I64d", &x)
#define ind(x) scanf("%d", &x)
 
using namespace std;

int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input1.in", "r", stdin);
    freopen("output.txt","w",stdout);
#endif
 ios_base::sync_with_stdio(false);
cin.tie(NULL);
 int t,tc;
 cin>>tc;
 for(t=0;t<tc;t++)
 {
   int n,temp,temp1=0,k=n;
 cin>>n;
 int a[12]={0};
 set<int> s;
 if(n!=0)
 {
   k=n;
 while(s.size()<10)
 {
     temp1=k;


     while(k>0)
     {
         //cout<<"kl"<<" ";
         temp=k%10;
         s.insert(temp);
         k=k/10;
     }
   k=temp1+n;
 }
 cout<<"Case #"<<(t+1)<<":"<<" "<<temp1<<"\n";
 }
 else
    {
     cout<<"Case #"<<(t+1)<<":"<<" "<<"INSOMNIA"<<"\n";
    }
  }
	return 0;
}