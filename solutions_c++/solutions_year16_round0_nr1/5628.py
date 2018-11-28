#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define sl(n) scanf("%lld",&n)
ll a[10];
int main()
{
    ifstream fin;
    ofstream fout("ans.txt");
    fin.open ("input.in");

    if(!fin.is_open())
    {
        cout<<"file error";
    }
    else
    {
        ll t;
        fin>>t;
        //cin>>t;
        ll t1=t;
        while(t--)
        {
            ll flag=0,m,x,n;
            fin>>n;
            //cin>>n;
            if(n==0)
            {
                fout<<"Case #"<<t1-t<<": ";
                fout<<"INSOMNIA"<<endl;
            }
            else
            {
                fill_n(a,10,0);
                x=1;
                while(flag!=1)
                {
                    m=n*x;
                    while(m>0)
                    {
                        a[m%10]++;
                        m=m/10;
                    }
                    flag=1;
                    for(int i=0;i<10;i++)
                    {
                        if(a[i]==0)
                        flag=0;
                    }
                    if(flag==1)
                        break;
                    x++;
                }
                fout<<"Case #"<<t1-t<<": "<<n*x<<endl;
            }
        }
        fin.close();
        fout.close();
    }
}
