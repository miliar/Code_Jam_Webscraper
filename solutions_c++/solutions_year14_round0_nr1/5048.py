#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string.h>
#include<map>
#include<cmath>
#include<iomanip>
#include<vector>
#include<queue>
using namespace std;
typedef long long LL;



int main(){
	int t;
	scanf("%d",&t);
	int z=t;
	while(t--)
	{
		int c1,c2;
		int n[4][4],a[4][4];
		scanf("%d",&c1);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&n[i][j]);
			}
		}
		scanf("%d",&c2);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		cout<<"Case #"<<z-t<<": "; 
		int f=0,fl=0,ans;
		for(int i=0;i<4;i++)
		{
			if(fl==0){
			for(int j=0;j<4;j++)
			{
				
				if(n[c1-1][i]==a[c2-1][j]&&f==0)
				{
				
					f=1;
					ans=n[c1-1][i];
				}
				else if(n[c1-1][i]==a[c2-1][j]&&f==1)
				{
					fl=1;
					
					cout<<"Bad magician!"<<endl;
					break;
				}
			}
			}
		}
		if(f==1&&fl==0)
		{
			cout<<ans<<endl;
		}
		else if(fl==0&&f==0)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
	}
	   
    return 0;
}
