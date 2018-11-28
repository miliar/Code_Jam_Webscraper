/*
name:Hatsune_Miku
*/
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	char s[1050];
	string ss;
	int temp=T;
	while(T--)
	{
		cin>>s;
		int len=strlen(s);
		ss="";
		ss+=s[0];
		char max=s[0];
		for(int i=1;i<len;i++)
		{
			if(s[i]>=max)
			{
				ss=s[i]+ss;
				max=s[i];
			}
			else{
				ss=ss+s[i];
			}
		}
		printf("Case #%d: ",temp-T);
		printf("%s\n",ss.c_str());
	}
	return 0;
} 
