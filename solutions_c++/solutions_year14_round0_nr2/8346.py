#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream a;
	ofstream q;
	a.open("B-large.in");
	q.open("B-small-out.txt");
	int t,c = 0;
	double C,F,X,tim,tim1,s = 0,rat;
	a>>t;
	for (c = 0; c < t; c++)
    {

        a>>C;
        a>>F;
        a>>X;
        rat = 2;
        tim = X/rat;
        tim1 = C/rat + X/(rat + F);
        while (tim1 < tim)
        {
            s = s + (C/rat);
            rat = rat + F;
            tim = X/rat;
            tim1 = C/rat + X/(rat + F);

        }
        q.precision(7);
        q.setf(ios::fixed);
        q.setf(ios::showpoint);
        q<<"Case #"<<c + 1<<": "<<s + tim<<endl;
        s = 0;
    }
};
