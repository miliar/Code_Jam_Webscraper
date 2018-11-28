#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;

int main (void)
{
	int num;
	cin >> num;
	
	unsigned long int x,r,t;
	for (x=0;x<num;x++){
		cin >> r;
		cin >> t;
		
		int y=0;
		unsigned long int circle_r = r+1;
		
		/*while (M_PI*((circle_r*circle_r)-((circle_r-1)*(circle_r-1)))<=t) {
			t=t-M_PI*((circle_r*circle_r)-((circle_r-1)*(circle_r-1)));
			y++;
			circle_r=circle_r+2;
		}*/
		
		while ((circle_r*circle_r)-((circle_r-1)*(circle_r-1))<=t) {
			t=t-((circle_r*circle_r)-((circle_r-1)*(circle_r-1)));
			y++;
			circle_r=circle_r+2;
		}
		
		cout << "Case #" << x+1 << ": " << y << endl;
	}
	
	return 0;
}
