#include <iostream>
#include <iomanip>
#include <cstdio>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <utility>
#include <fstream>
using namespace std;
int main()
{
	std::iostream::sync_with_stdio(false);
	int s=1;
	ofstream myfile;
	myfile.open ("example.txt");
	ifstream infile;
	infile.open("B-large.in");
	int t;
	infile>>t;
	//cin>>t;
	while(t--)
	{
		double c,f,x;
		infile>>c>>f>>x;
		//cin>>c>>f>>x;
		double y=1;
		double t=x/2;
		double sum=c/2;
		while(1)
		{
			t=min(t,sum+x/(2+y*f));
			if(t!=sum+x/(2+y*f))
				break;
			sum+=c/(2+y*f);
			y++;
		}
		myfile<<std::fixed;
		myfile<<setprecision(7)<<"Case #"<<s<<": "<<t<<endl;
		s++;
	}	
	return 0;
}