#include <iostream> 
#include <vector> 
#include <string> 
#include <algorithm> 
#include <regex>

using namespace std;

static auto solve = []( )
{
	int n; cin>>n;
	int mtrx1[4][4];

	for (int i=0; i<4; ++i)
		for (int j=0; j<4; ++j)
			cin>>mtrx1[i][j];

	int row1[4];
	for (int i=0; i<4; ++i)
		row1[i]=mtrx1[n-1][i];

	int m; cin>>m;
	int mtrx2[4][4];
	for (int i=0; i<4; ++i)
		for (int j=0; j<4; ++j)
			cin>>mtrx2[i][j];

	int row2[4];
	for (int i=0; i<4; ++i)
		row2[i]=mtrx2[m-1][i];

	bool flag=false;
	int	same_cnt=0, same=0;
	for (int i=0; i<4; ++i)
	{
		for(int j=0; j<4; ++j)
		{
			if(row1[i]==row2[j])
			{
				++same_cnt;
				same=row1[i];
			}
		}
	}

	string str;
	if (same_cnt==1)
	{
		str = to_string(same);
	}
	else if (same_cnt==0)
	{
		str = "Volunteer cheated!";
	}
	else
	{
		str ="Bad magician!";
	}
	
	return str;
};

void main()
{
	int T;	cin>>T;

	for (int case_no=1; case_no<=T; ++case_no )
	{
		cout<<"Case #"<<case_no<<": "<<solve( )<<endl;
	}
}
