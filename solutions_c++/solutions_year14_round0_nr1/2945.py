/*
Author:BobLee
Email:BobLee0717@gmail.com
*/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<map>
#include<string>
#include<vector>
using namespace std;

const int maxn = 5;

int data[maxn][maxn];
int jilu[17];
int fa;
int sa;

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-out.out","w",stdout);
    int t;
    cin>>t;
    int ca=1;

    while(t--)
    {
        memset(jilu,0,sizeof(jilu));
        cin>>fa;
        int tmp;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>tmp;
                if(i==fa)
                    jilu[tmp]++;
            }
        }
        cin>>sa;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>tmp;
                if(i==sa)
                    jilu[tmp]++;
            }
        }

        int co = 0;
        int ans;
        for(int i=1;i<=16;i++)
        {
            if(jilu[i]==2)
            {
                ans = i;
                co++;
            }
        }

        printf("Case #%d: ",ca++);
        if(co==0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(co==1)
        {
            printf("%d\n",ans);
        }
        else
            printf("Bad magician!\n");


    }
    return 0;
}
