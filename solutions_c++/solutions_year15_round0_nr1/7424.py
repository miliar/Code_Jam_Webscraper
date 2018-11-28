#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int t,n,ans;
char ipt[1001];
int sum;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int main()
{
    fin>>t;
    for(int c=1;c<=t;c++)
    {
        ans=0;
        sum=0;
        fin>>n;
        fin>>ipt;
        
        for(int i=0;i<=n;i++)
        {
            if(i>sum)
            {
                ans+=i-sum;
                sum+=(i-sum);
            }
            sum=sum+(ipt[i]-'0');
        }
        fout<<"Case #"<<c<<": "<<ans<<endl;
    }
}