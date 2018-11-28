#include<bits/stdc++.h>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
int main()
{
    //READ("A-large.in");
    //WRITE("A-large.out");
    long long int t, n,maxx=0,res=0;
    cin>>t;
    string s="";
    for(int i=0;i<t;i++)
    {
        cin>>n;
        cin>>s;
        maxx = 0;
        res=0;
        for(int j=0;j<n+1;j++)
        {
            if(s[j]!='0')
            {
                if(maxx >= j)
                    maxx+=(s[j]-'0');
                else
                {
                    res+=(j-maxx);
                    maxx+=(j-maxx);
                    j--;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<res<<endl;
    }
}
