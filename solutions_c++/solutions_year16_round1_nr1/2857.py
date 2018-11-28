#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	ll t,cnt,i,slen;
	string s;
	cin>>t;
	cnt=0LL;
	while(t--)
    {
        cnt++;
        cin>>s;
        string temp;
        temp=temp+s[0];
        slen=s.length();
        for(i=1;i<slen;i++)
        {
            if(s[i]<temp[0])
            {
                temp=temp+s[i];
            }
            else
            {
                temp=s[i]+temp;
            }
        }
        cout<<"Case #"<<cnt<<": "<<temp<<"\n";
        s.clear();
        temp.clear();
    }
    return 0;
}