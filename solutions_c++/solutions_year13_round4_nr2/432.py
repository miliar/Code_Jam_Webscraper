#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>

using namespace std;


#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define y1 y1_gedjcdgfce
#define y0 y0_sadasdasdsa
#define ws ws_sadsadsada
#define left left_asdsadsadsadsa
#define right right_asdasdsadasda
#define hash hash_asdasdasdsad

#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}


int get0(int ind, int size, int place) {
	if (size <= place) return 1;
	if (place <= 0) return 0;
	if (ind == 0) return place >= 0;
	return get0((ind - 1)/ 2, size / 2, place - size / 2);
}

int get1(int ind, int size, int place) {
	if (size <= place) return 1;
	if (place <= 0) return 0;
	if (ind == size - 1) return place >= size;
   	return get1((ind + 1)/ 2, size / 2, place);	

}
int solve(int test) {
	int n, p;
	scanf("%d%d", &n, &p);
	int res0 = 0;
	int res1 = 0;
	for (int i = 0; i < (1 << n); i++) {
		if (get0(i, 1 << n, p)) res0 = i;
		if (get1(i, 1 << n, p)) res1 = i;
	}
	printf("Case #%d: %d %d\n", test, res0, res1);
}
int main(){
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		solve(test);
	}
	return 0;
}
