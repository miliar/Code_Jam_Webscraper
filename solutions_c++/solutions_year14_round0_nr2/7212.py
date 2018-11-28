#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstring>
#include <iterator>
#include <map>
#include <bitset>
#include <queue>

using namespace std;

#define inf 200000000
#define neginf -20000000
#define PB push_back
#define pb pop_back
#define MK make_pair

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef long long ll;
typedef vector<vi> vvi;
typedef vector<ii> vii;

double c, f, x;

int main(){
int T; scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
		scanf("%lf %lf %lf", &c, &f, &x);
		
		printf("Case #%d: ", t);
		
		double prevR = 2.0;
		double prevT = x / prevR;
		double newT, newR;
		double intermediate = 0.0;
		
		bool flag;
		do{
			flag = false;
			newR = prevR + f;
			intermediate += (c /prevR);
			newT = intermediate + (x / newR);
			
			if(newT < prevT){
				prevR = newR;
				prevT = newT;
				flag = true;
			}
			
		}while(flag);
		
		printf("%0.7lf\n", prevT);

	}
return 0;
}
