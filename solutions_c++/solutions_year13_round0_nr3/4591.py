#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

bool isPal(long long a)
{
	vector<int> x;
	do
	{
		x.push_back(a%10);
		a/=10;
	}
	while(a>0);

	int size = x.size();
	for(int i=0;i<size/2;i++)
	{
		if(x[i]!=x[size-1-i])
			return false;
	}
	return true;
}

void run()
{
	long long A,B;
	cin>>A>>B;

	int start = sqrt((double)A);

	long long curSqr;

	while(start*start<A) start++;
	long long res=0;
	for(long long i=start; (curSqr = i*i)<=B;i++)
	{
		if(isPal(i) && isPal(curSqr))
			res++;
	}
	cout<<res<<endl;
}

int main()
{
	string input_name = "C-small-attempt0.in";
	string output_name = "output.txt";

	freopen(input_name.c_str(),"r",stdin);
	freopen(output_name.c_str(),"w",stdout);

	int test;
	cin>>test;
	for(int i = 1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		run();
	}
	return 0;
}