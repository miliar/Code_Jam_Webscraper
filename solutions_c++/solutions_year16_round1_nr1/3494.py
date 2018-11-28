#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string order(string a)
{
    stringstream ss;
    string temp;
    ss << a[0];
    ss >> temp;
    string b = temp;
    int sz = a.length();
    for(int i = 1; i < sz; ++i)
    {
        if(a[i] < b[0])
            b = b + a[i];
        else
            b = a[i] + b;
    }
    return b;
}


int main()
{
	int T;
	cin >> T;
	string a;
	for(int i = 0; i < T; ++i)
	{
		cin >> a;
        cout << "Case #" << i+1 << ": " << order(a) << endl;
	}
	return 0;
}
