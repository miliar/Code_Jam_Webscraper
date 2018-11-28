#include <iostream>
#include <fstream>
#include <conio.h>
#include <iomanip> 
#include <cmath> 

using namespace std; 

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	double f, sf, w, t=0, s=2;
	cin >> T;
	bool found = true;
	for (int i=0; i<T; i++)
	{
		cin >> f >> sf >> w;
		if (f/s >= w/s)
		cout << "Case #" << i+1 << ": " << fixed << setprecision(7) << w/s << '\n';
		else
		{
			for ( ; ; )
			{
				if ( w/s <= (f/s+w/(s+sf)) )
				{
					cout << "Case #" << i+1 << ": " << fixed << setprecision(7) << t+w/s << '\n';
					found = false;
				}
				else
				{
					t+=f/s;
					s+=sf;				
				}
				if (found == false)
				break;
			}	
		}		
		found = true;
		s=2;
		t=0;		
	}
	
	return 0;
}
//cout << "Case #" << i+1 << ": " << w/2 << '\n';
//cout << fixed << setprecision(8) << p << endl;
