#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
using namespace std;

bool palindrome(int num)
{
	int tmp = num;
	int a;
	for(a=0; tmp; tmp/=10)
		a = a*10 + tmp%10;
	return a == num;
}

int ffs(int a, int b)
{
	int c = 0;
	int l = sqrt(a);
	l = l*l == a?l:l+1;
	int u = sqrt(b);
	for(int i = l; i <= u; i++)
	{
		if(palindrome(i) && palindrome(i*i)) {
				cout<<i<<" "<<i*i<<endl;
				c++;
		}
	}
	return c;
}
int main()
{
    ifstream in("square.in");
    ofstream out("square.out");

	int t, a, b;
	in >> t;
	for(int i = 0; i < t; i++)
	{
		in >> a >> b;
		out << "Case #" << i+1 <<": " << ffs(a,b) << endl;
	}
	return 0;

}

