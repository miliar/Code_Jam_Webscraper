#include <stdio.h>
#include <istream>
#include <sstream>
#include <iomanip>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <deque>
#include <queue>

typedef long long ll;

using namespace std;

void run(double c, double f, double x)
{
	double production =2.0;
	double total=0.0;
	double time=0.0;

	if(x<=c)
	{
		cout<<x/2;
		return;
	}

	time=c/2;


	//Decide whether to buy a farm
	while((x-c)/production>c/f)
	{
		production+=f;
		time+=c/production;
	}

	//Now wait
	time+=(x-c)/production;

	cout<<time;
	return;
}





int main(int argc, char** argv)
{
	cout<<setprecision(12);
	int T;
	cin>>T; cin.ignore();
	string line;

	for(int i=1;i<=T;i++)
	{
		getline(cin, line);
		stringstream ss(line);
		double c, f, x;
		ss>>c;
		ss>>f;
		ss>>x;
		cout<<"Case #"<<i<<": ";
		run(c,f,x);
		cout<<endl;
	}
}