#include <cstdio>
#include <vector>
using std::vector;

int main()
{
	int T;	scanf("%d", &T);
	vector<int> digit;
	for(int i = 0; i < 10; ++i)
		digit.push_back(i);
	
	int N, N_origin, tmp, tmp2;
	for(int j = 0; j < T; ++j) {
		scanf("%d", &N);
		if(!N) {
			printf("Case #%d: INSOMNIA\n", j + 1);
			continue;
		}
		N_origin = N;
		while(digit.empty() == 0) {
			tmp = N;
			while(tmp) {
				tmp2 = tmp % 10, tmp /= 10;
				for(vector<int>::iterator it = digit.begin(); it != digit.end(); ++it)
					if(*it == tmp2) {
						digit.erase(it);
						break;
					}
			}
			N += N_origin;
		}
		printf("Case #%d: %d\n", j + 1, N - N_origin);
		for(int i = 0; i < 10; ++i)
			digit.push_back(i);
	}
	
	return 0;
}