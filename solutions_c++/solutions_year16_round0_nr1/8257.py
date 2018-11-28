#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
    int t;
    cin>>t;
  for(int z=1;z<=t;z++)
    {
        long int inp,ans;
        int i,f=0,j,tep;
        cin>>inp;
        if(inp==0)
            cout<<"Case #"<<z<<": INSOMNIA\n";
        else
        {
            int a[10]= {0,0};

            for(j=1; j>0; j++)
            {

                long int inp1=inp*j;
                ans=inp1;
                do
                {
                    tep=inp1%10;
                    a[tep]++;
                    inp1/=10;
                }
                while(inp1);

                for(i=0; i<10; i++)
                    if(!a[i])
                        break;
                if (i==10)
                {
                    f=1;
                    break;
                }

            }
            cout<<"Case #"<<z<<": "<<ans<<endl;
        }
    }
    return 0;
}
