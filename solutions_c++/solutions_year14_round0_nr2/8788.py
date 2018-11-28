//SKimov gJam Cooocies
#include <iostream>
#include <vector>
using namespace std;
struct farmpos
{
	double c;
	double f;
	double x;
};
int main()
{
	int incount;
	cin >> incount;
	vector<farmpos> farms;
	for (int i =0; i< incount;i++)
	{
		farmpos fp;
		cin >>fp.c>>fp.f>>fp.x;
		farms.push_back(fp);
	}
	for(int i =0; i <farms.size();i++)
	{
		double ct=0, cf = 2;
		bool stop = false;
		while(!stop)
		{
			double answ = ct +(farms[i].c/cf)+farms[i].x/(cf+farms[i].f);
			double ads = farms[i].x/cf + ct;
			if(answ < ads)
			{
				ct += farms[i].c/cf;
				cf = cf+farms[i].f;
			} else
			{
				ct = ct+(farms[i].x/cf);
				stop = true;
			}
		}
		//cout.precision(dbl::digits10);
		//cout <<"Case #"<<i+1<<": "<<round(ct,7)<<endl;
		printf("Case #%d: %0.7f\n",i,ct);
	}
	return 0;
}