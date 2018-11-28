#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;

int t;
int response;
int cards[5][5];
int possible[5];

int main()
{
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	cin>>t;
	int files;
	for(files=1;files<=t;files++)
	{
		cin>>response;
		int i,j;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				cin>>cards[i][j];
		
		for(i=1;i<=4;i++)
			possible[i] = cards[response][i];
		
		cin>>response;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				cin>>cards[i][j];
		
		int ans=0;
		bool repeat = false;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(possible[i] == cards[response][j])
				{
					if(ans==0)
						ans = possible[i];
					else
					{
						repeat=true;
						break;
					}
				}
			}
		}	
		
		if(ans==0)
			cout<<"Case #"<<files<<": Volunteer cheated!"<<endl;
		else if(repeat)
			cout<<"Case #"<<files<<": Bad magician!"<<endl;
		else
			cout<<"Case #"<<files<<": "<<ans<<endl;
	}
	//system("pause");
	return 0;
}
