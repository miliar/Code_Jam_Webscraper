#include<iostream>
#include<string.h>
using namespace std;
int check(char s[])
{
	int flag=0;
	int n=strlen(s);
	for(int i=0;i<n;i++)
	{
		if(s[i]!='+'){
			flag=1;
			break;
		}
	}
	if(flag==1)return 0;
	return 1;
}
void flip(char s[],int start,int end){
	for(int i=start;i<=end;i++){
		if(s[i]=='-')s[i]='+';
		else s[i]='-';
	}
	char temp;
    while (start < end)
    {
        temp = s[start];   
        s[start] = s[end];
        s[end] = temp;
        start++;
        end--;
    }   
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output_large","w",stdout);
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
		int ans=0,count=0,flag=0;
		char s[200];
		cin>>s;
		int len=strlen(s);
		while(1)
		{
				ans=check(s);
				if(ans==1)
					{cout<<"Case #"<<k+1<<": "<<count<<endl;break;}
			else
			{
			for(int i=0;i<len;i++)
			{
					if(s[i]!=s[i+1]){
						flip(s,0,i);
						count++;
						flag=1;
						i=len;
					}
			}
			if(flag==0)
			{
				flip(s,0,len-1);
				count++;
				cout<<"Case #"<<k+1<<": "<<count<<endl;
				break;
			}
			}
			flag=0;
		}
	}
	return 0;
}
