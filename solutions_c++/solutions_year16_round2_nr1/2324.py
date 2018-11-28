#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	string s;
	int Case=1;
	while(t--)
	{
		cin>>s;
		vector<int>a(26,0);
		vector<int>b(10,0);
		for(int i=0;i<s.length();i++)
			{
				a[s[i]-'A']++;
			}
		if(a['Z'-'A']!=0)
		{
			a['E'-'A']-=a['Z'-'A'];
			a['R'-'A']-=a['Z'-'A'];
			a['O'-'A']-=a['Z'-'A'];
			b[0]=a['Z'-'A'];
			a['Z'-'A']=0;
		}
		if(a['W'-'A']!=0)
		{
			a['T'-'A']-=a['W'-'A'];
			a['O'-'A']-=a['W'-'A'];
			b[2]=a['W'-'A'];
			a['W'-'A']=0;	
		}
		if(a['U'-'A']!=0)
		{
			a['F'-'A']-=a['U'-'A'];
			a['O'-'A']-=a['U'-'A'];
			a['R'-'A']-=a['U'-'A'];
			b[4]=a['U'-'A'];
			a['U'-'A']=0;	
		}
		if(a['F'-'A']!=0)
		{
			a['I'-'A']-=a['F'-'A'];
			a['V'-'A']-=a['F'-'A'];
			a['E'-'A']-=a['F'-'A'];
			b[5]=a['F'-'A'];
			a['F'-'A']=0;	
		}
		if(a['X'-'A']!=0)
		{
			a['I'-'A']-=a['X'-'A'];
			a['S'-'A']-=a['X'-'A'];
			b[6]=a['X'-'A'];
			a['X'-'A']=0;	
		}
		if(a['V'-'A']!=0)
		{
			a['S'-'A']-=a['V'-'A'];
			a['E'-'A']-=(2*a['V'-'A']);
			a['N'-'A']-=a['V'-'A'];
			b[7]=a['V'-'A'];
			a['V'-'A']=0;	
		}
		if(a['G'-'A']!=0)
		{
			a['E'-'A']-=a['G'-'A'];
			a['I'-'A']-=a['G'-'A'];
			a['H'-'A']-=a['G'-'A'];
			a['T'-'A']-=a['G'-'A'];
			b[8]=a['G'-'A'];
			a['G'-'A']=0;	
		}
		if(a['O'-'A']!=0)
		{
			a['N'-'A']-=a['O'-'A'];
			a['E'-'A']-=a['O'-'A'];
			b[1]=a['O'-'A'];
			a['O'-'A']=0;	
		}
		if(a['T'-'A']!=0)
		{
			a['H'-'A']-=a['T'-'A'];
			a['R'-'A']-=a['T'-'A'];
			a['E'-'A']-=(2*a['T'-'A']);
			b[3]=a['T'-'A'];
			a['T'-'A']=0;	
		}
		if(a['N'-'A']!=0)
		{
			a['I'-'A']-=(a['N'-'A']/2);
			a['E'-'A']-=(a['N'-'A']/2);
			b[9]=(a['N'-'A']/2);
			a['N'-'A']=0;	
		}
		
		cout<<"Case #"<<Case<<": ";
		for(int i=0;i<10;i++)
			{
				for(int j=b[i];j>0;j--)
				{
					cout<<i;
				}
			}
		cout<<endl;
		Case++;
	}
	return 0;
}
