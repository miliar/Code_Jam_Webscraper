

#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;
int main ()
{	

 long double R,F,C,X,T;
 cin >> T;
 long double time;
 long double cookieCost,currSplurgeCost, nextSplurgeCost;
 for(int t = 0; t < T; t++)
 {
 	cin >> C >> F >> X;
 	//cout << C << " " << F << " " << X << endl;
 	time = 0;
 	R=2;
 	int numCookies;
 	//cout << "R\tcookieCost\tcurrSplurgeCost\tnextSplurgeCost\n";
 	while(true)
 	{

		cookieCost = C/R;
		currSplurgeCost = X/R;
		nextSplurgeCost = cookieCost +(X)/(R+F);
 		//cout << R << "\t" << cookieCost << "\t" << currSplurgeCost << "\t" << nextSplurgeCost << endl;
		if(currSplurgeCost < nextSplurgeCost || currSplurgeCost <=cookieCost){
			time += currSplurgeCost;
			break;
		}else
		{
			time +=cookieCost;
			
		}
		R+=F;
 	}
 	cout.precision(7);
 	cout << "Case #" << t+1 << ": " << fixed<<(double)time << endl;
 }//!t

}
