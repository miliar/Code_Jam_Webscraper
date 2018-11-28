#include <fstream>

#define MN 4

using namespace std;

typedef struct{
	int row;
	int m[MN][MN];
}cards;

cards first;
cards second;

ifstream cin;
ofstream cout;

void readACard(cards &c)
{
	cin>>c.row;
	for(int i=0; i<MN; ++i)
	{
		for(int j=0; j<MN; ++j)
		{
			cin>>c.m[i][j];
		}
	}
}

int getRes(cards &first, cards &second)
{
	bool flag[MN*MN+1]={false};
	int count = 0;
	int res = -1;
	int row = first.row-1;
	for(int i=0; i<MN; ++i)
	{
		flag[first.m[row][i]] = true;
	}

	row = second.row-1;
	for(int i=0; i<MN; ++i)
	{
		if(true == flag[second.m[row][i]])
		{
			count++;
			res = second.m[row][i];
		}
	}
	if(count == 0)
	{
		return -1;
	}
	else if(count == 1)
	{
		return res;
	}
	else
	{
		return MN*MN+1;
	}
}

void search(int num)
{

	readACard(first);
	readACard(second);
	int res = getRes(first, second);
	if(res<=0)
	{
		cout<<"Case #"<<(num+1)<<": Volunteer cheated!"<<endl;
	}
	else if(res <= MN*MN)
	{
		cout<<"Case #"<<(num+1)<<": "<<res<<endl;
	}
	else
	{
		cout<<"Case #"<<(num+1)<<": Bad magician!"<<endl;
	}
}

int main()
{
	cin.open("A-small-attempt1.in");
	cout.open("A-small-attempt1.out");
	int n;
	cin>>n;
	for(int i=0; i<n; ++i)
	{
		search(i);
	}
	return 0;
}