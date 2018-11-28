#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int X,R,C;
	int T;

	cin >> T;

	string winner ="";

	for (int i = 0; i < T; i++)
	{
		cin >> X;
		cin >> R;
		cin >> C;

		if (X==1)
		{	// only one possible omino

		winner = "GABRIEL";

		}
		else if (X==2)
		{	
			if (R==1)
			{
				if (C==2 || C==4) winner = "GABRIEL";
				else winner = "RICHARD";
			}
			else if (R==2)
			{
				winner = "GABRIEL";
			}
			else if (R==3)
			{
				if (C==2 || C==4) winner = "GABRIEL";
				else winner = "RICHARD";
			}
			else if (R==4)
			{
				winner = "GABRIEL";
			}
			// only one possible 2-omino   00
			// if ((R*C)%2 == 0)
			// {
			// 	if (R*C==2){
			// 		winner = "RICHARD";
			// 	}
			// 	else {
			// 		winner = "GABRIEL";}
			// }
			// else 
			// 	winner = "RICHARD";

			// if (R==1)
			// {
			// 	if (C==1 || C==2 || C==3) winner = "RICHARD";
			// 	else winner = "GABRIEL";

			// }
			// if (R==2)
			// {
			// 	if (C==1)  winner = "RICHARD";
			//     else winner = "GABRIEL";
			// }
			// if (R==3)
			// {
			// 	if (C==1 || C==3)  winner = "RICHARD";
			// 	else winner = "GABRIEL";
			// }
			// if (R==4)
			// {
			// 	winner = "GABRIEL";
			// }

		}
		else if (X==3)
		{
			if (R==1)
			{
				 winner = "RICHARD";
			}
			else if (R==2)
			{
				if (C==3) winner = "GABRIEL";
				else  winner = "RICHARD";
			}
			else if (R==3)
			{
				if (C==1) winner = "RICHARD";
				else winner = "GABRIEL";
			}
			else if (R==4)
			{
				if (C==3) winner = "GABRIEL";
				else  winner = "RICHARD";
			}
			// if ( R*C < 6 || ((R*C-6>0)&&(R*C-6)%3!=0) )
			// {
			// 	winner = "RICHARD";
			// }
			// else 
			// {
			// 	winner = "GABRIEL";
			// }
			// if (R==1){
			// 	winner = "RICHARD";
			// }
			// else if (R==2){
			// 	if (C==3) winner = "GABRIEL"; 
			// 	else winner = "RICHARD";
			// }
			// else if (R==3){
			// 	if (C==1) winner = "RICHARD";
			// 	else winner = "GABRIEL"; 
			// }
			// else if (R==4){
			// 	if (C==1 || C==2 ) winner = "RICHARD";
			// 	else winner = "GABRIEL";
			// }

		}
		else if (X==4)
		{
			if (R==1)
			{
				winner = "RICHARD";
			}
			else if (R==2)
			{
				winner = "RICHARD";
			}
			else if (R==3)
			{
				if (C==1 || C==2 || C==3) winner = "RICHARD";
				else winner = "GABRIEL";
			}
			else if (R==4)
			{
				if (C==3 || C==4) winner = "GABRIEL";
				else winner = "RICHARD";
			}
			// if(R*C < 8 || ((R*C-8>0)&&(R*C-8)%4!=0))
			// {
			// 	winner = "RICHARD";
			// }
			// else 
			// {
			// 	winner = "GABRIEL";
			// }

			// if (R==1){
			// 	winner = "RICHARD";
			// }
			// else if (R==2){
			// 	winner = "RICHARD";
			// }
			// else if (R==3){
			// 	if (C<=3) winner = "RICHARD";
			// 	else if (C==4) winner = "GABRIEL"; 
			// }
			// else if (R==4){
			// 	if (C<=2) winner = "RICHARD";
			// 	else if (C>=3) winner = "GABRIEL";
			// }
		}


		cout << "Case #" << i+1 << ": " << winner << endl ;
	}
}