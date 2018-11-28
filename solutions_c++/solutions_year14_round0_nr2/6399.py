#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("C:\\Users\\Shaival\\Desktop\\B-large.in","r",stdin);
    freopen("C:\\Users\\Shaival\\Desktop\\OP1.txt","w",stdout);
    int t;
    int I;
    scanf("%d",&t);
    for(I=1;I<=t;I++)
    {
        double C,F,X;
        cin>>C>>F>>X;
        int i,j;
        double Ans=0,Cmp1=0,Cmp2=0;
        double tReq=0;
        double tBuild=0;
        double tFin,tNxtBuild;
        double r=2.0;
     //   cout<<C<<" "<<F<<" "<<X<<endl;
        while(1)
        {
            tReq=X/r;
            tBuild=C/r;
            Cmp1=Ans+tReq;
            Cmp2=Ans+tBuild+X/(r+F);
            //printf("%lf %lf\n",Cmp1,Cmp2);
            if(Cmp2<Cmp1)
            {
                r+=F;
                Ans+=tBuild;
            }
            else
            {
                Ans+=tReq;
                break;
            }
        }
//        printf("%lf %lf\n",tReq,tBuild);
        printf("Case #%d: %.7lf\n",I,Ans);
    }
    return 0;
}
