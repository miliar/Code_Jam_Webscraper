#include<iostream>
using namespace std;
int main()
{
	int cases;
	int ans1,ans2;
	int deck1[4][4], deck2[4][4];
	cin >> cases;
	int c = 0;
	while(c < cases)
	{
	cin >> ans1;
	int i,j;
	for(i = 0; i<4;i++)
	{
		for(j =0; j<4;j++)
		{
			cin >> deck1[i][j];
		}
	}
	cin>>ans2;
	for(i = 0;i<4;i++)
	{
		for(j = 0;j<4;j++)
		{
			cin >> deck2[i][j];
		}
	}
	int lst1[4] , lst2[4];
	for(i = 0;i<4;i++)
	{
		lst1[i] = deck1[ans1-1][i];
		lst2[i] = deck2[ans2-1][i];
	}
	int count = 0;
	int check = 0;
	int ans;
	for(i = 0;i<4;i++)
	{
		for(j =0;j<4;j++)
		{
			if(lst1[i] == lst2[j])
			{
				ans = lst1[i];
				check = 1;
				if (count== 0)
					count +=1;
				else
					check = 2;
			}
		}
	}
	if(check == 1)
		cout<<"Case #"<<c+1<<": "<<ans<<"\n";
	else if(check == 0)
		cout<<"Case #"<<c+1<<": Volunteer cheated!"<<"\n";
	else if(check == 2)
		cout<<"Case #"<<c+1<<": Bad magician!"<<"\n"; 
	c += 1;
	}
	return 0;
}
	
