/*Standing Ovation*/
#include<iostream>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1_large.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {   int n;
        cin>>n;
        string s;
        cin>>s;
        int ans=0,temp=s[0]-'0',i=1;
        while(i<=n)
        {   if(s[i]!='0'&&temp<i)
            {   ans+=i-temp;
                temp+=i-temp;
            }
            temp+=s[i]-'0';
            i++;
        }
        cout<<"Case #"<<cas<<": "<<ans<<endl;
        cas++;
    }
    return 0;
}
