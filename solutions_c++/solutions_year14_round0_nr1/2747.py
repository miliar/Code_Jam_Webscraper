#include <fstream>

using namespace std;


ifstream cin;
ofstream cout;


void solve(int k)
{
	int a[4][4];
	int b[4][4];
	int flag[17]={0};
	int num1,num2,result;
	int count=0;
	cin>>num1;
	num1--;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>a[i][j];
		}
	}
	for(int i=0;i<4;i++)
		flag[a[num1][i]]=1;

	cin>>num2;
	num2--;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>b[i][j];
		}
	}
	for(int i=0;i<4;i++)
	{
		if(flag[b[num2][i]])
		{
			count++;
			result=b[num2][i];
		}
	}

	if(count==0)
	{
		cout<<"Case #"<<(k+1)<<": Volunteer cheated!"<<endl;
	}
	else if(count==1)
	{
		cout<<"Case #"<<(k+1)<<": "<<result<<endl;
	}
	else
	{
		cout<<"Case #"<<(k+1)<<": Bad magician!"<<endl;
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
		solve(i);
	}
	return 0;
}