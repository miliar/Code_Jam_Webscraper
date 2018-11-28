#include <iostream>
using namespace std;

int main()
{
int testcases;
int no;
int temp;
int first[4];
int second[4];
int answer;
cin >> testcases;
for (int i=1;i<=testcases;i++)
{
	cin >> no;
	for (int j=0;j<4;j++)
	{
		for (int k=0;k<4;k++)
		{
		cin >> temp;
		if (j==no-1) first[k]=temp;
		} 
	}
	 cin >> no;
        for (int j=0;j<4;j++)
        {
                for (int k=0;k<4;k++)
                {
                cin >> temp;
                if (j==no-1) second[k]=temp;
                }
        }
	int flag=0;
	for (int j=0;j<4;j++)
        {
                for (int k=0;k<4;k++)
                {
        	        if (first[j]==second[k]) 
			{
				answer=first[j];
				flag++;					

			}
                }
        }
	if (flag==1) cout <<"Case #"<< i<<": "<< answer<<endl;
	if (flag==0) cout <<"Case #"<< i<<": "<<"Volunteer cheated!\n";
	if (flag>1)  cout <<"Case #"<< i<<": "<<"Bad magician!\n";
}

return 0;
}
