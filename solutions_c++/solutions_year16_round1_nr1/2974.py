#include <bits/stdc++.h>
using namespace std;
#define ll long long
bool p[100000001];
ll t,n,j,primes[6000005],k;
int main()
{
    ifstream inFile;
    ofstream outFile;
    inFile.open("input.txt");//("B-small-attempt0.in");
    outFile.open("output_file.txt");
    inFile>>t;
    for(int i=1;i<=t;i++)
    {
        outFile<<"Case #"<<i<<": ";
        int cnt=0;
        string str,ans="",temp;
        inFile>>str;
        ans+=str[0];
        for(int j=1;j<str.size();j++)
        {
            if(str[j]>=ans[0])
            {
                temp="";
                temp+=str[j];
                temp+=ans;
                ans=temp;
            }
            else
            {
                ans+=str[j];
            }
        }
        outFile<<ans<<endl;
    }
    return 0;
}
