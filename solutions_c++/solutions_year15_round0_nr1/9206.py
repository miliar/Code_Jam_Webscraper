// Author : Muhammad Rifayat Samee
// Problem :
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
char str[10005];
int n;
int main(){

	freopen("A_big.in","r",stdin);
	freopen("A_big.out","w",stdout);
    int cases,i,j,k,ct=1;
    scanf("%d",&cases);
    while(cases--){
        scanf("%d",&n);
        scanf("%s",str);
        int cur,res = 0;
        cur = 0;
        int len = strlen(str);
        for(i=0;i<len;i++){

            if(i==0){
               cur = cur + (str[i] - '0');
            }
            else{
                if(str[i] == '0')continue;
                if(cur<i){
                    res = res + i - cur;
                    cur = cur + (str[i] - '0') + i - cur;
                }
                else
                    cur = cur + (str[i] - '0');
            }
            //printf("%d\n",cur);
        }
        printf("Case #%d: %d\n",ct++,res);
    }

	return 0;
}
