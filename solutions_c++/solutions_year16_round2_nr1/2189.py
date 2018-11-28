#include<bits/stdc++.h>
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
using namespace std;
int main()
{
	f_in("large1.in");
	f_out("large1out.txt")
	int t,i,j,k=0;
	cin>>t;
	getchar();
	string s;
	while(t--)
	{
		k++;
		cin>>s;
		int hash[267]={0};
		int n[20]={0};
		for(i=0;i<s.length();i++)
		{
			hash[s[i]]++;
		}
		if(hash['X']!=0)
		{
			n[6]+=hash['X'];
			hash['S']-=hash['X'];
			hash['I']-=hash['I'];
			hash['X']=0;
		}
		if(hash['Z']!=0)
		{
			n[0]+=hash['Z'];
			hash['E']-=hash['Z'];
			hash['R']-=hash['Z'];
			hash['O']-=hash['Z'];
			hash['Z']=0;
		}
		if(hash['W']!=0)
		{
			n[2]=hash['W'];
			hash['O']-=hash['W'];
			hash['T']-=hash['W'];
			hash['W']=0;
		}
		if(hash['U']!=0)
		{
			
			n[4]=hash['U'];
			hash['F']-=hash['U'];
			hash['O']-=hash['U'];
			hash['R']-=hash['U'];
			hash['U']=0;
		}
		if(hash['F']!=0)
		{
			//cout<<"5"<<endl;
			n[5]=hash['F'];
			hash['I']-=hash['F'];
			hash['V']-=hash['F'];
			hash['E']-=hash['F'];
			hash['F']=0;
		}
		if(hash['V']!=0)
		{
			//cout<<"7"<<endl;
			n[7]=hash['V'];
			hash['S']-=hash['V'];
			hash['E']-=2*hash['V'];
			hash['N']-=hash['V'];
			hash['V']=0;
		}
		if(hash['O']!=0)
		{
			//cout<<"1"<<endl;
			n[1]=hash['O'];
			hash['E']-=hash['O'];
			hash['N']-=hash['O'];
			hash['O']=0;
		}
		if(hash['N']!=0)
		{
			//cout<<"9"<<endl;
			n[9]=hash['N']/2;
			hash['I']-=hash['N']/2;
			hash['E']-=hash['N']/2;
			hash['N']=0;
		}
		if(hash['G']!=0)
		{
			//cout<<"8"<<endl;
			n[8]=hash['G'];
			hash['E']-=hash['G'];
			hash['I']-=hash['G'];
			hash['H']-=hash['G'];
			hash['T']-=hash['G'];
			hash['G']=0;
		}
		if(hash['T']!=0)
		{
			n[3]=hash['T'];
		}
		cout<<"CASE #"<<k<<": ";
		for(i=0;i<=9;i++)
		{
			//cout<<hash[i]<<endl;
			for(j=0;j<n[i];j++)
			{
				cout<<i;
			}
		}
		cout<<endl;
	}
	return 0;
}
