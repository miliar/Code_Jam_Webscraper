#include <cmath>
#include <climits>
#include <queue>
#include <vector>
#include <unordered_map>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	int t, n, p = 1, count;
	string str;
	cin >> t;
	while(t--)
	{
		count = 0;
		cin >> str;
		for(int i=0; i<str.length()-1; i++) {
			if(str[i] != str[i+1])
				count++;
		}
		if(str.back() == '-')
			count++;
		cout << "Case #"<<p<<": "<<count<<endl;
		++p;
	}	
	return 0;
}
