#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <queue>
#include <bitset>
using namespace std;

typedef vector<int> voi;
typedef set<int> soi;
typedef vector<voi> vooi;
typedef pair<int, int> pii;
typedef vector< bitset<150> > vb;
typedef vector<  set< int > >  vosi;
typedef vector<  string >  vos;
typedef vector<  pair<char, int> >  vopci;

#define FOR(i, a, b) for(i=(a); i < (b); ++i)
#define REPEAT(i, n) FOR(i, 0, n)

#define ABS(x) (((x) < 0) ? (-(x)) : (x))


/*
inline int round(double x){
	if (fabs(x - int(x)) > 0.5){
		return int(x)+1;
	}else return int(x);

}*/

int main(){
	freopen("in.txt", "r", stdin);
	freopen("ou.txt", "w", stdout);
	//ios_base::sync_with_stdio(false);
	int T;
	
	scanf("%d", &T);
	int i;
	int l;
	int N;
	int id;
	vos a;
	a.reserve(100);

	//vopci c;
	//c.reserve(10000);
	string c;
	string s;
	vector<int> current_positions;
	vector<int> current;
	int j,k,m;
	int sum;
	int current_large;
	bool out = false;;
	int medium;
	for (l=1; l<= T;++l){
		c.clear();	
		out = false;
		scanf("%d", &N);
		a.clear();
		sum = 0;
		current_positions.assign(N, 0);//позиция в строке
		current.assign(N, 0);//число данных элементов
		for (i=0; i<N; ++i){
			cin >> s;
			a.push_back(s);
		}
		//c.push_back(make_pair(a[0][0], 1));
		c.push_back(a[0][0]);
		//id = 1;
		for (i=1; i<a[0].size(); ++i){
			if (c.back() != a[0][i]){
				c.push_back(a[0][i]);
			}
		}
		
		for (i=0; i<c.size(); ++i){
			current.assign(N, 0);//число данных элементов
			if (out)break;
			current_large = 0;
			for (j=0; j< N;  ++j){
				while(( current_positions[j] <  a[j].size()) && (a[j][current_positions[j]] == c[i])){
					++current_positions[j];
					++current_large;
					++current[j];
				}
				if (current[j] == 0){
					printf("Case #%d: Fegla Won\n", l);
					out = true;
					break;
				}
			}
			
			current_large = round(((double)current_large) / N);
			for (j=0; j< N;  ++j){
				sum += abs(current[j] - current_large);
			}
		}
		if (out)continue;
		for (j=0; j< N;  ++j){
				if (current_positions[j]  !=  a[j].size()){
					printf("Case #%d: Fegla Won\n", l);
					out = true;
					break;
				}
			}
			if (out)continue;
		printf("Case #%d: %d\n", l, sum);
	}


		
	return 0;
}
