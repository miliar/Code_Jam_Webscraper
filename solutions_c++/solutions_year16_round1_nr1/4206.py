#include<iostream>
#include<string.h>
using namespace std;

char* insert(char s1[],char s2[],int l)
{
	char temp[1001];
	int i;
	if(l<0)
	return NULL;
	else
	{
		for(i=0; i<l; i++)
		{
			if(i==0)
			{
				s2[i]=s1[i];
			}
			else if(s2[0]>s1[i])
			{
				s2[i]=s1[i];
			}
			else
			{
				temp[0]=s1[i];
				for(int i=0; i<l ;i++)
				{
					temp[i+1]=s2[i];
				}
				strcpy(s2,temp);
			}
		}
		s2[i]='\0';
		return s2;
	}
}
int main()
{
	int t,t1=1,len,cnt;
	cin>>t;
	char str[1001],str_new[1001],*s;
	while(t>0){
	cin>>str;
	len=strlen(str);
	cnt=len;
	s=insert(str,str_new,len);
	strcpy(str_new,s);
	cout<<"Case #"<<t1<<": "<<str_new<<endl;
	t--;
	t1++;
	}
}
