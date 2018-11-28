#include <cstring>
#include <cstdio>
#include <iostream>
#include <iomanip>

#define BASECOOKIE 2.0

using namespace std;

int main()
{
    int ncases;
    cin >> ncases;
    cout << setprecision(7) << fixed;

    for(int i = 0; i < ncases; i++)
    {
	double farm; //C - # cookies to buy farm
	double bonus; // F - # extra cookies per farm
	double win; // X - # cookies to win
	cin >> farm;
	cin >> bonus;
	cin >> win;

	double time = win;
	int num_farm = 0;
	while(true)
	{
	    double new_time = 0.0;
	    //cout << new_time;
	    //number of farms
	    for(int j = 0; j < num_farm; j++)
	    {		
		//time to get farm
		double ftime = farm/(BASECOOKIE+((double)j*bonus));
	    	new_time += ftime;
		//cout << " + " << ftime;
	    }
	    new_time += win/(BASECOOKIE+((double)num_farm*bonus));
	    if(new_time < time) {
		time = new_time;
		num_farm++;
	    }
	    else
		break;
	}
	cout << "Case #" << i+1 << ": " << time << endl; 
    }

    return 0;
}
