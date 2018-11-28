#include <iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define lld long long int
char stg[100005];
lld str[100005];
int main()
{
    lld l,t,i,j,x,k,a,s,sts,m;
    freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    lld ar[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
    for(m=1;m<=t;m++)
    {
        cin>>l>>x;
        cin>>stg;
        k=0;
        for(i=0;i<x;i++)
        {
            for(j=0;j<l;j++,k++)
                str[k]=(stg[j]-'i'+2);
        }
        a=1;
        s=1;
        sts=0;
        for(i=0;i<l*x;i++)
        {
            a=ar[a][str[i]];
            if(a<0)
            {
                a=a*(-1);
                s=s*(-1);
            }
            if(s==1&&(sts==0&&a==2||sts==1&&a==3||sts==2&&a==4))
            {
                sts++;
                a=1;
            }
        }

        cout<<"Case #"<<m<<": ";
        if(sts==3&&a==1&&s==1)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
	return 0;
}
