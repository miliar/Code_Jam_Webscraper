#include<iostream>
using namespace std;

int main() {
	char a[11] = {0};
	char s[128];
	int t, n, k;
	cin >> t;
	for(int i = 0; i < t; i++){
		int j;
		for(int k = 0; k < 10; k++)
			a[k]=0;
		j=0;
		cin >> n;
		if(n == 0){
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << '\n';
			continue;
		}
		while(1){
			j++;
			k = n * j;
			sprintf(s, "%d", k);
			for(int i = 0; i < 10; i++){
				char c=i+48;
				if(strchr(s, c) != NULL){
					a[i] = c;
				}
			}
			if(strcmp(a, "0123456789") == 0){
				cout << "Case #" << i+1 << ": " << k << '\n';
				break;
			}
		}
	}
	return 0;
}