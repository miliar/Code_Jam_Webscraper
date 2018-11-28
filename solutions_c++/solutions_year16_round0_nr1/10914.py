#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
#include<conio.h>
#include<fstream>
using namespace std;
	int s[100];
	int a0=0, a1=0, a2=0, a3=0, a4=0, a5=0, a6=0, a7=0, a8=0, a9=0;
int func(int);
int main()
{
	getch();
		long test,ret=0;
	long i,sta[10000],stao,k=1;
	long q=1,po[1000];
	long s;
	long kl[100];
ifstream in;
ofstream out;
in.open("A-large(1).in");
out.open("thisisfinla.out");
if(!in)
{
	cerr<<"file not found\n";
	return -1;
}
in>>test;
while(in.eof()==0)
{
	in>>s;
	po[q]=s;
	q++;
}
for(i=1;i<=test;i++)
{
	sta[i]=po[i];
}

	for(i=1;i<=test;i++)
	{
		if(sta[i]==0)
		{
		cout<<"case #"<<i<<": "<<"INSOMNIA\n";
			out<<"case #"<<i<<": "<<"INSOMNIA\n";
		goto exi;
		}
	bk:	stao=sta[i] * k;
		ret=func(stao);
		kl[i]=ret;
		if(ret==0) 
		{
			k++;
			goto bk;
		}
		

	cout<<"case #"<<i<<": "<<ret<<endl;
	out<<"case #"<<i<<": "<<ret<<endl;
	exi: ;
	a0=0; a1=0 ;a2=0 ;a3=0;a4=0;a5=0;a6=0;a7=0;a8=0;a9=0;
	ret=0;
	k=1;
	}
	in.close();
	return 0;
}
int func(int a)
{
	int as=a;
	int i,j,t=0;

	for(i=0;i>=0;i++)
	{
	if(a<10)
	{
		s[i]=a;
		t++;
		goto ex;
	}
		s[i]=a%10;
	a=a/10;
	t++;
	}
	ex:
	for(j=0;j<t;j++)
	{
		if(s[j]==0) a0++;
		else	if(s[j]==1) a1++;
			else	if(s[j]==2) a2++;
				else	if(s[j]==3) a3++;
					else	if(s[j]==4) a4++;
						else	if(s[j]==5) a5++;
							else	if(s[j]==6) a6++;
								else	if(s[j]==7) a7++;
									else	if(s[j]==8) a8++;
										else	if(s[j]==9) a9++;
		
		
	}
	if(a0>=1 && a1>=1 && a2>=1 && a3>=1 && a4>=1 && a5>=1 && a6>=1 && a7>=1 && a8>=1 && a9>=1  )
	{
		return as;
	}
	return 0;
}
