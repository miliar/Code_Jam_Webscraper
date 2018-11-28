#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

typedef long long ll;

int main() 
{
	freopen("/Users/vivek.v/Desktop/input.txt","r",stdin);
	freopen("/Users/vivek.v/Desktop/output.txt","w",stdout);
	
	ll T,s,i,len,tt,up,needed,cnt,temp;
	string ss;
	cin>>T;
	for(tt = 1; tt <= T; tt++)
	{
		cin>>s; cin>>ss;
		len = ss.size();
		up = (ss[0]-'0');
		cnt = 0;
		for(i = 1; i < len; i++)
		{
			if(up < i)
			{
				temp = (i - up);
				cnt += temp;
				up += temp;
			}
			up += (ss[i]-'0');
		}
		cout<<"Case #"<<tt<<": "<<cnt<<endl;
	}
	return 0;
}
