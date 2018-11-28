#include<bits/stdc++.h>
using namespace std;
int main()
{
int T,N,ans=0,tot=0;
string str;
cin>>T;
for(int j=1;j<=T;j++)
{
tot=0;
ans=0;
cin>>N;
cin>>str;
for(int i=0;i<=N;i++)
{
				int temp=str[i]-'0';
				if(ans<i){
					tot+=(i-ans);
					ans=i;
				}
				ans+=temp;

}

cout<<"Case #"<<j<<": "<<tot<<endl;
}
return 0;
}