#include<iostream>
#include<string>
#include<fstream>
using namespace std;

ofstream fout ("A.out");
  ifstream fin ("A-large.in");
int main()
{
    int t,n,q,br,ans;
    fin>>t;
    string s;
    for(int t1=1;t1<=t;t1++)
    {
        fin>>n>>s;
        br=0;
        ans=0;
        for(int i=0;i<=n;i++)
        {
            q=s[i]-'0';
            if(q>0)
            if(i<=br)br+=q;
            else
            {//fout<<br<<" "<<i<<endl;
                ans+=i-br;
                br=i+q;
            }
        }
        fout<<"Case #"<<t1<<": "<<ans<<endl;
    }
    return 0;
}
