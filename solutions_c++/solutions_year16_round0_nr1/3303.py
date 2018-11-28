#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int t,j,i;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		int n,p=0,q=0,m=0,a,b,cnt0=0,cnt1=0,cnt2=0,cnt3=0,cnt4=0,cnt5=0,cnt6=0,cnt7=0,cnt8=0,cnt9=0;
		cin>>n;
		m=n;
		if(n==0)
		cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
		else{
		
		for(i=1;;i++)
		{
			p=m;
			//cout<<p<<endl;
			while(p>0)
			{
				q=p%10;
				if(q==0)
				cnt0++;
			    if(q==1)
				cnt1++;
				 if(q==2)
				cnt2++;
				 if(q==3)
				cnt3++;
				 if(q==4)
				cnt4++;
				 if(q==5)
				cnt5++;
				 if(q==6)
				cnt6++;
				 if(q==7)
				cnt7++;
				 if(q==8)
				cnt8++;
				 if(q==9)
				cnt9++;
				p=p/10;
				//cout<<p<<endl;
			}
			if(cnt0>=1&&cnt1>=1&&cnt2>=1&&cnt3>=1&&cnt4>=1&&cnt5>=1&&cnt6>=1&&cnt7>=1&&cnt8>=1&&cnt9>=1)
			{cout<<"Case #"<<j<<": "<<m<<endl;break;}
			else
			m=n*(i+1);
		}
		}
	}
}

