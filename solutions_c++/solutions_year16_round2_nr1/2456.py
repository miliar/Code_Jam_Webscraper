#include<bits/stdc++.h>
using namespace std;
int main()
{
	char s[2000+5];
	int t,i,l,j,k;
	ifstream infile("input.txt");
	ofstream myfile("output.txt");
	infile>>t;
	for(k=1;k<=t;k++)
	{
		infile>>s;
		l=strlen(s);
		int a[26]={0};
		for(i=0;i<l;i++)
		{
			a[s[i]-65]++;
		}
		int b[10]={0};
		if(a[25]!=0)
		{
			b[0]=a[25];
			a[4]-=a[25];
			a[17]-=a[25];
			a[14]-=a[25];
			a[25]=0;
		}
		//cout<<a[14]<<endl;
		if(a[23]!=0)
		{
			b[6]=a[23];
			a[18]-=a[23];
			a[8]-=a[23];
			a[23]=0;
		}
		if(a[6]!=0)
		{
			b[8]=a[6];
			a[4]-=a[6];
			a[8]-=a[6];
			a[7]-=a[6];
			a[19]-=a[6];
			a[6]=0;
		}
		if(a[18]!=0)
		{
			b[7]=a[18];
			a[4]-=2*a[18];
			a[21]-=a[18];
			a[13]-=a[18];
			a[18]=0;
		}
		if(a[22]!=0)
		{
			b[2]=a[22];
			a[19]-=a[22];
			a[14]-=a[22];
			a[22]=0;
		}
		if(a[20]!=0)
		{
			b[4]=a[20];
			a[5]-=a[20];
			a[14]-=a[20];
			a[17]-=a[20];
		}
		if(a[5]!=0)
		{
			b[5]=a[5];
			a[4]-=a[5];
			a[21]-=a[5];
			a[8]-=a[5];
			a[5]=0;
		}
		
		if(a[14]!=0)
		{
			b[1]=a[14];
			a[4]-=a[14];
			a[13]-=a[14];
			a[14]=0;
		}
		if(a[7]!=0)
		{
			b[3]=a[7];
			a[19]-=a[7];
			a[17]-=a[7];
			a[4]-=a[7]*2;
			a[7]-=0;
		}
		if(a[8]!=0)
		{
			b[9]=a[8];
			a[13]-=2*a[8];
			a[4]-=a[8];
			a[8]=0;
		}
		myfile<<"Case #"<<k<<": ";
	for(i=0;i<10;i++)
	{
		for(j=0;j<b[i];j++)
		{
			myfile<<i;
		}
	}
	myfile<<endl;
}
}
