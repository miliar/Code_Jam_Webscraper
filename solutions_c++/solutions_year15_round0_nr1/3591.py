#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	int tests, max_shy, result, counter, people;
	char peo;
	cin >> tests;
	for(int t=1; t<=tests; t++) {
		result = 0;
		counter = 0;
		cin >> max_shy;
		for(int i=0; i<=max_shy; i++) {
			cin >> peo;
			people = int(peo) - int('0');
			if(counter < i) {
				result = result + i - counter;
				counter = i;
				}
			counter = counter + people;	
		}
		cout << "Case #" << t << ": " << result << "\n";
		}
	return 0;
	}
