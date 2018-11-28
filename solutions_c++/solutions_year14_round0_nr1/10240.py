#include<cstdio>
#include<string>
#include<cstring>
#include<algorithm>
#include<queue>
#include<cmath>
#include<iostream>
#include<cstdlib>
#include<map>
#include<fstream>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define MS0(x) memset(x,0,sizeof(x))

using namespace std;
typedef long long LL;

int a[5][5];
int k1[20],k2[20];

void work(){
    int r1,r2;
    scanf("%d",&r1);
    FOR(i,1,4)FOR(j,1,4)scanf("%d",&a[i][j]);
    
    FOR(i,1,16)k1[i]=k2[i]=0;
    
    FOR(j,1,4)k1[a[r1][j]]=1;
    scanf("%d",&r2);
    FOR(i,1,4)FOR(j,1,4)scanf("%d",&a[i][j]);
    FOR(j,1,4)k2[a[r2][j]]=1;
    
    int tot=0;
    FOR(i,1,16)if(k1[i]&&k2[i])tot++;
    if(tot>1)printf("Bad magician!\n");
    else if(tot==0)printf("Volunteer cheated!\n");
    else{
        FOR(i,1,16)if(k1[i]&&k2[i]){
            printf("%d\n",i);
        }
    }
}
    
    

int main(){
    //freopen("A-small-attempt6.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int ttt;
    scanf("%d",&ttt);
    FOR(hhh,1,ttt){
        printf("Case #%d: ",hhh);
        work();
    }
    return 0;
}
    
