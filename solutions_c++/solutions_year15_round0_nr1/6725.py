#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int max(int a, int b){
	if(a > b) return a;
	return b;
}

int min(int a, int b){
	if(a < b) return a;
	return b;
}

int main(){

	char pessoas[2000];

	int n, t, size, s, friends;
	char lixo;

	cin >> n;

	for(int i = 0; i < n; i++){

		printf("Case #%d: ", i+1);

		scanf("%d %s", &t, pessoas);

		friends = 0;
		s = pessoas[0] - '0';
		size = strlen(pessoas);

		for(int j = 1; j < size; j++){

			if(pessoas[j] - '0' > 0){
				if(s < j){
					friends += j-s;
					s += j-s;
				}

				s += pessoas[j] - '0';
			}
		}

		cout << friends << endl;

	}

	return 0;

}
