#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

void splitArr(int arr[], int num){
	int temp = num, mod;
	while(temp > 0){
		mod = (temp%10);
		arr[mod] = 1;
		temp /= 10;
	}
}

int main(){
	//freopen("inputlarge.in","r",stdin);
    //freopen("outputlarge.out","w",stdout);
	int arr[10];
	int t,n, idx = 1;
	cin >> t;
	while(t--){
		cin >> n;
		int i;
		int cont;
		bool ok = false;
		memset(arr, 0, sizeof(arr));
		for(i = 1; i <= 200000; i++){
			splitArr(arr, n*i);
			cont = 0;
			for(int k = 0; k < 10; k++){
				if(arr[k] == 1) cont++;
			}
			if(cont == 10) break;
 		}
		if(cont == 10) cout << "Case #" << idx++ <<": " << n*i;
		else cout << "Case #" << idx++ <<": INSOMNIA";
		cout << "\n";
	}
	//fclose(stdin);
    //fclose(stdout);
	return 0;
}
