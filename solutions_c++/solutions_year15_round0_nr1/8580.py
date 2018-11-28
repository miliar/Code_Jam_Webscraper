#include<bits/stdc++.h>

using namespace std;
#define ll long long int

int main()
{   freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    int t;
    cin>>t; int j=1;
    while(t--)
    {
        int smax; cin>>smax;
        char ch; cin>>ch;

        int ans=0,rsum=1,sum=0,k=1;

        if((int(ch)-48)==0) { ans++; sum=sum+1; }
        else
            sum=(int(ch)-48);

        while(smax--)
        {
         if(rsum>sum)
         {
             ans=ans+(rsum-sum);
             sum=rsum;
         }

         rsum++;

         cin>>ch;

         sum=sum+(int(ch)-48);




        }



         cout<<"Case #"<<j<<": "<<ans<<"\n";
         j++;

    }


    fclose (stdout);
    return 0;
}

