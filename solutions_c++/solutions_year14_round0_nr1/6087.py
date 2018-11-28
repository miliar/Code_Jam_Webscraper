#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <map>
#include <vector>
#include <cmath>
#include <string.h>
#include <time.h>
#include <fstream>
#include <set>
#include <stack>
#include <list>

using namespace std;

#define READ freopen("acm.in","r",stdin)
#define WRITE freopen("acm.out","w",stdout)
#define ll long long
#define ull unsigned long long 
#define uint unsigned int
#define PII pair<int,int>
#define PDD pair<double,double>
#define fst first
#define sec second
#define MS(x,d) memset(x,d,sizeof(x))
#define INF 0x3f3f3f3f
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MOD 1000000007
#define MAX 1111

int b[12][12];
int ans[20];
int main()
{
    READ;
    int cas;
    freopen("acm.out","w",stdout);
    scanf("%d",&cas);
    for(int T=1;T<=cas;T++)
    {
        MS(ans,0);
        int row;
        scanf("%d",&row);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        for(int i=1;i<=4;i++)
            ans[b[row][i]]=1;
        scanf("%d",&row);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        int cnt=0,num;
        for(int i=1;i<=4;i++)
        {
            cnt+=ans[b[row][i]];
            if(ans[b[row][i]])
                num=b[row][i];
        }   
        printf("Case #%d: ",T);
        if(cnt==1)
            cout<<num<<endl;
        else if(cnt>=2)
            puts("Bad magician!"); 
        else
            puts("Volunteer cheated!");        
    }
    return 0;
}
