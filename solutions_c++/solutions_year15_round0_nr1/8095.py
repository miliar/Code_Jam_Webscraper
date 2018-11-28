#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    ifstream in("A-large.in");
    ofstream out("out.out");
    in>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        string s;
        in>>n>>s;
        int up=s[0]-'0';
        long long v=0;
        for(int j=1;j<=n;j++)
        {
            //cout<<"\n\n "<<up<<" people are clapping and we want to make people of shyness level "<<j<<" stand up \n\n";
            if(up<j)
            {
                int temp= j-up;
                v+=temp;
                up+=temp;
            }
            up+=s[j]-'0';
        }
        //printf("Case #%d: %I64d\n",i+1,v);
        out<<"Case #"<<i+1<<": "<<v<<'\n';
    }
    return 0;
}
