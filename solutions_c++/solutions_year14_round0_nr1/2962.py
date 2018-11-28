
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int conv (string x)
{
	int z;
	if (x == "O")z=1;
	else if (x == "X") z=10;
	else if (x == ".") z=100;
	else if (x == "T") z=5;
	else z = 100 ;

	return z ;
}
int main()
{
	freopen("D:\\C++ Projects\\Magic\\A-small-attempt0.in","r",stdin); // For reading input
    freopen("D:\\C++ Projects\\Magic\\Output.txt","w",stdout); // for writing output
	int L, T;cin>>T;
	int x[4][4] , y[4][4],ch1,ch2;
	for (L=1;L<=T;L++)
	{
		cin >> ch1 ;
		int i,j ,R = 0 ,clk = 0 ;
		for (i=0;i<=3;i++)
		{
			for (j=0;j<=3;j++)
				cin >> x[i][j];
		}
		
		cin >> ch2 ;
		for (i=0;i<=3;i++)
		{
			for (j=0;j<=3;j++)
				cin >> y[i][j];
		}


		for (i=0;i<=3;i++)
		{
			for (j=0;j<=3;j++)
			{
				if (x[ch1-1][i] == y[ch2-1][j])
				{
				R = x[ch1-1][i];
				if (R != 0)
				{
				clk = clk + 1	;
				}
				}
			}
		}
		if (clk == 1)
			cout <<"Case #" <<L<<": "<<R<< '\n' ;
		else if (clk == 0)
			cout <<"Case #" <<L<<": "<<"Volunteer cheated! \n" ;
		else 
			cout <<"Case #" <<L<<": "<<"Bad magician! \n" ;

	}
return 0;
}
