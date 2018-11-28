#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <cmath>
#include <stack>

using namespace std;

double sea, ph, eks, lan, start, ha, pt, pehla, doosra, extra1, extra2, extra3;

int main()
{
	//mera kuch bhi comment
	long long int T;
    cin >> T;
    for(int q=1; q<=T; q++)
    {
       cin >> sea >> ph >> eks;
       start = 1;
       start = start*2;
       pt=0;
       ha=0;
       extra1 = 0;
       while((eks!=pt))
       {
       	//mera ek aur bakwaas comment
       	   pehla = sea / start;
           lan = eks / start;
           doosra = eks / (ph + start);
           if(lan <= (pehla + doosra))
           {
               pt = eks;
               ha = ha + lan;
           }
           else
           {
           	//ek aur ghatiya comment
              start = start + ph;
              ha = ha + pehla;
              ha = ha + extra1;
           }
       }
       cout << fixed;
       cout << "Case #" << q << ": " << setprecision(7) << ha << endl;
       //ye ek bahut hi pelu code likha gaya hai.
    }
    return 0;
}