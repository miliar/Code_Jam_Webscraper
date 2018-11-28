#include <iostream>
#include <string>

using namespace std;
int main() 
{
	int t;
	string s;
	cin >> t;
	for (int a0 = 1; a0 <= t; a0++)
	{
		cin >> s;
		int k = s.length();
	    int m=0;
		for (int i=0;i<k-1;i++)
		    if (s[i] != s[i+1])
		       m++;
		if (s[k-1] == '-')
		    m++;
		    
		cout << "Case #" << a0 << ": " << m << endl;
	}
return 0;
}