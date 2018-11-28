#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
using namespace std;

int cases = 0;

std::string itos(int number) {
	std::stringstream ss;
  ss << number;

  return ss.str();
}

bool pa(string n) {
	for (int i=0; i<n.size()/2; ++i)
		if (n[i] != n[n.size()-1])
			return false;

	return true; 
}

bool is(int n) {
	if (pa(itos(n)) && (int)(((int)sqrt(n*1.0)) * ((int)sqrt(n*1.0))) == n && pa(itos(sqrt(n*1.0))))
		return true;
	else
		return false;
}

void run()
{
	int f, t, n = 0;
	cin >> f >> t;

	for (int i=f; i<=t; ++i)
		if (is(i))
			n++;

	cout << "Case #" << (++cases) << ": " << n << endl;
}

int main()
{
	int n;
	cin >> n;
	while (n --> 0)
		run();
}