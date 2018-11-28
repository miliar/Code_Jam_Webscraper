#include<iostream>
#include<stdio.h>
#include<fstream>

using namespace std;

//ifstream fin("input.txt");
//ofstream fout("output.txt");

int main()
{
    std::ios::sync_with_stdio(false);
    int t,c=1;
    cin>>t;
    while(t--)
    {
        int n,cnt=0,ans=0,k,m;
        bool ck[10]={false};
        cin>>n;
        if(n==0)
            cout<<"Case #"<<c<<": INSOMNIA\n";
        else
        {
            int i=1;
            while(cnt<10)
            {
                m=n*i;
                while(m)
                {
                    k=m%10;
                    if(ck[k]==false)
                        cnt++,ck[k]=true;
                    m/=10;
                }
                i++;
            }
            ans=n*(i-1);
            cout<<"Case #"<<c<<": "<<ans<<endl;
        }
        c++;
    }
    return 0;
}
