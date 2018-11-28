// Author : Muhammad Rifayat Samee
// Problem : A
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<complex>
#include<valarray>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;
set<int>S;
void makeit(int n){
    int i;
    while(n!=0){
        int r = n%10;
        S.insert(r);
        n = n/10;
    }
}

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);
    int cases,n,i,j,k,ct=1;
    scanf("%d",&cases);
    while(cases--){
        scanf("%d",&n);
        S.clear();
        printf("Case #%d: ",ct++);
        if(n == 0){
            printf("INSOMNIA\n");
        }
        else{
            i = 1;
            while(1){
                makeit(i*n);
                //printf("?? %d %d\n",n,S.size());
                if(S.size() == 10){
                    printf("%d\n",i*n);
                    break;
                }
                i++;
            }

        }
    }

	return 0;
}
