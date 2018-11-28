#include<iostream>
#include<vector>
using namespace std;
int main()
{
	vector < vector <int> > arrange1,arrange2;
	int testcase,c=1;
	cin>>testcase;
	while(testcase!=0)
	{
		int ans1,ans2,count=0,column;
		testcase--;
		count=0;
		column=0;
		arrange1.clear();
		arrange2.clear();
		cin>>ans1;
		ans1--;
		for(int counter1=0;counter1<4;counter1++)
		{
			vector <int> row;
			for(int counter2=0;counter2<4;counter2++)
			{
				int temp;
				cin>>temp;
				row.push_back(temp);
			}
			arrange1.push_back(row);
		}	
		cin>>ans2;
		ans2--;
		for(int counter1=0;counter1<4;counter1++)
		{
			vector <int> row;
			for(int counter2=0;counter2<4;counter2++)
			{
				int temp;
				cin>>temp;
				row.push_back(temp);
			}
			arrange2.push_back(row);
		}
		for(int counter1=0;counter1<4;counter1++)
		{
			for(int counter2=0;counter2<4;counter2++)
			{
				if(arrange1[ans1][counter1]==arrange2[ans2][counter2])
				{
					count++;
					column=counter1;
				}
			}
		}
		cout<<"Case #"<<c<<": ";
		if(count==0)
		{
			cout<<"Volunteer cheated!";
		}
		else if(count==1)
		{
			cout<<arrange1[ans1][column];
		}
		else if(count>1)
		{
			cout<<"Bad magician!";
		}
		cout<<"\n";
		c++;
	}
	return 0;
}
