#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

struct pod
{
	int x;
	int y;
} podd;


bool check_finishd(bool b[102][102],int x1,int y1)
{
	for (int i1 = 1;i1<=x1;i1++)
		for (int i2 = 1;i2<=y1;i2++)
			if (b[i1][i2] == false) return false;
	return true;
}

int main()
{
	bool built[102][102];
	int height[102][102];
	int n,x,y;
	int min_height = 101;
	vector<pod> mins;
	bool unbl = false;
	ifstream ist("input2.in");
	ofstream ost("output2.out");

	ist>>n;
	for (int i = 1;i<=n;i++)
	{
		memset(built,false,sizeof(built));
		memset(height,0,sizeof(height));
		mins.clear();
		ist >>x>>y;
		for (int i1 = 1;i1<=x;i1++)
			for (int i2 = 1;i2<=y;i2++)
				ist >> height[i1][i2];
		unbl = false;
		min_height = 101;
		while (!check_finishd(built,x,y))
		{
			min_height = 101;
		for (int i1 = 1;i1<=x;i1++)
			for (int i2 = 1;i2<=y;i2++)
			{
				if ((height[i1][i2]<min_height)&&(!built[i1][i2])) {min_height = height[i1][i2];mins.clear();
																	pod t2;
																	t2.x = i1;
																	t2.y = i2;
																	mins.push_back(t2);}
				if ((height[i1][i2]==min_height)&&(!built[i1][i2])) {
																	pod t2;
																	t2.x = i1;
																	t2.y = i2;
																	mins.push_back(t2);}
			}

		for (int i1 = 0;i1<mins.size();i1++)
		{

			built[mins[i1].x][mins[i1].y] = true;
		}

		//Check Valid
		for (int i1 = 0;i1<mins.size();i1++)
		{
			bool validd1 = true;
			bool validd2 = true;
			for (int i2 = 1;i2<=x;i2++)
			{
				if (!built[i2][mins[i1].y]) validd1 = false;
			}
			for (int i2 = 1;i2<=y;i2++)
			{
				if (!built[mins[i1].x][i2]) validd2 = false;
			}
			if ((!validd1)&&(!validd2)&&(!unbl)) {ost<<"Case #"<<i<<": NO"<<endl;unbl = true;}
		}
		}

		if (!unbl) ost<<"Case #"<<i<<": YES"<<endl;

	}

	//system("pause");
}