# include <iostream>
# include <cstdio>
# include <string.h>
# include <string> 
using namespace std;
int x,l,t;
string cal(string u,char v)
{
	if (u=="1")
	{
		if (v=='1')return "1";
		else if (v=='i')return "i";
		else if (v=='j')return "j";
		else return "k";
	}
	else if (u=="-1")
	{
		if (v=='1')return "-1";
		else if (v=='i')return "-i";
		else if (v=='j')return "-j";
		else return "-k";
	}
	else if (u=="i")
	{
		if (v=='1')return "i";
		else if (v=='i')return "-1";
		else if (v=='j')return "k";
		else return "-j";
	}
	else if (u=="-i")
	{
		if (v=='1')return "-i";
		else if (v=='i')return "1";
		else if (v=='j')return "-k";
		else return "j";
	}
	else if (u=="j")
	{
		if (v=='1')return "j";
		else if (v=='i')return "-k";
		else if (v=='j')return "-1";
		else return "i";
	}
	else if (u=="-j")
	{
		if (v=='1')return "-j";
		else if (v=='i')return "k";
		else if (v=='j')return "1";
		else return "-i";
	}
	else if (u=="k")
	{
		if (v=='1')return "k";
		else if (v=='i')return "j";
		else if (v=='j')return "-i";
		else return "-1";
	}
	else 
	{
		if (v=='1')return "-k";
		else if (v=='i')return "-j";
		else if (v=='j')return "i";
		else return "1";
	}
}
int main()
{
//	freopen("in.txt","r",stdin);
  //  freopen("out.txt","w",stdout);
	int i,j;
	string str="",temp,sum;
	char s[20010],c;
	bool ans,flag;;
	scanf("%d",&t);
	for (j=1;j<=t;j++)
	{
		scanf("%d %d",&l,&x);
		scanf("%s",&s);
		temp=str="";ans=1;
		for (i=0;i<strlen(s);i++)temp+=s[i];
		for (i=1;i<=x;i++)str+=temp;
		for (i=0,flag=0,sum="1";i<str.size();i++)
		{
			sum=cal(sum,str[i]);
			if (sum == "i"){
				flag=1;
				break;
			}
		}
		if (flag==0){printf("Case #%d: NO\n",j);continue;}
		for (i=i+1,flag=0,sum="1";i<str.size();i++)
		{
			sum=cal(sum,str[i]);
			if (sum == "j"){
				flag=1;
				break;
			}
		}
		if (flag==0){printf("Case #%d: NO\n",j);continue;}
		for (i=i+1,flag=0,sum="1";i<str.size();i++)sum=cal(sum,str[i]);
		if (sum!="k"){printf("Case #%d: NO\n",j);continue;}
		printf("Case #%d: YES\n",j);
	} 
	return 0;
} 
