#include <iostream>

using namespace std;

int reset(long long unsigned int arr[]){
long long unsigned int	i;
						for(i = 0 ; i < 10 ; i++)
							arr[i] = 0;
						return 0;	
}

int update(long long unsigned int N, long long unsigned int arr[], long long unsigned int &sum){
long long unsigned int	dig;
						while(N != 0){
							dig = N % 10;
							if(arr[dig] == 0){
								sum++;
								arr[dig] = 1;
							}
							N /= 10;
						}
						return 0;
}

int main(){
long long unsigned int	arr[10], sum = 0, T, i, N, j;
						cin >> T;
						for(i = 0 ; i < T ; i++){
							reset(arr);
							sum = 0;
							cin >> N;
							for(j = 1 ; j <= 10000 ; j++){
								update(j * N, arr, sum);
								if(sum == 10)goto CONT;
							}
							CONT :
								cout << "Case #" << i + 1 << ": ";
								if(sum != 10)cout << "INSOMNIA";
								else cout << j * N;
								if(i != T - 1)cout << endl;
						}
						return 0;
}
