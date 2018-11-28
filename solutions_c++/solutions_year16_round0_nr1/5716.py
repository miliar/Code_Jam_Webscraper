#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
    ifstream fp;
    fp.open("A-large.in",ios::in);
    ofstream fo;
    fo.open("out1.txt",ios::out);
    int t;
    long long int i,j,z,n,flag,k,l;
    fp>>t;
    for(i=1;i<=t;i++)
    {
        fp>>n;
        l=n;
        int t[10];
        for(j=0;j<10;j++)
        {
            t[j]=0;
        }
        if(n==0)
        {
            fo<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }
        else
        {
            while(1)
            {
                lb:
                z=n;
                while(z>0)
                {
                    k=z%10;
                    //cout<<k<<endl;
                    t[k]=1;
                    z/=10;
                }
                for(j=0;j<10;j++)
                {
                    if(t[j]==0)
                    {
                        n+=l;
                        goto lb;
                    }
                }
                break;
            }
            fo<<"Case #"<<i<<": "<<n<<endl;
        }
    }

}
