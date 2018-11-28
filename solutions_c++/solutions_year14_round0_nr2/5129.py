#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int tc,i,j,k;
    double c,f,x,n=2,sum,curr,prev;
    cin>>tc;
    for(k=1;k<=tc;k++)
    {
        //cin>>c>>f>>x;
        scanf("%lf%lf%lf",&c,&f,&x);
        n=2;
        prev=x/2;
        sum=0;
        while(1)
        {
            sum+=c/n;
            //cout<<sum<<endl;
            n+=f;
            curr=sum+(x/n);
            //cout<<curr<<" "<<prev<<endl;
            if(curr>=prev)
                break;
            else
              {

                prev=curr;
              }

        }
        //cout<<prev<<endl;


        printf("Case #");
        printf("%d",k);
        printf(": ");
        printf("%0.7lf\n",prev);
    }
    return 0;
}
