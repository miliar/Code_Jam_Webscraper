#include <iostream>
using namespace std;

int main() {
	int a[4][4],b[4][4],r1,r2,t,h,c,i,k,m;
	cin>>t;
	h=t;
	while(t--)
	{
		cin>>r1;r1--;
		for(i=0;i<4;i++)for(k=0;k<4;k++)cin>>a[i][k];
		cin>>r2;r2--;
		for(i=0;i<4;i++)for(k=0;k<4;k++)cin>>b[i][k];
		m=0;
		for(i=0;i<4;i++)
		{
			for(k=0;k<4;k++)
			{
				if(a[r1][i]==b[r2][k]){
				m++;
				c=a[r1][i];}
			}
		}
		if(m>1)cout<<"Case #"<<(h-t)<<": Bad Magician!\n";
		else if(m==0)cout<<"Case #"<<(h-t)<<": Volunteer Cheated!\n";
		else if(m==1)cout<<"Case #"<<(h-t)<<": "<<c<<"\n";
		}
	return 0;
}
