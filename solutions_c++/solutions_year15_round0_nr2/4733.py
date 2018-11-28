#include <cstdio>
#include <iostream>
using namespace std;
int arr[1010], N;


int main(){
	int tt;
	cin >> tt;
	for (int tcas = 1; tcas <= tt; ++tcas){
		
		cin >> N;
		for (int i = 0; i < N; ++i)
			cin >> arr[i];
		int res = 1000;
		
		for (int i = 1; i <= 1000; ++i){
			int tmp = i;
			for (int j = 0; j < N; ++j)
				tmp += (arr[j]-1) / i;
			if (tmp < res) res = tmp;
		}		
		printf("Case #%d: %d\n", tcas, res);
	}
}
	
