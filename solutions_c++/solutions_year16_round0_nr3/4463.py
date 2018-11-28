#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <sstream>
#include <iomanip>
#include <time.h>
#include <fstream>

using namespace std;



int main()
{
	cout<<"Case #1:\n";
	for(int i=0;i<500;i++)
	{
		int n=i;
		cout<<1;
		for(int j=0;j<15;j++)
		{
			if(n%2==0) cout<<"00";
			else cout<<"11";
			n/=2;
		}
		cout<<"1 ";
		for(int b=2;b<=10;b++) cout<<b+1<<" ";
		cout<<"\n";
	}
	return 0;
}