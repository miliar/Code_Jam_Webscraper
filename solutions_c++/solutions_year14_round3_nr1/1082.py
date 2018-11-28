#include <fstream>
#include <iostream>
#include <string>

using namespace std;

long long int gcd(long long int a,long long int b)
{
    return b==0?a:gcd(b,a%b);
}

int main()
{
    int t;
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in");
    fout.open("output.txt");
    fin>>t;
    for(int k=1;k<=t;++k)
    {
        long long int p=0,q=0;
        string s;
        bool f=false;
        fin>>s;
        for(int i=0;i<s.size();++i)
        {
            if(s[i]=='/')
            {
                f=true;
                continue;
            }
            if(!f)p*=10,p+=s[i]-48;
            else q*=10,q+=s[i]-48;
        }
        //cout<<p<<" "<<q<<endl;
        long long int g=gcd(p,q);
        //cout<<g<<endl;
        p/=g,q/=g;
        long long int l=q,n=0;
        while(l%2==0)l/=2,n++;
        if(l!=1||n>40)
        {
            fout<<"Case #"<<k<<": impossible"<<endl;
            //fout<<"SEGESG"<<endl;
            continue;
        }
        int ans=0;
        while(p<q/2)q/=2,++ans;
        fout<<"Case #"<<k<<": "<<ans+1<<endl;
    }
    return 0;
}
