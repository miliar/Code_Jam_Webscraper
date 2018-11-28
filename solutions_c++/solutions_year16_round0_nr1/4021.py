#include<iostream>

using namespace std;

int main() {
	
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, N, t, arr[10] ;
	cin >> T;
	t = 1;
	while(t < T) {
		
		for(int j = 0; j < 10; j++)
			arr[j] = 0;
			
		cin >> N;
		int mul = 1, num, temp;
		if (N == 0 ) {
			printf("Case #%d: INSOMNIA\n");
			continue;
		}
		while(true) {
			num = N * mul;
			temp = num;
			
			while(temp > 0) {
				arr[(temp % 10)] = 1;
				temp = temp / 10;
			}

			int flag = 1;
			for(int j = 0; j < 10; j++) {
				if (arr[j] == 0)
					flag = 0;
			}
			
			if(flag == 1) {
				printf("Case #%d: %d\n", t, num);
				break;
			}	
			mul++;
		}
		t++;
	}
	
	return 0;
}
