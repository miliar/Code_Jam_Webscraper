#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	int Smax;
	int shyness[1001];
	char c;
	
	for (int i = 1; i <= T ; i ++){
		long long int sum = 0;
		long long int friends = 0;

		scanf("%d", &Smax);
		scanf("%c", &c);
		for (int j = 0; j <= Smax; j++){
			scanf("%c", &c);
			shyness[j] = c - '0';
		}
		sum = shyness[0];
		for (int j=1; j<=Smax; j++) {
			if ((sum < j) && (shyness[j]>0)) {
				friends = friends + (j-sum);
				sum = j;
			}	
			sum = sum + shyness[j];	
		}
	
		printf("Case #%d: %lld\n", i, friends);
	}
	

}
