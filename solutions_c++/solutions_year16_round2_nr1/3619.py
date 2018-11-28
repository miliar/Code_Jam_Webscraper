#include <iostream>
using namespace std;
bool present(int alpha[], int i){
	string numbers[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR",
	"FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	int j, k, n;
	n = numbers[i].length();
	for(j = 0; j < n; j++)
		if(!alpha[numbers[i][j] - 'A'])
			break;
		else
			alpha[numbers[i][j] - 'A']--;
	if(j < n){
		for(int k = 0; k < j; k++)
			alpha[numbers[i][k] - 'A']++;
		return false;
	}
	return true;
}
void add(int alpha[], int digits[]){
	int a[] = {0, 2, 4, 1, 5, 6, 3, 7, 8, 9};
	for(int i = 0; i < 10; i++)
		while(present(alpha, a[i]))
			digits[a[i]]++;
}
int main() {
	int T, turn, i;
	string S;
	cin>>T;
	turn = 1;
	while(turn <= T){
		cin>>S;
		int digits[10] = {0}, alpha[26] = {0};
		for(i = 0; i < S.length(); i++)
			alpha[S[i] - 'A']++;
		add(alpha, digits);
		cout<<"Case #"<<turn++<<": ";
		for(i = 0; i < 10; i++)
			while(digits[i]--)
				cout<<i;
		cout<<endl;
	}
	return 0;
}
