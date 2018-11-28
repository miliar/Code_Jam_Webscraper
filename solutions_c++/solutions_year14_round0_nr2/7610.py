/*Input

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line contains three space-separated real-valued numbers: C, F and X, whose meanings are described earlier in the problem statement.

C, F and X will each consist of at least 1 digit followed by 1 decimal point followed by from 1 to 5 digits. There will be no leading zeroes.
Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of seconds it takes before you can have X delicious cookies.

We recommend outputting y to 7 decimal places, but it is not required. y will be considered correct if it is close enough to the correct number: within an absolute or relative error of 10-6. See the FAQ for an explanation of what that means, and what formats of real numbers we accept. 
*/
#include<iostream>
#include<cstdio>
#include<cstdlib> 
using namespace std;
#define lli long long int

int main()
{
	int T,casen=0;
	double C,F,X,bs=2,ctimes,prevt,news,newt;//bs=base speed,bt=base time
	cin >> T;
	while(T--)
	{
		cin >> C >> F >> X;
		bs=2;

		ctimes=C/bs;/////
		prevt=X/bs;/////
		news=bs+F;/////
		newt=ctimes+(X/news);/////
		while(newt<prevt)
		{
			prevt=newt;
			ctimes+=(C/news);
			news+=F;
			newt=ctimes+(X/news);			
		}
		cout << "Case #" << ++casen << ": ";
		printf("%.7lf",prevt);
		cout << "\n";
	}
	return 0;
}

