#include <iostream>
#include <string>
#include <cmath>
#include <conio.h>
using namespace std;

bool pal(int x){
	int temp = x;
	int y = 0;
	while(x){
		y *= 10;
		y += x % 10;
		x /= 10;
	};
	return temp == y;
}

void main(){
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	int T;
	cin>>T;
	for(int tc=1; tc<=T; tc++){
		int a, b;
		cin >> a >> b;
		if(a > b) swap(a,b);
		int cnt = 0;
		for(int i=a; i<=b; i++){
			if(pal(i)){
				int j = sqrt((double)(i));
				if(i == j*j && pal(j)) cnt++;
			}
		}
		//010 --> 10

		cout << "Case #" << tc << ": " << cnt << endl;
	}
	getch();
}
/*
3
 1 4
 10 120
 100 1000

Case #1: 2
Case #2: 0
Case #3: 2
*/