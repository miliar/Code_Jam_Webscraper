#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <map>
#include <iomanip>
#define pb push_back
#define mp make_pair
using namespace std;
//--------------------
int mas1 [5][5], mas2 [5][5];
int a,b,c,t, ans;

//--------------------
int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &t);
	for(int t1 = 1; t1 <= t; ++t1){
		ans = 0;
		cout<<"Case #"<<t1<<": ";
		scanf("%d", &a);
		for(int i = 1; i < 5; ++i){
			for(int j = 1; j < 5; j++){
				scanf("%d", &mas1[i][j]);
			}
		}
		scanf("%d", &b);
		for(int i = 1; i < 5; ++i){
			for(int j = 1; j < 5; j++){
				scanf("%d", &mas2[i][j]);
			}
		}

		for(int i = 1; i < 5; i++){
			for(int j = 1; j < 5; j++){
				if(mas1[a][i] == mas2[b][j]){
					ans++;
					c = mas1[a][i];
				}
			}
		}

		if(ans == 1){
			cout<<c<<endl;
		}else if(ans > 1) cout<<"Bad magician!"<<endl;
				else cout<<"Volunteer cheated!"<<endl;

	}

	return 0;
}