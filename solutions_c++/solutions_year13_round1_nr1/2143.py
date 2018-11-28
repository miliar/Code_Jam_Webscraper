#include <iostream>
#include <conio.h>
#include "DynamicArray.h"

using namespace std;

int* asd();

void main()
{
	int index ,index2=1;
	cin>>index;
	while(index)
	{
		int result=1;
		int r,t;
		cin>>r>>t;
		int rl=r+2;
		int rn=r+3;
		t -= (r+1)*(r+1) - r*r;

		while(1)
		{
			if((rn*rn - rl*rl) <= t)
			{
				t -= (rn*rn - rl*rl);
				rn+=2;
				rl+=2;
				result++;
			}
			else
				break;
		}


		cout<<"Case #"<<index2<<": "<<result<<endl;
		index--;
		index2++;
	}
}