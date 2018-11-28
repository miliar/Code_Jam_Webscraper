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
    freopen("input.in", "r", stdin);
    freopen("output.txt","w",stdout);
#endif
 ios_base::sync_with_stdio(false);
cin.tie(NULL);
 int t,tc;
 cin>>tc;
 for(t=1;t<=tc;t++)
 {
 	int k,c,s,i;
   cin>>k>>c>>s;
   cout<<"Case #"<<t<<": ";
   for(i=1;i<=k;i++)
   {
    cout<<i<<" ";
   }
   cout<<"\n";
 }
 
	return 0;
}