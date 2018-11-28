#include "math.h"
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <conio.h>
#include <iomanip>
using namespace std;



int main()
{
	
	int a=0,i=0;
	ifstream in("Input.txt");	
    if (!in) {
    cout << "Cannot open file.\n";
    return 0;
     }
	freopen("Output.txt", "w", stdout);
    in>>a;
	
	for(i=1;i<=a;i++)
	{
		double x=0,f=0,c=0,k=2,d=0;
		in>>c;
		in>>f;
		in>>x;
		while(c/k+x/(k+f)<x/k)
		{
			d=d+c/k;
			k=k+f;
		}
		d=d+x/k;
		
		printf("Case #%d: %.7f\n",i, d);
	}
	fclose (stdout);
	in.close();

 return 0;
}