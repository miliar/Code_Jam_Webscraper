#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
using namespace std;
int main()
{
	freopen("Ain.in","r",stdin);
	freopen("Aout.txt","w",stdout);
	int T;
	int row[2],mp[2][4][4],pos[20];
	vector<int > ans;
	cin>>T;
	for(int x=0;x<T;x++)
	{
		for(int i=0;i<2;i++)
		{
			cin>>row[i];
			row[i]--;
			for(int j=0;j<4;j++)
				for(int k=0;k<4;k++)
					cin>>mp[i][j][k];
		}
		memset(pos,0,sizeof(pos));
		for(int i=0;i<2;i++)
			for(int k=0;k<4;k++)
				pos[ mp[i][row[i]][k] ]++;
		ans.clear();
		for(int i=0;i<20;i++)
			if(pos[i]==2)
				ans.push_back(i);
		cout<<"Case #"<<x+1<<": ";
		if(ans.size()==0)
			cout<<"Volunteer cheated!\n";
		else if(ans.size()==1)
			cout<<ans[0]<<endl;
		else
			cout<<"Bad magician!\n";
	}
	return 0;
}
