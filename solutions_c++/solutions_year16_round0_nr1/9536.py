#include <cstdio>
#include <iostream>
using namespace std;
typedef long long ll;

int T;
ll cases[110];
void input(){
	freopen("counting.in", "r", stdin);
	fscanf(stdin, "%d", &T);
	for (int i = 0; i < T; i++){
		ll a;
		fscanf(stdin, "%lld", &a);
		cases[i] = a;
		
	}
}


int main(){
	freopen("counting.out", "w", stdout);
	
	input();
	for (int i = 0; i < T; i++){
		bool seen[10];
		for (int j = 0; j < 10; j++){
			seen[j] = false;
		}
		int counter = 10;
		//cout << cases[i] << endl;
		ll curr = cases[i];
		ll start = curr;

		if (curr == 0){
			fprintf(stdout, "Case #%d: %s\n", i+1, "INSOMNIA");
			continue;
		}

		while (counter > 0){
			ll temp = curr;
			int digit;
			while (temp > 0){
				digit = temp%10;
				if (seen[digit] == false){
					counter--;
					seen[digit] = true;
				}
				temp = temp/10;
				//cout << temp << endl;
			}
			//break;
			//cout << curr << endl;
			curr += start;	
		}

		
		fprintf(stdout, "Case #%d: %lld\n" , i+1, curr-start);
	}

}