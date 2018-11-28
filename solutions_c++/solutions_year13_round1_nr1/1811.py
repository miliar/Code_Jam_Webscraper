#include <fstream>
#include <cmath>
#include <sstream>
//#include <string>
using namespace std;

string itoa(double n)
// postcondition: return string equivalent of int n
{
    ostringstream output;
    output << n;   
    return output.str();
}

int main()
{
	ifstream input("f.txt");
	ofstream output("out.txt");
	int test_cases;
	input >> test_cases;
	for (int i = 0; i < test_cases; i++)
	{
		double radius, t;
		input >> radius >> t;
		double a =  floor(sqrt(t/(2 * radius + 1)));
		for (; (2 * radius - 1) * a + 2 * a * a <= t; a++);
		output << "Case #" << i+1 << ": " << itoa(a-1) << endl;
	}
	system("PAUSE");
	return 0;
}