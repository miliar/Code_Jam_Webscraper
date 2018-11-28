#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <time.h>

typedef float flt;
typedef double dbl;
typedef long long Lint;
typedef std::pair <int,int> ii;
typedef std::pair <Lint,Lint> Lii;

#define mutlak(x) x<0 ? x=-x : x=x
#define eksi(x) x<0 ? -x : x
#define buyuk(x,y) x>y ? y=x : x=y
#define kucuk(x,y) x<y ? y=x : x=y

using namespace std;

/*ahmetarift*/

int main()
{
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int n,j,z,sum,i,shy,kisi;
    scanf("%d",&n);
    char s[7];
    for(i=0;i<n;i++){
    scanf("%d",&shy);
    cin>>s;
    kisi=0;
    sum=0;
    for(j=0;j<=shy;j++){
    if(kisi<j&&((s[j]-48)!=0)){
    sum+=j-kisi;
    kisi+=sum;
    }
    kisi+=s[j]-48;
    }
    printf("Case #%d: %d\n",i+1,sum);
    }
}
