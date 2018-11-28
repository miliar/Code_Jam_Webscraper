#include <iostream>

int array1[4][4];
int array2[4][4];

using namespace std;


void work(int x, int y)
{
	int flag[17];

	for (int i = 0; i < 17; i++)
		flag[i] = 0;

	for (int i = 0; i < 4; i++)
	{
		flag[array1[x-1][i]]++;
	}

	
	for (int i = 0; i < 4; i++)
	{
		flag[array2[y-1][i]]++;
	}

	int cnt = 0;
	int num;

	for (int i = 1; i < 17; i++)
	{
		if (flag[i] >= 2)
		{
			cnt++;
			num = i;
		}
	}

	if (cnt >= 2)
	{
		cout<<"Bad magician!"<<endl;
	}
	else if (cnt == 0)
	{
		cout<<"Volunteer cheated!"<<endl;
	}
	else
	{
		cout<<num<<endl;
	}
	return;
}


int main()
{
	int N;

	cin>>N;

	for (int line = 1; line <= N; line++)
	{
		int x, y;
		cin>>x;
		
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin>>array1[i][j];

		cin>>y;

		
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin>>array2[i][j];

		cout<<"Case #"<<line<<": ";

		work(x, y);
	}

	return 0;
}

