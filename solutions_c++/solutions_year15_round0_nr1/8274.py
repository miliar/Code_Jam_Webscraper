#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
	string line;
	ifstream infile("A-large.in");
	ofstream offile("A-large.out", ios::out);

	while(getline(infile, line))
	{
		istringstream iss(line);
		long int a;
		string b;

		if(!(iss >>a >> b)){  }
		cout << a << " " << b << endl;

		long int oldnum=0,num=0, i=0, len;
		static long int outline =0;
		len = b.length() -1;
		long int reqd = 0,store=0;
		while(i <= len)
		{
			oldnum += num;
			num = (b[i]-'0');
		cout << "ppl standing "<< num << endl;
		if(num >0)
		{ 
		if(i>0 && oldnum >=i);
		else
		{
		       	reqd += (i-oldnum) ;
			store+=reqd;
			cout << "reqd "<< store<< endl;
		}
		oldnum+=reqd;
		reqd =0;
		}
			++i;
		}
		if(outline >0)
		offile <<"Case #"<<outline <<":"<< " " << store<< endl;
		++outline;
		reqd=0;
		store=0;
	}
	offile.close();


}
