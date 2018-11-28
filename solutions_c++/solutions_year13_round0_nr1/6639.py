#include<iostream>
#include<fstream>
#include<cstring>
#include<stdio.h>
using namespace std;
char str[6][300],ch;
int main()
{
	int i,k,t,flag,f,j;
	char ch,s;
	//cout<<sizeof(a)<<i;
	//scanf("%d",&t);
	ifstream p("p.txt");
	ofstream o("pra.txt");
	p>>t;
	p.get(ch);
	for(k=1;k<=t;k++)
	{
		
		int f2=1,f3=1,f4=0,f1=0;
		for(i=0;i<=4;i++)
		{
			fflush(stdin);
			p.getline(str[i],300);
			//cout<<str[i]<<endl;
		}
		/*for(i=0;i<4;i++)
		{
			cout<<str[i]<<" ";
			cout<<endl;
		}
		cout<<endl<<endl;*/
		o<<"Case #"<<k<<": ";
		for(i=0;i<4;i++)
		{
			flag=1;f=1;
			for(j=0;j<4;j++)
			{
				if(str[i][j]=='X'||str[i][j]=='T')
					{
						flag*=1;
					}
				else flag*=0;
				if(str[i][j]=='O'||str[i][j]=='T')
					f*=1;
				else f*=0;
				if(i==3-j)
				{
					if(str[i][j]=='X'||str[i][j]=='T')
						f2*=1;
					else f2*=0;
					if(str[i][j]=='O'||str[i][j]=='T')
						f3*=1;
					else f3*=0;
				}
			}
			if(flag==1&&f1==0)	
			{
				o<<"X won\n";
				f2=0;f3=0;f=0;f1=1;
				break;
			}
			if(f==1&&f1==0)	
			{
				o<<"O won\n";
				f2=0;f3=0;flag=0;f1=1;
				break;
			}			
		}
		if(f2==1&&f1==0) 
		{
			o<<"X won\n";
			f1=1;
		}
		if(f3==1&&f1==0) 
		{
			o<<"O won\n";
			f1=1;
		}
		f3=1;f2=1;f4=0;//o<<f1<<endl;
		for(j=0;j<4;j++)
		{
			flag=1;f=1;
			for(i=0;i<4;i++)
			{
				if(str[i][j]=='.') f4=1;
				if(str[i][j]=='X'||str[i][j]=='T')
					{
						flag*=1;
					}
				else flag*=0;
				//o<<str[i][j]<<" ";
				if(str[i][j]=='O'||str[i][j]=='T')
					f*=1;
				else f*=0;
				if(i==j)
				{
					if(str[i][j]=='X'||str[i][j]=='T')
						f2*=1;
					else f2*=0;
					if(str[i][j]=='O'||str[i][j]=='T')
						f3*=1;
					else f3*=0;
				}
			}
			if(flag==1&&f1==0)	
			{
				o<<"X won\n";
				f2=0;f3=0;f=0;f1=1;
				break;
			}
			if(f==1&&f1==0)	
			{
				o<<"O won\n";f1=1;
				f2=0;f3=0;flag=0;break;
			}
		}
		if(f2==1&&f1==0) 
		{
			o<<"X won\n";
			f1=1;
		}
		if(f3==1&&f1==0) 
		{
			o<<"O won\n";
			f1=1;
		}
		if(f1==0&&f4==1) o<<"Game has not completed\n";
		if(f1==0&&f4==0) o<<"Draw\n";
		
	}
	p.close();
	o.close();
	return 0;
}
