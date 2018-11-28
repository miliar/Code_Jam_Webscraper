#include <bits/stdc++.h>
using namespace std;

#define INTMAX ((int) 1E9 + 10)
#define valueOfA ((int) 'A')
#define rint(x) scanf("%d", &(x))
#define pint(x) printf("%d\n", (x))
#define rchar(x) scanf("%c", &(x))
#define pchar(x) printf("%c\n", (x))
#define rstring(x) scanf("%s", &(x))
#define pstring(x) printf("%s\n", (x))
#define mp make_pair

typedef pair<int, int> edge;

int T, sMax;
int people [1001];

int main(){
	freopen("A.txt", "w", stdout);
	rint(T);
	for (int a = 1; a <= T; a++){
		rint(sMax);
		char shyValues [sMax+1];
		int totalClapped = 0, friendsAdded = 0;
		rstring(shyValues);

		for (int b = 0; b <= sMax; b++){
			people[b] = shyValues[b] - '0';
		}

		// for (int b = 0; b <= sMax; b++){
		// 	cout << people[b];
		// }
		// cout << endl;

		for (int b = 0; b <= sMax; b++){
			if (totalClapped < b && people[b] != 0){
				friendsAdded += b-totalClapped;
				totalClapped += friendsAdded;
			}

			totalClapped += people[b];
		}

		cout << "Case #" << a << ": " << friendsAdded << endl;
	}
}