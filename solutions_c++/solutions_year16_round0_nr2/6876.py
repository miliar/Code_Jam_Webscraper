#include <iostream>
#include <string>

using namespace std;

int main(){
	int T, len, i, count, testcase = 1;
	string pancake;

	FILE *finput = freopen("input.txt", "r", stdin);
	FILE *foutput = freopen("output.txt", "w+", stdout);

	scanf("%d",&T);

	while (T--){
		cin >> pancake;
		count = 0;
		
		len = pancake.size();
		for (i = 0; i < len-1; i++)
			if (pancake[i] != pancake[i + 1]) count++;
		if (pancake[len - 1] == '-') count++;
		printf("Case #%d: %d\n", testcase++, count);
	}

	return 0;
}