
#include <iostream>
#include <vector>
using namespace std;
//Nikhil Kulkarni, India.
class Cards
{
	int **cards;
	int test_cases,row1,row2;
	int choice1,choice2;
	int flag;
public:
	vector<int> result;
	Cards()
	{
		test_cases=0;row1=0,row2=0;
		choice1=choice2=0;
		flag=-3;
		cards=new int*[4];
		for(int i=0;i<4;i++)
		{
			cards[i]=new int[4];
		}
	}

	int get_test_cases()
	{
		cin>>test_cases;
		return test_cases;
	}
	void get_row1()
	{
		int test;
		cin>>test;row1=test-1;
	}
	void get_row2()
		{
			int test;
			cin>>test;row2=test-1;
		}

	void get_cards();
	void print();
	void process();
};

void Cards::get_cards()
{
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			cin>>cards[i][j];
}

void Cards::print()
{
	for(int i=0;i<4;i++)
		{for(int j=0;j<4;j++)
			{cout<<cards[i][j]<<" ";}
		cout<<endl;
		}
}

void Cards::process()
{
	flag=-3;
	int temp3;
	get_row1();
	get_cards();
	int temp1[4],temp2[4];
	for(int i=0;i<4;i++)
	{
			temp1[i]=cards[row1][i];
	}
	get_row2();
	get_cards();;
	for(int i=0;i<4;i++)
	{
			temp2[i]=cards[row2][i];
	}
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(temp1[i]==temp2[j])
				{flag++;
				temp3=temp1[i];
				}
		}
	if(flag==-2)
	result.push_back(temp3);
	else if(flag==-3)
		result.push_back(0);
	else if(flag>-2)
		result.push_back(-10);


}

int main()
{
	Cards c1;
	int test=c1.get_test_cases();
	for(int i=0;i<test;i++)
	c1.process();
	cout<<"\n";
	for(int i=0;i<test;i++)
	{
		if(c1.result[i]==-10)
			cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
		else if(c1.result[i]==0)
			cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<i+1<<": "<<c1.result[i]<<endl;
	}
	return 0;
}
