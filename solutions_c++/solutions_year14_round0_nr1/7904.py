#include<iostream>
using namespace std;

int main()
{
	int n, i, row1, row2, nos[4], j, k, inp[4], count, res;

	cin>>n;

	for(i = 1; i <= n; i++)
	{
		cin>>row1;

		for(j = 1; j <= 4; j++)
		{
			cin>>inp[0]>>inp[1]>>inp[2]>>inp[3];
			if(j == row1)
			{
				nos[0] = inp[0];
				nos[1] = inp[1];
				nos[2] = inp[2];
				nos[3] = inp[3];
			}
		}

		cin>>row2;

		count = 0;
		res = 0;
		for(j = 1; j <= 4; j++)
		{
			cin>>inp[0]>>inp[1]>>inp[2]>>inp[3];
			if(j == row2)
			{
				for(k = 0; k < 4; k ++)
				{
					if(inp[k] == nos[0])
					{
						count++;
						res = nos[0];
					}
					if(inp[k] == nos[1])
					{
						count++;
						res = nos[1];
					}
					if(inp[k] == nos[2])
					{
						count++;
						res = nos[2];
					}
					if(inp[k] == nos[3])
					{
						count++;
						res = nos[3];
					}
				}
			}
		}

		if(count == 1)
			cout<<"Case #"<<i<<": "<<res<<endl;
		else if(count == 0)
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
	}
}
