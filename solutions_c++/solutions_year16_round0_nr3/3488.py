#include<iostream>
#include<string.h>
#include<math.h>

using namespace std;

void inc(int arr[], int N) {
	for(int i = 1;i < N-1; i++) {
		if(arr[i] == 0) {
			arr[i] = 1;
			break;
		}
		else {
			if(arr[i+1] == 0) {
				for(int j = 1; j <= i; j++)
					arr[j] = 0;
				arr[i+1] = 1;
				break;
			}
		}
	}
}

int isPrime(long long int N) {
	long long int i;
	if(N % 2 == 0)
		return 2;
	
	for(i = 3; i <= sqrt(N); i += 2) {
		if(N % i == 0)
		return i;
	}
	return 1;
}
void printArray(int arr[], int N) {
	for(int i = N-1; i >= 0; i--)
		cout << arr[i];
}

void testCase(int arr[], int N, int J) {
	// Convert into base 2, 3, --- etc and check if it is prime
	int i, j, divisors[10];
	long long int num, result;
	while(J > 0) {
		int flag = 1;
		for(j = 2; j <= 10; j++) {
			num = 0;
			for(i = N-1; i >= 0; i--) {
				if(arr[i] == 1) {	
					num += pow(j, i);
				}
			}
			//printArray(arr, N);
			//cout << " base " << j << " value: " << num << endl;
			result = isPrime(num);
			if(result != 1) {
				divisors[j-2] = result;
			}
			else {
				flag = 0;
				break;
			}
		}
		if(flag == 1) {
			printArray(arr, N);
			cout << " " ;
			for(i = 0; i < 9; i++)
				cout << divisors[i] << " ";
			cout << endl;
			J--;
		}
		inc(arr, N);
		
	}
}



int main() {
	
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, N, J, t, len, count, arr[100000], i;
	cin >> T;
	t = 1;
	while(t <= T) {
		cin >> N >> J;
		for(i = 0; i < 100000; i++)
			arr[i] = 0;
		arr[0] = 1;
		arr[N-1] = 1;
		cout << "Case #" << t << ":\n";
		testCase(arr, N, J);
		//printf("Case #%d: %d\n", t, count);
		t++;	
	}
	
	return 0;
}
