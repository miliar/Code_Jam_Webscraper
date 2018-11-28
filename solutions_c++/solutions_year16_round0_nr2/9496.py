#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<climits>
#define ll long long
using namespace std;


void swaping(string str,int init,int fin)
{
    while(init<fin)
    {
        swap(str[init],str[fin]);
        if(str[init]=='+')
            str[init]=='-';
        else
            str[init]=='+';
        if(str[fin]=='+')
            str[fin]=='-';
        else
            str[fin]=='+';
        init++;
        fin--;
    }
    if(init==fin)
    {
        if(str[init]=='-')
            str[init]='+';
        else
            str[init]='-';
            return;
    }

}
int main()
{
    freopen("inter.in","r",stdin);
    freopen("outer.out","w",stdout);
	ll t,y=1;
	string s;
	cin>>t;
	while(t--)
	{
		ll plus=0,minus=0,ret;
		cin>>s;
		ll n=s.length();
		for(int i=0;i<n;i++)
		{
			if(s[i]=='+')  plus++;
			if(s[i]=='-')  minus++;
		}
		if(minus==0)
		{
			cout<<"Case #"<<y<<": "<<"0"<<endl;
			y++;
			continue;
		}
		if(plus==0)
        {
            cout<<"Case #"<<y<<": "<<"1"<<endl;
            y++;
            continue;
        }
		int final=0;
		long long p=LONG_LONG_MAX;
		while(final<n)
        {
            long long ans=0,cnt=0;
            bool flag=false;
            ret=n-1;
            while(s[ret]=='+')
                ret--;
            int i=0;
            if(s[0]=='+')
                cnt++;
            while(s[i]=='+')
                i++;
            while(i<=ret)
            {
                if(s[i]=='-' && flag==false)
                {
                    i++;
                    continue;
                }
                if(s[i]=='-' && flag==true)
                {
                    ans+=2;
                    flag=false;
                    i++;
                    continue;
                }
                if(s[i]=='+')
                {
                    flag=true;
                    i++;
                }
            }
            if(cnt==1)
                ans++;
			p=min(p,ans);
			ans=0;
			swaping(s,0,final);
			ans++;
			final++;
        }
        cout<<"Case #"<<y<<": "<<(p+1)<<endl;
        y++;
    }
return 0;
}
