#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<deque>
#include<bitset>
#define ll __int64
#define inf 0x7FFFFFFF
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
double c,f,x;
double allSec,v;
int judge()
{
    if(c>=x) {allSec+=x/v;return 2;}
    double go2Time=x/v;
    double go1Time=c/v+x/(v+f);
    if(go2Time-go1Time>1e-9)
    {
        allSec+=c/v;
        v+=f;
        return 1;
    }
    allSec+=go2Time;
    return 2;
}
int main()
{
    int i,j,k;
    int n,m,t;
    freopen("B-large.in","r",stdin);freopen("B-large-output.txt","w",stdout);
    scanf("%d",&t);for(int tcase=1;tcase<=t;tcase++)
    //while(scanf("%d",&n)!=EOF)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        allSec=0;
        v=2.0;
        while(1)
        {
            if(judge()==1)// get a farm
            {
                //cout<<allSec<<endl;
            }
            else
            {
                //cout<<allSec<<endl;
                break;
            }
        }
        printf("Case #%d: ",tcase);
        printf("%.7lf\n",allSec);
    }
    fclose(stdin);
    fclose(stdout);
}
