#include <iostream>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <stack>
#include <vector>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

string cs = "Case #";

int main(int argc, char* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	int t;
	cin >> t;	
	for(int l=1;l<=t;l++)
	{
		double c,f,x;
		cin >> c >> f >> x;
		double time = 2000000,temp = 0;
		double d = 2;		
		double q;
		if(c < 10000)
			q=x*int(sqrt(x)+1); else
			q=x*5;
		while (d <=q)		
		{
			if (x/d +temp < time)
					time = x/d + temp;
			temp+=c/d;
			d+=f;
		}
		if (x/d+temp<time)
			time = x/d + temp;
		cout << cs << l <<": ";
		printf("%.7f\n",time);
	}
	return 0;
}
