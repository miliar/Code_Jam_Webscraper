#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <bitset>
#include <math.h>

using namespace std;

int is_prime(long long x) {
	
	if (x % 2 == 0) 
		return 2;

	for (long long i=3; i<sqrt(x); i+=2)
	{
		if (x % i == 0)
		{
			return i;
		}
	}
	
	return 0;	
}

int main(int argc, char *args[]) {
	if (argc == 2 && strcmp(args[1], "small") == 0) {
		freopen("small.in", "r", stdin);
		freopen("small.out", "w", stdout);
	}
	else if (argc == 2 && strcmp(args[1], "large") == 0) {
		freopen("large.in", "r", stdin);
		freopen("large.out", "w", stdout);
	}
	else {
		cout << "\nPlease enter \"small\" or \"large\" test file.";
		return 0;
	}

	int N = 16;
	int J = 50;

	printf("Case #1:\n");

	for (int i=0; i<=383 && J > 0; i++) {
		bool isbreaked = false;
		string s = "1" + bitset<14>(i).to_string() + "1";
		const char* schr = s.c_str();
        long long dvs[9] = {0};
        for (int b=2; b<=10; b++) {
			long long x = strtoll(schr, NULL, b);			
		    // printf("%lld\n", x);
            int dv = is_prime(x);
            if (dv > 0) {
                dvs[b-2] = dv;
			}
			else {
				isbreaked = true;
				break;
			}
		}
		if (!isbreaked) {
       		printf("%s %lld %lld %lld %lld %lld %lld %lld %lld %lld\n", schr, dvs[0],dvs[1],dvs[2],dvs[3],dvs[4],dvs[5],dvs[6],dvs[7],dvs[8]);
			J--;
		}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;	
}	

