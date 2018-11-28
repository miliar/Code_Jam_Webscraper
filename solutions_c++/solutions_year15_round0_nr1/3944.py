#include <iostream>
#include <vector>
#include <string>

using namespace std;

void print(vector<int> v)
{
    for (int i = 0; i < v.size(); i++)
    {
	cout << v[i] << " ";
    }
    cout << endl;
}

int main()
{
    int numCases;
    cin >> numCases;
    for (int c = 1; c <= numCases; c++)
    {
	int maxShy;
	string shyString;
	cin >> maxShy;
	vector<int> numppl(maxShy+1);
	cin >> shyString;
	for (int i = 0; i <= maxShy; i++)
	{
	    numppl[i] = shyString[i]-48;
	}
	//print(numppl);
	int total = 0;
	int needInvite = 0;
	for (int i = 0; i <= maxShy; i++)
	{
	    if (total < i)
	    {
		needInvite += i - total;
		total += i - total;
	    }
	    total += numppl[i];
	}
	cout << "Case #" << c << ": " << needInvite << endl;
    }
}
