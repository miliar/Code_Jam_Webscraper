#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;
int main()
{
	ifstream in("dummyInput.in");
	ofstream out("dummy.out");
	int cases  = 0;
	int currentCase = 1;
	double c = 0;
	double f = 0;
	double x = 0;
	double cps = 0;
	double time = 0;
	double ttw = 0;
	double ttf = 0;
	
	double checkTime = 0;

	if(in.is_open())
	{
		in>>cases;
		while(currentCase <= cases)
		{
			time = 0;
			in>>c;			// Cookies required to purchase cookie farm
			in>>f;			// Extra Cookies per second from farm
			in>>x;			// Total Cookies required to win the game
			cps = 2.0;		// Default Cookie per Second
		
			ttw = x/cps;
			ttf = c/cps;
			
			if(x <= c)
			{
			   out <<"Case #"<<currentCase<<": "<<fixed<<setprecision(7)<<ttw<<endl;
			}
			else
			{
				checkTime = ttf + x/(cps+f);
				while(ttw >= checkTime)
				{
					
					time += ttf;
					cps += f;
					ttw = x/cps;
					ttf = c/cps;	
					checkTime = ttf + x/(cps+f);
							
				}
				time += ttw;
				
				out <<"Case #"<<currentCase<<": "<<fixed<<setprecision(7)<<time<<endl;
			}
			
			currentCase++;		// Incrementing currentCase Variable
		}	
	}

	in.close();
}
