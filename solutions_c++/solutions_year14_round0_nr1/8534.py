
// User: lovelotus(Prem Kamal)

//#include<bits/stdc++.h>
//#define _ ios_base::sync_with_stdio(0);cin.tie(0);

#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<map>
#include<string>
#include<vector>
#include<queue>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<stack>
#include<set>
#include<utility>
#define pii pair<int,int>
#define pip pair<int,pii>
#define F first
#define S second
#define lli long long int
using namespace std;

int a[20];

int main()
{
    freopen("C:\\Users\\lovelotus\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\lovelotus\\Desktop\\output.txt","w",stdout);
    int tst=1,t,i,j,p,c,x;
    scanf("%d",&t);
    while(t--)
    {
        memset(a,0,sizeof(a));
        c=2;
        while(c--)
        {
            scanf("%d",&p);
            p--;
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    scanf("%d",&x);
                    if(i==p) a[x]++;
                }
            }
        }
        int ans=0,err=0;
        for(i=1;i<17;i++)
        {
            if(a[i]>1)
            {
                if(!ans) ans=i;
                else err=1;
            }
        }
        printf("Case #%d: ",tst);
        if(!ans) printf("Volunteer cheated!\n");
        else if(err) printf("Bad magician!\n");
        else printf("%d\n",ans);
        tst++;
    }
    return 0;
}
