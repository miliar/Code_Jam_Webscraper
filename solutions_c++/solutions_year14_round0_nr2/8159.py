#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <list>
#include <fstream>

using namespace std;

int main()
{
	std::ios_base::sync_with_stdio(false);

	int t;
	double time,c,f,x,per_sec;
	ofstream output;
    output.open("output.txt");
	ifstream input;
	input.open("input.txt");
	input>>t;

	for(int index=1;index<=t;index++)
	{
	    time=0.0;
	    per_sec=2.0;
	  //  fscanf("%lf %lf %lf",c,f,x);
		input>>c>>f>>x;

        while(1)
        {
            if((c/(per_sec))+(x/(per_sec+f)) > (x/per_sec))
            {
                time+=(x/per_sec);
                break;
            }else{
                time += (c/per_sec);
                per_sec += f;
            }
        }

        output<<std::fixed;
        output<<setprecision(7)<<"case #"<<index<<": "<<time<<endl;

	}
	output.close();
	input.close();

	return 0;
}
