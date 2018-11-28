#include <bits/stdc++.h>

using namespace std;

int n;
int p[50];
int total;
int main(){
	int t;
	cin >> t;
	for (int cn = 1; cn <= t; cn++){
		cin >> n;
		total = 0;
		for (int i = 0; i < n; i++){
			cin >> p[i];
			total +=  p[i];
		}
		printf("Case #%d: ", cn);
		while (total){
			int evac = 2;
			for(int i = 0; i < n && evac > 0; i++){
				if (p[i] > (total-1)/2){
					p[i]--;
					total--;
					evac--;
					printf("%c",i+'A');
				}
				if (p[i] > (total-1)/2 && evac > 0){
					p[i]--;
					total--;
					evac--;
					printf("%c",i+'A');
				}
			}
			if (evac != 0){
				int i;
				for (i = 0; p[i] <= 0; i++);
				p[i]--;
				total--;
				printf("%c", i+'A');
			}
			cout << " ";
		}
		if (cn != t)
			cout << endl;
	}
	return 0;
}