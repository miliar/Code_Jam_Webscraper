#include <bits/stdc++.h>

using namespace std;

std::vector<int> tmp, stat;
int res[500][10];

long long get_int_from_base(int n, int length, int base){

	long long sum =0;

	for (int i =length; i >= 0; i--){
		int t = ( (n & (1 << i)) != 0) ? 1 : 0;
		sum = sum * base + t;
	}
	return sum;
}

int main(){
	
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int test;

	scanf("%d\n", &test);
	int n, m;
	scanf("%d %d", &n, &m);

	int counter =0;

	for (int i = (1 << n) - 1 ; i >=0; i-- ){
		if (( (i & (1 << (n -1))) != 0) && ((i % 2) ==1)){
			tmp.clear();
			bool take = true;
			for (int j = 2; j <= 10; j++){
				bool is_prime = true;
				long long t = get_int_from_base(i, n-1, j);
		
				for (int k =2; k < sqrt(t); k ++){
					if (t % k == 0){
						is_prime = false;
						tmp.push_back(k);
						break;
					}
				}
				if (is_prime){
					take = false;
					break;
				}
			}

			if (take){
				counter ++;
				stat.push_back(i);
				for (int j =0; j < 9; j++){
					res[counter][j] = tmp[j];
				}
			}

			if (counter == m){
				printf("Case #1: \n");

				for (int z = 0; z < m; z ++){
					string s = "";
					for (int j = n-1; j >= 0; j--){
						if ((stat[z] & (1 << j)) != 0) {
							s += '1';
						} else {
							s +='0';
						}
					}

					printf("%s ", s.c_str());
					for (int j= 0; j < 9; j++){
						printf("%d ", res[z+1][j]);
					}
					printf("\n");
				}
				return 0;
			}
		}
	}
	return 0;
}