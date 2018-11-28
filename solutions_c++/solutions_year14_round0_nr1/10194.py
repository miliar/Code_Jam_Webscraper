#include <iostream>
using namespace std;

int main()
{
	
	int t,i,a1,a2,a[4][4],b[4][4],j,k,flag=0,ans;
	cin >> t;
	for(i=0;i<t;i++)
	{
		cin >> a1;
		a1--;
		flag=0;
		ans=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			cin >> a[j][k];
		}
		cin >> a2;
		a2--;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			cin >> b[j][k];
		}
		
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[a1][j]==b[a2][k])
				{
				ans=a[a1][j];
				flag++;
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		if(flag==0)
		cout << "Volunteer cheated!";
		else if(flag==1)
		cout << ans;
		else
		cout << "Bad magician!";
		
		cout << "\n"; 
	}
	
	return 0;
}
