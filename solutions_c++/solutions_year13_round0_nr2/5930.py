// Jai Mata Di
#include<iostream>
#include<vector>
using namespace std;
class Lawn
{
public:
	int rows;
	int columns;
	vector<vector<int > > e;
	vector<vector<int > > c;
	void Input()
	{
		cin>>rows;
//		cout<<rows<<endl;
		cin>>columns;
//		cout<<columns<<endl;
		for(int i=0;i<rows;i++)
		{
			vector<int> v;
			for(int j=0;j<columns;j++)
			{
				int ii;
				cin>>ii;
//				cout<<ii<<endl;
				v.push_back(ii);
			}
			e.push_back(v);
		}
		
		for(int i=0;i<rows;i++)
		{
			vector<int> v;
			for(int j=0;j<columns;j++)
			{
				v.push_back(100);
			}
			c.push_back(v);
		}
		
	}
	void Print()
	{
		cout<<endl;
		for(int i=0;i<rows;i++)
		{
			for(int j=0;j<columns;j++)
			{
				cout<<e[i][j]<<" ";
			}
			cout<<endl;
		}
	}
	void PrintC()
	{
		cout<<endl;
		for(int i=0;i<rows;i++)
		{
			for(int j=0;j<columns;j++)
			{
				cout<<c[i][j]<<" ";
			}
			cout<<endl;
		}
	}

	bool MoeRowWise()
	{
		for(int i=0;i<rows;i++)
		{
			int max = -1;
			for(int j=0;j<columns;j++)
			{
				if(e[i][j] > max)
				{
					max = e[i][j];
				}
			}
//			cout<<"max"<<max<<endl;
			for(int j=0;j<columns;j++)
			{
				if(c[i][j] > max)
					c[i][j] = max;
			}
		}
		return false;
	}
	bool MoeColWise()
	{
		for(int i=0;i<columns;i++)
		{
			int max = -1;
			for(int j=0;j<rows;j++)
			{
				if(e[j][i] > max)
				{
					max = e[j][i];
				}
			}
//			cout<<"max"<<max<<endl;
			for(int j=0;j<rows;j++)
			{
				if(c[j][i] > max)
					c[j][i] = max;
			}
		}
		return false;
	}
	bool CheckIfPossible()
	{
		for(int i=0;i<rows;i++)
		{
			for(int j=0; j<columns;j++)
			{
				if(c[i][j] != e[i][j])
				{
					return false;
				}
			}
		}
		return true;
	}
	void CheckAnswer()
	{
		MoeRowWise();
		MoeColWise();
//		PrintC();
		if(CheckIfPossible())
		{
			cout<<"YES"<<endl;
		}
		else
		{
			cout<<"NO"<<endl;
		}
	}
};
int main()
{
	int noOfTestCases;
	cin>>noOfTestCases;
//	cout<<noOfTestCases<<endl;
	for(int i=1;i<=noOfTestCases;i++)
	{
		Lawn l;
		l.Input();
//		l.Print();
		cout<<"Case #"<<i<<": ";
		l.CheckAnswer();
	}
	return 0;
}
