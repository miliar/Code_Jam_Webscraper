#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	freopen("sample.txt", "r", stdin);
	freopen("result.txt", "w", stdout);

	int magic1[4][4], magic2[4][4];
	int T;
	cin>>T;
	for(int i = 1; i <= T; ++i)
	{
		int first,second;
		cin>>first;
		for(int j = 0; j < 4; ++j)
			for(int k = 0; k < 4; ++k)
				cin>>magic1[j][k];
		cin>>second;
		for(int j = 0; j < 4; ++j)
			for(int k = 0; k < 4; ++k)
				cin>>magic2[j][k];
		int count = 0, col = -1;
		for(int j = 0; j < 4; ++j)
		{
			for(int k = 0; k < 4; ++k)
			{
				if(magic2[second-1][k] == magic1[first-1][j])
				{
					count++;
					if(count==1)
					{
						col = j;
					}
					break;
				}
			}
			if(count > 1)
				break;
		}
		if(count == 1)
		{
			cout<<"Case #"<<i<<": "<<magic1[first-1][col]<<endl;
		}
		else if(count>1)
		{
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}

	}
	return 0;
}

