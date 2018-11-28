//#define LOCAL
#include<iostream>
using namespace std; 
int main()
{
	#ifdef LOCAL
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	#endif
	int t;
	int n[4][4];
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int g1,g2,j,k;
		int tmp1[4],tmp2[4];
		cin>>g1;
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
				cin>>n[j][k];
		for(j=0;j<4;j++)tmp1[j]=n[g1-1][j];
		cin>>g2;
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
				cin>>n[j][k];
		for(j=0;j<4;j++)tmp2[j]=n[g2-1][j];
		int count=0,num;
		for(j=0;j<4;j++)
			for( k=0;k<4;k++)
				if(tmp1[j]==tmp2[k]){count++;num=tmp1[j];}
		if(count==0)cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		else if(count==1)cout<<"Case #"<<i+1<<": "<<num<<endl;
		else cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
	}
	return 0;
}
