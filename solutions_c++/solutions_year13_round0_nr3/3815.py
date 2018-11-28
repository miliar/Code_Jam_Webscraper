#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std;

bool palindrome(int num)
{
	int tmp = num;
	int a;
	for(a=0; tmp;a = a*10 + tmp%10, tmp/=10);
	return a == num;
}

int ffs(int A, int B)
{
	int counter = 0;
	int lower = sqrt(A);
	lower = lower*lower == A?lower:lower+1;
	int upper = sqrt(B);
	for(int i = lower; i <= upper; i++)
	{
		if(palindrome(i) && palindrome(i*i)) {
				cout<<i<<" "<<i*i<<endl;
				counter++;
		}
	}
	//cout<<counter<<endl;
	return counter;
}
int main()
{
    ifstream in("input.in");
    ofstream out("output.in");

	int T, A, B;
	in>>T;
	for(int i = 0; i < T; i++)
	{
		in>>A>>B;
		out<<"Case #"<<i+1<<": ";
		out<<ffs(A,B)<<endl;
	}
	return 0;

}
