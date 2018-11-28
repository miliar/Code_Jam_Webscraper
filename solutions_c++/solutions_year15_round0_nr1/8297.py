#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    ifstream in("in.txt");
    ofstream out("out.txt");
    int t,p=1;
    in>>t;
    while(t--)
    {
        int n;
        string s;
        in>>n;
        in>>s;
        long long sum=0,c=0;
        if(s[0]=='0')
        {
            c=1;
            sum=1;
        }
        else
            sum=s[0]-'0';
        for( int i = 1 ; i < n+1 ; i++)
        {
            if( sum < i )
            {
                c+=i-sum;
                sum+=i-sum;
            }
            sum+=(s[i]-'0');
        }
        out<<"Case #"<<p<<": "<<c<<endl;
        p++;
    }
    return 0;
}
