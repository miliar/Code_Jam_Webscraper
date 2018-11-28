#include<bits/stdc++.h>
using namespace std;
#define ll int
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    ll cnt,len,m,ans,test,i,j,num,neg,pos;
    bool flag;
    cin>>test;
    char ch;
    for(ll k=1;k<=test;k++)
    {
    	string str;
    	cnt=0;
    	cin>>str;
    	len=str.length();
    	for(i=1;i<len;i++)
    	{
    		if(str[i]!=str[i-1])
    			cnt++;
    	}
    	if(cnt%2==1)
    	{
    		if(str[0]=='+')
    			cnt++;
    	}
    	else
    	{
    		if(str[0]=='-')
    			cnt++;
    	}
    	printf("Case #%d: %d\n",k,cnt);
    }
    return 0;
}
