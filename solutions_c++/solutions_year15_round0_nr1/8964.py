#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cfloat>
#include <cstdlib>
#include <cassert>
#include <iterator>
#include <deque>
#include <stack>
#include <bitset>
#include <numeric>
#include <utility>
#include <sstream>
#include <ctime>
#include <memory>
#include <climits>

using namespace std;

#define sf(n) scanf("%d",&n)
#define pf(n) printf("%d",n)
#define psp() printf(" ")
#define pt() printf("\t")
#define pln() printf("\n")
#define f(i,a,b) for(i=a; i<=b; ++i)

int i,j;

int main() {
	int t;sf(t);
	f(j,1,t){
		int s;sf(s);
		string x;cin>>x;int x1[s+1];
		int sum[s+1];
		f(i,0,s){ x1[i]=(int)(x[i])-48; /*cout<<x1[i]<<endl;*/}
		sum[0]=x1[0];int n=0;
		f(i,1,s){ 
			if(sum[i-1]<i){ n+=(i-sum[i-1]);sum[i]=i+x1[i]; }
			else { sum[i]=sum[i-1]+x1[i]; }
		}	
		printf("Case #%d: %d\n",j,n);
		
	}
	return 0;
}