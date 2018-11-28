#include<iostream>
#include<conio.h>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Out.out","w",stdout);
	static long T, a, b, a1, a2, x, ans, comp1[4], comp2[4], occ, l , m;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		scanf("%d",&a1);
		for(int a=0;a<4;a++)
		{
			for(int b=0;b<4;b++)
			{
				scanf("%d",&x);
				if(a+1==a1)
					comp1[b]=x;
			}
		}
		scanf("%d",&a2);
		for(int a=0;a<4;a++)
		{
			for(int b=0;b<4;b++)
			{
				scanf("%d",&x);
				if(a+1==a2)
					comp2[b]=x;
			}
		}
		sort(comp1,comp1+4);
		sort(comp2,comp2+4);
		occ=0; l=0; m=0;
		while(l<4 && m<4)
		{
			if(comp1[l]<comp2[m])
				l++;
			else if(comp2[m]<comp1[l])
				m++;
			else
			{
				ans=comp1[l];
				l++;
				m++;
				occ++;
			}
			
		}
		if(occ>1)
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		else if(occ==0)
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
