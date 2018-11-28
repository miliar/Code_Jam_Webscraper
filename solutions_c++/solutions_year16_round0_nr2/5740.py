#include<bits/stdc++.h>

using namespace std;
#define MOD 1000000007
#define M_PI 3.14159265358979323846
#define M_PIl 3.141592653589793238462643383279502884L

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t; cin>>t; int ch,cnt;
    for(int tc=1;tc<=t;tc++)
    {
        string s;
        cin>>s; ch=-1; cnt=0;
        for(int i=s.size()-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                if(ch==1)
                {
                    if(cnt%2==1)
                    {
                        cnt++;
                    }
                }
                ch=0;
            }
            else
            {
                if(ch==0)
                {
                    if(cnt%2==0)
                    {
                        cnt++;
                    }
                }
                ch=1;
            }
        }
        if(s[0]=='-')
        {
            if(cnt%2==0)
            {
                cnt++;
            }
        }
        else
        {
            if(cnt%2==1)
            {
                cnt++;
            }
        }
        cout<<"Case #"<<tc<<": "<<cnt<<endl;
    }
    return 0;
}
