#include<iostream>
#define size 4
using namespace std;

class trick
{
	int a1,a2,first[size][size],second[size][size];
public:
	void getinfo()
	{
		cin>>a1;
		for(int i=0;i<size;i++)
		{
			for(int j=0;j<size;j++)
				cin>>first[i][j];
		}
		cin>>a2;
		for(int i=0;i<size;i++)
		{
			for(int j=0;j<size;j++)
				cin>>second[i][j];
		}
	}
	int getresult()
	{
		int row1[size],row2[size],result,count=0;
		for(int i=0;i<size;i++)
		{
			row1[i] = first[a1 - 1][i];
			row2[i] = second[a2 - 1][i];
		}
		for(int i=0;i<size;i++)
		{
			for(int j=0;j<size;j++)
			{
				if(row1[i] == row2[j])
				{
					result = row1[i];
					count++;
				}
			}
		}
		if(count == 1)
			return result;
		else if(count == 0)
			return -1;
		else return 0;
	}
};
int main()
{
	trick t;
	int n;
	cin>>n;
	int result[n];
	for(int i=0;i<n;i++)
	{
		t.getinfo();
		result[i] = t.getresult();
	}
	for(int i=0;i<n;i++)
	{
		if(result[i] > 0)
			cout<<"Case #"<<i+1<<": "<<result[i];
		else if(result[i] == 0)
			cout<<"Case #"<<i+1<<": Bad magician!";
		else
			cout<<"Case #"<<i+1<<": Volunteer cheated!";
		cout<<endl;
	}
	return 0;
}