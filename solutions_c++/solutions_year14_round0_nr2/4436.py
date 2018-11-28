#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

double getT(double C, double F, double X, int curC)
{
	double curF = 2;
	double curT = 0;
	for(int CC=0;CC<curC;CC++)
	{
		curT+=C/curF;
		curF+=F;
	}
	curT+=X/curF;
	return curT;
}


void run()
{
	double C,F,X;	

	cin>>C>>F>>X;
	int maxC = 1000000;

	double result = 1e10;
	int lt = 0, rt = maxC;
	while((rt - lt) > 50)
	{		
		int curC1 = (2 * lt + rt)/3;
		int curC2 = (lt + 2 * rt)/3;
		double q1 = getT(C,F,X,curC1);
		double q2 = getT(C,F,X,curC2);
		if(q1 < q2) rt = curC2;
		else lt = curC1;
	}
	for(int curC = lt; curC <=rt; curC++)
	{
		double q = getT(C,F,X,curC);
		if(q < result) result = q;
	}

	cout.setf(ios::fixed, ios::floatfield);
	cout.precision(7);
	cout<<result<<endl;
}

int main()
{
	string input_name = "B-large (1).in";
	freopen(input_name.c_str(),"r",stdin);

	string output_name = "output.txt";
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