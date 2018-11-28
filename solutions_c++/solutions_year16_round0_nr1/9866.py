#include<stdio.h>
#include<set>

using namespace std;


int main(void) {

	int testcase;
	int num, tmp,tmp_num;
	int k = 1;
	int count;
	FILE *input = freopen("input.txt", "r", stdin);
	FILE *output = freopen("output.txt", "w+", stdout);
	
	scanf("%d", &testcase);

	for (int i = 0; i < testcase; i++) {
		int n = 1;
		scanf("%d", &num);
		
		if (num == 0) {
			printf("Case #%d: INSOMNIA\n", k);
			k++;
			continue;
		}
		set<int> s;
		
		while (true) {
			tmp_num = num*n;
			while (tmp_num != 0) {
				tmp = tmp_num % 10;
				tmp_num /= 10;

				s.insert(tmp);
			}
			
			if (s.size() == 10) {
				printf("Case #%d: %d\n", k, num*n);
				break;
			}
			
			n++;
			
		}
		k++;
	}



	return 0;
}