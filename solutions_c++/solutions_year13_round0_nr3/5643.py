#include<cstdio>
#include<string>
#include<cmath>
#include<iostream>
using namespace std;

int check(int a){
	int x = 0;
	while((int)(a / pow(10, x)) != 0){
		x++;
	}
	for(int i = 0; i < x / 2; i ++){
		if(a % (int)pow(10, i+1) != a / (int)pow(10, x-1) % 10)
			return 0;
	}	
	return 1;

}


int main(){
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++){
		int min, max;
		cin >> min >> max;
		int count = 0;
		for(int j = 1; j <= sqrt(max); j++){
			if(check(j) && j*j >= min && check(j*j))
				count++;
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
}
