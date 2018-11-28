using namespace std;
#include <iostream>
#define SIZE 10

void setAllZero(int []);

int main(){
	int n,countDigit = 0,num;
	int digit,ten[SIZE] = {},tmp,tmp2;
	cin >> n;
	for (int count = 1 ; count <= n ; count++){
		cin >> num;
		tmp = num;
		for (int i = 1; i <= 100 && countDigit < 10; ++i)
		{
			tmp2 = num*i;
			tmp = num*i;
			if (tmp == 0){
				if (ten[0] < 1){
					ten[0]++;
					countDigit++;
				}
			}
			while( tmp != 0 ){
				digit = tmp % 10;
				if (ten[digit] < 1){
					ten[digit]++;
					countDigit++;
				}
				tmp /= 10;
			}
		}
		cout << "Case #" << count << ": ";
		countDigit == 10 ? cout << tmp2 : cout << "INSOMNIA";
		cout << endl;
		countDigit = 0;
		setAllZero(ten);

	}
	return 0;
}

void setAllZero(int arr[]){
	for (int i = 0; i < SIZE; i++)
	{
		arr[i] = 0;
	}
}
