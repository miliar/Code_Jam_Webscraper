#include<bits/stdc++.h>
using namespace std;
long long con(long long num, int base)
{
    long long  op=0;
    long long k=num;
    long long p=1,s;
    while(k!=0)
    {
        s=k%10;
         k=k/10;
         op=op+s*p;
         p=p*base;
    }
    return op;
}

long long div(long long m)
{
    int s=sqrt(m);
    long long ans=0;
    for(int i=2;i<=s;i++)
    {
        if(m%i==0)
        {
            ans=i;
            break;
        }
    }
    return ans;
}

long long bin(long long n)
{
    long long rem, i=1, binary=0;
    while (n!=0)
    {
        rem=n%2;
        n/=2;
        binary+=rem*i;
        i*=10;
    }
    return binary;
}
int main()
{
    int t=1,T,n,i,j;
    long long k,c,p,q,b,m,kcon;
    vector<long long> ans;
    ifstream infile;
    infile.open("C-small-attempt0.in");
    ofstream outfile;
    outfile.open("output.txt");
    infile>>T;
    while(T--)
    {
        infile>>n>>k;
        p=pow(2,n-1)-1;
        q=pow(2,n)-1;

        kcon=0;
        outfile<<"Case #"<<t++<<": "<<endl;

        for(i=p+2;i<=q;i=i+2)
        {
            ans.clear();
            b=bin(i);
            for(j=2;j<11;j++)
            {
                m=con(b,j);
                if(div(m)==0)
                {
                    //cout<<m<<endl;
                    break;
                }
                else
                {
                    //cout<<div(m)<<endl;
                    ans.push_back(div(m));
                }
            }
            if(ans.size()==9)
            {
                outfile<<b<<" ";
                for(int s=0;s<ans.size();s++) outfile<<ans[s]<<" ";
                outfile<<endl;
                kcon++;
                if(kcon==k) break;
            }
        }
    }
    infile.close();
    outfile.close();
}
