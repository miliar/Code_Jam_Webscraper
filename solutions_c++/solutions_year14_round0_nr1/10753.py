#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>

using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> VVII;
typedef vector<VI> VVI;


#define INF 2000000000
#define INFLL (1LL<<62)
#define FI first
#define SE second
#define PB push_back
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({LL x;scanf("%lld", &x);x;})
#define rep(i,n) for(i=0;i<(n);i++)
#define _mp make_pair
int A[4][4];
int main(){
        int t=SS,p,i,j,ans,r;
        for (unsigned int k = 0; k < t; k += 1)
        {
                map<int,int> mp;
                map<int,int> :: iterator it;
                p=2;
                while(p--){
                r=SS;
                rep(i,4) rep(j,4) A[i][j]=SS;
                rep(j,4) mp[A[r-1][j]]++;
                }
               // printf("%d \n",mp.size());
                if(mp.size()==8){
                        printf("Case #%d: Volunteer cheated!\n",k+1);
                }
                else if(mp.size()==7){
                        for ( it = mp.begin(); it != mp.end(); it++)
                        {
                                if((*it).SE==2)
                                        ans=(*it).FI;
                        }
                        printf("Case #%d: %d\n",k+1,ans);
                }
                else
                        printf("Case #%d: Bad magician!\n",k+1);
          }
          return 0;
}          
