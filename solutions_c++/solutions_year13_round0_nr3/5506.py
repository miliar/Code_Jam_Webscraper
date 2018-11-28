#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int z=0;z<t;z++)
    {
        int a,b,s=0;
        cin>>a>>b;
        for(int c=sqrt(a),d=sqrt(b);c<=d;c++)
        {
            int p=pow(c,2);
            if(p>=a&&p<=b)
            {
                int l=ceil(log10(c+1));
                bool ok=true;
                for(int i=0,j=l/2;i<j;i++)
                {
                    if((int)(c/pow(10,i))%10!=(int)(c/pow(10,l-i-1))%10)
                    {
                        ok=false;
                    }
                }
                if(ok)
                {
                    l=ceil(log10(p+1));
                    ok=true;
                    for(int i=0,j=l/2;i<j;i++)
                    {
                        if((int)(p/pow(10,i))%10!=(int)(p/pow(10,l-i-1))%10)
                        {
                            ok=false;
                        }
                    }
                    if(ok)
                        s++;
                }
            }
        }
        cout<<"Case #"<<z+1<<": "<<s<<'\n';
    }
    cout<<flush;
}
