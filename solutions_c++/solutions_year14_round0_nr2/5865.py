#include <iostream>
#include <cstdlib>

using namespace std;

int main(void)
{
	int n;

	double C;	//cost 
	double F;	//extra
	double X;	//target
	
	double S;

	double t0;
	double tot_time;
	int teller;
	double solution;
	double time;

	cout << fixed;
	cout.precision(7);

	cin >> n;
	
	for(int i=0;i<n;i++)
	{
		tot_time = 0;
		teller = 1;
		S = 2.0;
		cin >> C >> F >> X;	

		t0 = X/S;

		while(1)	
		{
			time = X/(S+teller*F);
			for(int j=teller-1;j>=0;j--)
			{
				time += C/(S+j*F); 
			}
			if(time >= t0)
			{
				solution = t0;
				break;
			}
			teller++;
			t0 = time;
		}
		

		cout << "Case #" << i+1 << ": "; 
		cout << solution << endl;
	}

}
