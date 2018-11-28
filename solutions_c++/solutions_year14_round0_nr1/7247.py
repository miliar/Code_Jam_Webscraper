#include <iostream>       // std::cout
#include <stdio.h>
using namespace std;
typedef unsigned int uint;
int main ()
{
	uint test_cases = 0;
	uint row1,row2;
	uint i,j,k,count,ans;
  	uint uiarrange1[5][5],uiarrange2[5][5];
  	cin >> test_cases;
  	for (i=1;i<=test_cases;i++) 
  	{	
		cin >> row1;
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				cin >> uiarrange1[j][k];
			}
		}
		cin >> row2;
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				cin >> uiarrange2[j][k];
			}
		}
		count = 0;
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				if(uiarrange1[row1][j] == uiarrange2[row2][k])
				{
					ans = uiarrange2[row2][k];
					count++;
				}
			}
		}
		if(count == 1)
		{
			cout << "Case #" << i << ": " << ans << endl;
		}
		else if(count > 1)
		{
			cout << "Case #" << i << ": " << "Bad magician!" << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
		}		
		
  	}
  return 0;
}
