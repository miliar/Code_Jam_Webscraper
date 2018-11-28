#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
        int tc,i;
        cin>>tc;
        double C,F,X,epsilon=0.000001;
        double ans;
        double max,min,val,j,n;
        for(i=0;i<tc;i++)
        {
                cin>>C>>F>>X;
                max=((F*X)/C);        //last term's max value
                min=(((X-C)*F)/C);    //last term's min value
          //      cout<<max<<"\n"<<min<<"\n";
                val=0;
                for(n=0;;n++)
                {
                    val=2+(n*F);
                    if(val<=max && val>=min)
                        break;
                    if(max<2)
                        break;
                }
             //   cout<<n<<"\n"<<val<<"\n";
                ans=0;
                for(j=0;j<=n;j++)     //adding all the terms
                {
                    if((2+j*F)==val)
                    {
                        ans+=X/(2+(j*F));
                        break;
                    }
                    ans+=C/(2+(j*F));
                }
                printf("Case #%d: %.7f\n",i+1,ans);
        }
        return 0;
}
