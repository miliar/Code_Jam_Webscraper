#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;
int inp[4][4][2];
int first,second,ans=-1;
bool flag[17][3];
int main()
{
	int t,tcase;
	cin>>t;
	for(tcase=1;tcase<=t;tcase++)
	{
		memset(flag,0,sizeof(flag));
		cin>>first;
		for(int i=0;i<4;i++)	
			for(int j=0;j<4;j++)
				cin>>inp[i][j][0];
		for(int i=0;i<4;i++)
			flag[inp[first-1][i][0]][0] = true;
		
		cin>>second;
		for(int i=0;i<4;i++)	
			for(int j=0;j<4;j++)
				cin>>inp[i][j][1];
		for(int i=0;i<4;i++)
			flag[inp[second-1][i][1]][1] = true;
		int prev=-1,count=0;
		for(int i=0;i<17;i++)
		{
			flag[i][2] = flag[i][0] & flag[i][1];
			if(flag[i][2])
			{
				count++;
				prev = i;	
			}
		}
		if(count==0)cout<<"Case #"<<tcase<<": Volunteer cheated!\n";
		else if(count>1)cout<<"Case #"<<tcase<<": Bad magician!\n";
		else cout<<"Case #"<<tcase<<": "<<prev<<"\n";
	}	
	return 0;
}
