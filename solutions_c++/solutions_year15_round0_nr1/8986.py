#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<set>
#include<cmath>
#include<cstdlib>
#include<string>
#include<stack>
#include<queue>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    //freopen("in.txt","r",stdin);
    //freopen("a.txt","w",stdout);

    int t,test=0;

    cin>>t;
    int smax;
    string s;
    while(t--)
    {
        cout<<"Case #"<<++test<<": ";
        cin>>smax>>s;
        //cout<<smax<<" "<<s<<endl;
        int standing=s[0]-'0';
        int res=0;
        for(int i=1;i<=smax;i++)
        {
            if(s[i]-'0'!=0)
            {
                if(standing>=i)standing+=s[i]-'0';
                else{
                    res+=i-standing;
                    standing+=i-standing;
                    standing+=s[i]-'0';
                }

            }
        }
        cout<<res<<endl;

    }




return 0;
}
