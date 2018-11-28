/* 
 * Author: Mohamad Shawkey
 * Created on April 12, 2014, 2:59 PM
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;


int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int row1,row2;
		int grid1[4][4],grid2[4][4];
		cin>>row1;
		row1--;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++) cin>>grid1[j][k];
		cin>>row2; row2--;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++) cin>>grid2[j][k];
		int res[4];
		for(int j=0;j<4;j++) res[j]=0;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++) 
				if(grid1[row1][k]==grid2[row2][j]) res[k]++;
		
		int cnt=0;
		int val;
		for(int j=0;j<4;j++) if(res[j]>0) {cnt++; val=grid1[row1][j];}
		cout<<"Case #"<<i<<": ";
		if(cnt==0) cout<<"Volunteer cheated!\n";
		else if(cnt>1) cout<<"Bad magician!\n";
		else cout<< val<<endl;
	}
	return 0;
}

