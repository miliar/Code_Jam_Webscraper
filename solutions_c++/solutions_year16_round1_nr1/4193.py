#include<bits/stdc++.h>
using namespace std;
int main()
{
   // cin.sync_with_stdio(false);
   // cin.tie(0);
    ifstream in("large.in");
    ofstream out("b.txt");
    int t,n,i,j,len,var,ar[30];
    string str;
    in>>t;
    var=0;
    while(t--)
    {
        var++;
        out<<"Case #"<<var<<": ";
        in>>str;
        len=str.size();
        memset(ar,0,sizeof(ar));
        string ans="";
        ans+=str[0];
        for(i=1;i<len;i++)
        {
            if(str[i]>=ans[0])
                ans=str[i]+ans;
            else
                ans+=str[i];
        }
        out<<ans<<'\n';
    }
}

