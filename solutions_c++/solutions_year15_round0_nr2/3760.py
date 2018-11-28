// Q2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include<fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;


int max_cake(int D, int P[])
{
	int i;
	int max;

	max=P[0];
	for (i=0;i<D;i++)
	{
		if (P[i]>max)
		    max=P[i];
	}

	return max;
}

int single_divide(int cake, int base)
{
	double x;
	x=double(cake)/double(base);
	return (ceil(x)-1);
	
}

long int divide_cake_with_base(int D, int P[], int base)
{
	int i;
	long int sum=0;

	for (i=0;i<D;i++)
		sum=sum+single_divide(P[i],base);

	return sum;
}


long int total_time(int D, int P[])
{
	int base;
	int max;
	long int time[1000];
	long int total=0;

	max=max_cake(D,P);
	
	for (base=1;base<max;base++)
	{
		time[base-1]=divide_cake_with_base(D,P,base)+base;
	}

	total=max;
	for (base=1;base<max;base++)
	{
		if (total>time[base-1])
			total=time[base-1];
	}

	return total;
}




int main()
{
	freopen("C://wxy_project//B-large.in", "r", stdin);
    freopen("C://wxy_project//B-large.out", "w", stdout);

	string line_T;

    getline (cin,line_T);
	stringstream stream(line_T);

	int Casenum;

	while(1) {
       stream >> Casenum;
       if(!stream)
          break;
    }

	for(int i=0; i<Casenum; i++) {
	    string line_D;
	    string line_P;
		int D;
		int P[1000];

		getline(cin,line_D);
		stringstream stream(line_D);

		while(1) {
           stream >> D;
           if(!stream)
              break;
        }

		

		getline(cin,line_P);
		stringstream stream2(line_P);

		int index=0;
		while(1) {
            stream2 >> P[index] ;
		    index++;
            if(!stream2)
               break;
        }



		cout << "Case #" << (i+1) << ": " << total_time(D, P) << endl;
	}
	return 0;
}

