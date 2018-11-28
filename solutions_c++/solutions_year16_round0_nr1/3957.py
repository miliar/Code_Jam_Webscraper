#include<bits/stdc++.h>
using namespace std;


int main()
{
    freopen("in3.in","r",stdin);
    freopen("out3.out","w",stdout);

    int i,j,k;
    int a,b,c;
    long long n,x,y;
    int t;

    cin>>t;

    i=1;

    while(t--)
    {
        cin>>n;

        vector<bool> found(10,false);
        j=0;

        if(n==0)
            k=0;

        else
        {
            x=0;

            while(j<10)
            {
                x+=n;

                //analyze the digits 
                
                y=x;

                while(y)
                {
                    a=y%10;
                    y/=10;

                    if(found[a]==false)
                    {
                        j++;
                        found[a]=true;
                    }
                }
            }
        }

        cout<<"Case #"<<i<<": ";

        if(n==0)
        {
            cout<<"INSOMNIA";
        }
        
        else
        {
            cout<<x;
        }

        cout<<endl;
        i++;
    }
   
    return 0;
}
