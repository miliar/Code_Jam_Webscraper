#include <iostream>

using namespace std;

int main()
{
	int T=0;
	cin >> T;
	
	for (int i=1;i<=T;++i)
	{
		int ans1,ans2;
		int a[4][4];
		int b[4][4];
		
		int c[17] = {0};
		
		cin >> ans1;
		for (int j=0;j<4;++j)
			for (int k=0;k<4;++k)
				cin >> a[j][k];
		
		for (int k=0;k<4;++k)
		{
			c[a[ans1-1][k]] = 1;
		}
		
		cin >> ans2;
		for (int j=0;j<4;++j)
			for (int k=0;k<4;++k)
				cin >> b[j][k];
		
		int rst = 0;
		int cnt = 0;
		
		for (int k=0;k<4;++k)
		{
			if (c[b[ans2-1][k]] == 1)
			{
				++cnt;
				rst = b[ans2-1][k];		
			}
		}
		
		if (cnt==1) cout <<"Case #"<<i<<": "<<rst<<endl;
		if (cnt==0) cout <<"Case #"<<i<<": Volunteer cheated!"<<endl;
		if (cnt>1) cout <<"Case #"<<i<<": Bad magician!"<<endl;
	}
	
	return 0;
}