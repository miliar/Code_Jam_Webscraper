#include <bits/stdc++.h>
#define _USE_MATH_DEFINES
#define pb push_back
#define mp make_pair
#define ll long long
#define vi vector <int>
#define ii pair <int, int>
#define vii vector < ii >
#define vll vector <ll>
#define hash1 10000000000000061ll
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define AB(a) (-(a)<(a)?(a):-(a))
#define na(x) ((x)<P?(x):(x)-P)
#define X first
#define Y second
using namespace std;
//__________________________

int n, t, d, ans, a;
int mas [1001];
//_________________________________________

void rec(int i, int j){
	if(i == 0) return;
	if(mas[i] == 0){
		rec(i-1, j);
		return;
	}
	if(i == 9){
		ans = MI(ans, j + i);
		j += mas[i];
		mas[i/2] += mas[i];
		mas[i - i/2] += mas[i];
		rec(i-1,j);
		j += mas[i];
		mas[i/2] -= mas[i];
		mas[i - i/2] -= mas[i];
		mas[3] += 3 * mas[i];
		rec(i-1,j);
		return;
	}
	ans = MI(ans, j + i);
	j += mas[i];
	mas[i/2] += mas[i];
	mas[i - i/2] += mas[i];
	rec(i-1,j);
}

//_________________________________________
int main(){

	freopen("B-small-attempt2.in","r",stdin);
	//freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>t;
	for(int t1 = 1; t1 <= t; ++t1){
		for(int i = 0; i < 1001; i++)
			mas[i] = 0;

		ans = 0;

		scanf("%d", &d);
		for(int i = 0; i < d; i++){
			scanf("%d", &a);
			mas[a]++;
			ans = MA(ans, a);
		}
		rec (ans, 0);

		printf("Case #%d: %d\n", t1, ans);
	}

    return 0;
}
