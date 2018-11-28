#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("example2.txt","r",stdin);
    freopen("output2.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        double c,f,x,prevsum,currensum,n,totalsum;
        double count=0;
        cin>>c>>f>>x;
       // n=2.0;
        prevsum = x/2;

        currensum= c/2+ x/(f+2);
        totalsum=c/2;
        while(currensum <prevsum)
        {

            count++;
            prevsum=currensum;
            totalsum+=c/((count*f) +2);
            currensum=totalsum+ x/(2+(count+1)*f);


        }
      //  cout<<prevsum<<" ";
    //    totalsum+=x/(2+count*f);

       printf("Case #%d: %0.7lf\n",i,prevsum);

    }
}
