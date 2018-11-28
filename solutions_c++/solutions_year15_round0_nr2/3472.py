#include<iostream>
#include<cstdio>
using namespace std;

int din[1005];

int main()
{
	ios_base::sync_with_stdio(0);
	int tests, plates, sum, result;
	
	cin >> tests;
	for(int t=1; t<=tests; t++) {
		result = 0;
		cin >> plates;
		for(int i=1; i<=plates; i++) {
			cin >> din[i];
			result = max(din[i], result);
		}
		
		for(int i=1; i<result; i++) {
			sum = 0;
			for(int j=1; j<=plates; j++) {
				sum = sum + (din[j]-1)/i;
			}
			result = min(result, (sum+i));
		}
		
		cout << "Case #" << t << ": " << result << "\n";
		}
	return 0;
	}
