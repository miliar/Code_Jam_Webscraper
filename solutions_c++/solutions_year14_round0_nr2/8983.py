#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int main ()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
		
	int T = 0;
	cin >> T;
	
	for (int i = 1; i<=T; ++i)
	{
		double C, F, X, R = 2., t1 = 0, t2 = 0, P = 0, t = 0;
		cin >> C >> F >> X;
		
		int q = 1;
		t = C/R;
		t1 = X/R;
		t2 = X/(R+F) + t;
		while (t1>t2)
		{
			t1 = t2;
			q++;
			t += C/(R+(q-1)*F);
			t2 = X/(R+q*F)+	t;	
		}
		char buff [1024];
		sprintf(buff,"Case #%d: %.7lf",i,t1);
		cout << buff;
		if (i!=T) cout << endl;
	}	
	
	return 0;
}
