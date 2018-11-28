#include<iostream>

using namespace std;

int main()
{
    freopen ("output.txt","w",stdout);
    freopen ("input.txt","r",stdin);
    int tc;
    cin>>tc;
    long int ans;
    int smax;
    long int cursum;
    char *si;
    for(int i = 0 ; i < tc  ; i++)
    {
        ans=0;
        cursum=0;
        cout<<"Case #"<<(i+1)<<": ";
        cin>>smax;
 //       cout<<smax<<" ";
        si=new char [smax+1];
        for(int j=0; j<=smax ; j++)
        {
            if(cursum<j)
            {
                ans++;
                cursum++;
            }
            cin>>si[j];
            cursum +=si[j]-'0';
        //   cout<<endl<<si[j]<<endl;
          //  cout<<"fasdf"<<cursum<<endl;
        }

        delete []si;
        cout<<ans<<endl;
    }
}
