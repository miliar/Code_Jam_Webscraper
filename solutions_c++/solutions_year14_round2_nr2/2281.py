#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <vector>
#define ll long long
#define s second
#define f first
#define PB push_back
using namespace std;
map<ll,ll>mp;
typedef pair<int,int>pib;

#define SWAP(a, b) (((a) ^= (b)), ((b) ^= (a)), ((a) ^= (b)))

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int main(){
int cases;
cin>>cases;
for(int t=1;t<=cases;t++){
	ll a,b,k,count=0;
	cin>>a>>b>>k;
	for(int i=0;i<a;i++){
		for(int j=0;j<b;j++){
			if((i&j)<k)
          count++;
          
      }}
      	printf("Case #%d: %d\n",t,count);
      }

cin.get();
return 0;
}

