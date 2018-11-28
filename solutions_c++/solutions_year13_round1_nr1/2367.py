#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <sstream>


using namespace std;

#define pb push_back

//g++ -o a.exe a.cpp
//./a.exe < A-small-practice.in > A-small-practice.out


int cases;


int main()
{
	long double r,t,area;
	int count=0;
	cin>> cases;	
		//cout << "begin"<<endl;
		for(int caseno=1;caseno<=cases;caseno++)
		{
			cin >>r>>t;
			
			area = 2*r+1;
			count=(((2-area)+sqrt(((area-2)*(area-2))+8*t))/(4));
			//cout<<floor((((3-2)+sqrt(((2-3)*(2-3))+8*5))/(4)));
			
			
			
			cout <<"Case #"<< caseno<<": "<< count << endl;
		}
	
	return 0;
}

