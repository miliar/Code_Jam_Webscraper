#include <iostream>

using namespace std;

int SumDigits(bool* digits);
void PrintDigitsArr(bool* digits);
void CheckDigits(int N, bool* digits);

int main(){
	int T(0);
	cin >> T;
	
	int64_t N(0);
	for (int i=0; i<T; i++){
		
		cin >> N;
		int count(1), num(N);
        bool digits[10] = {0};
		
		if (N==0){
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
		}else{
			while(SumDigits(digits) != 10){
				num = count * N;
				//cout << count << ", " << N << endl;
				CheckDigits(num, digits);
				count++;
			}
			cout << "Case #" << i+1 << ": " << num << endl;
		}
		
	} // end for
	
}

int SumDigits(bool* digits){
	int sum(0);
	for (int i=0;i<10;i++){
		sum += digits[i];
	}
	return sum;
}

void PrintDigitsArr(bool* digits){
	for (int i=0; i<10; i++){
		printf(digits[i] ? "1" : "0");
	}
	cout << ", " << SumDigits(digits) << endl;
}

void CheckDigits(int N, bool* digits){
	int d(0);
	while (N>0){
		d = N%10;
		digits[d] = true;
		N /= 10;
	}
	//PrintDigitsArr(digits);
}

