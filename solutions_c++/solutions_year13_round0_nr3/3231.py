#include <iostream>
#include <string>
#include <cmath>
#include <cassert>
using namespace std;

string ftoa(double val);
bool ispalindromes(double v);

int main()
{
	int T ; cin >> T;
	for(int n = 1; n <= T; n++)
	{
		double A, B;
		cin >> A >> B;
		double a = sqrt(A);
		double b = sqrt(B);
		a = ceil(a);
		b = floor(b);
		int count = 0;
		for(double i = a; i <= b; i++)
		{
			if(!ispalindromes(i)) continue;
			double j = i*i;
			if(ispalindromes(j)) count++;
		}
		cout<<"Case #"<<n<<": "<<count<<endl;
	}
}

bool ispalindromes(double v)
{
	string str = ftoa(v);
	string str2 = str;
	reverse(str2.begin(), str2.end());
	return str == str2;
}

string ftoa(double val)
{
	string str="";
	char c[1] = {'0'};
	while(val > 0)
	{
		int a = fmod(val,10);
		assert(a >= 0 && a <= 9);
		switch(a)
		{
			case 0: str += "0"; break;
			case 1: str += "1"; break;
			case 2: str += "2"; break;
			case 3: str += "3"; break;
			case 4: str += "4"; break;
			case 5: str += "5"; break;
			case 6: str += "6"; break;
			case 7: str += "7"; break;
			case 8: str += "8"; break;
			case 9: str += "9"; break;
			default:
					exit(0);
		}
		val = (val-a)/10;
	}
	//reverse(str.begin(), str.end());
	return str;
}
