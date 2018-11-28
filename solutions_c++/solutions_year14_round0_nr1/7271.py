#include<stdio.h>
#include<iostream>
#include<set>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<cmath>
#include<ctype.h>
#define LL unsigned long long
#define h1t35h using
#define rocks namespace
#define theworld std;
#define SI(n) scanf("%d",&n);
#define SF(n) scanf("%f",&n);
#define SLL(n) scanf("%lld",&n);
#define SC(n) scanf("%c",&n);
#define PC(n) printf("%c",&n);
#define PI(n) printf("%d",n);
#define PF(n) printf("%f",n);
#define PLL(n) printf("%lld",n);
#define FOR(x,n) for(x=0;x<(n);x++)
#define FORL(x,a,b) for(x=a;x<b;x++)
LL gcd(LL a, LL b)
{
    return b?gcd(b,a%b):a;
}
h1t35h rocks theworld;
int main()
{
    register int loop,test,i,j;
    //freopen("A-small-attempt0","r",stdin);
    SI(test);
    loop=0;
    int ans1,ans2;
    while(loop<test)
    {
        SI(ans1)
        int mat[4][4];
        bool num[17]= {false};
        FOR(i,4)
        {
            FOR(j,4)
            {
                SI(mat[i][j])
                if(i==ans1-1)
                {
                    num[mat[ans1-1][j]]=true;

                }
            }
        }
        SI(ans2)
        FOR(i,4)
        {
            FOR(j,4)
            {
                SI(mat[i][j])
            }
        }
        int cnt=0;
        int val;
        FOR(j,4)
        {
            if(num[mat[ans2-1][j]])
            {
                cnt++;
                val=mat[ans2-1][j];
            }

        }
        if(cnt==1)
        {
            cout<<"Case #"<<loop+1<<": "<<val<<endl;
        }
        else if(cnt==0)
        {
            cout<<"Case #"<<loop+1<<": Volunteer cheated!"<<endl;
        }
        else
        {
            cout<<"Case #"<<loop+1<<": Bad magician!"<<endl;
        }
        loop++;
    }
    return 0;
}

