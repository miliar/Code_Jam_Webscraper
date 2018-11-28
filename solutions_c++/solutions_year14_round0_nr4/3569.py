#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <vector>
#include <queue>
using namespace std;

typedef vector<int> voi;
typedef set<int> soi;
typedef vector<voi> vooi;
typedef pair<int, int> pii;

#define FOR(i, a, b) for(i=(a); i < (b); ++i)
#define REPEAT(i, n) FOR(i, 0, n)

#define	 EPS 1E-10

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//ios_base::sync_with_stdio(false);
	
	int T, N;
	scanf("%d", &T);
	
//	scanf("%F %F %F", &C, &F, &X);

	double temp;
	int i,j,k;
	int ans;
	bool answer = false;
	vector<double> Naomi, Kendzi,Back;
	Naomi.reserve(50); Kendzi.reserve(50); Back.reserve(50);
	for (k=1; k<= T; ++k){
		Naomi.clear(); Kendzi.clear();
		scanf("%d", &N);
		printf("Case #%d: ", k);//\n
		for (j=0; j < N; ++j){
			cin >> temp;
			Naomi.push_back(temp);
		}
		for (j=0; j < N; ++j){
			cin >> temp;
			Kendzi.push_back(temp);
		}
		sort(Naomi.begin(),  Naomi.end());
		sort(Kendzi.begin(), Kendzi.end());
		/*
		//for (j=0; j< N; ++j){
		for (j= 0; j< N; ++j){
			cout << Naomi[j] << " ";
		}
		cout << endl;
		for (j= 0; j< N; ++j){
			cout << Kendzi[j] << " ";
		}
		cout << endl;*/
		//}]
		/*
		j=0;
		while((j < N)){
			if (Naomi[j] < Kendzi[N - j - 1]){
				++j;
			}
			else{
					break;
			}

		}*/
		Back = Kendzi;
		ans = 0;
		for (i = 0; i < N; ++i) {
	        for (j = 0; j < N; ++j)
				if (Naomi[i] > Kendzi[j]) {
	                ++ans;
					Kendzi[j] = 10;
					break;
				}
		}
		Kendzi.swap(Back);

		//ans = N - j;
		cout << ans ;

		ans = 0;
	for (i = 0; i < N; ++i) {
		answer = false;
        for (j = 0; j < N; ++j){
            if (Naomi[i] < Kendzi[j]) {
                Kendzi[j] = -1;
                answer = true;
                break;
            }
		}
        if (!answer) ++ans;
    }
	cout << " " << ans << endl;






	}
	
	return 0;
}
