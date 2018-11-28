#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int N;
double a[10000], b[10000];
int solve1(){
	int j = N-1, res = 0;
	for (int i = N-1; i >= 0; i--){
		for (; j >= 0; j--){
			if (a[i]>b[j]){
				res++;
				j--;
				break;
			}
		}
	}
	return res;
}
int solve2(){
	int i = N - 1, j = N - 1, res = 0;
	for (; i >= 0; i --){
		if (a[i] > b[j])res++;
		else j--;
		if (j < 0)break;
	}
	return res;
}
int main() {
	freopen("out.txt", "w", stdout);
	freopen("in.txt", "r", stdin);
	int tc, t = 1;
	cin >> tc;
	while (tc--){
		cin >> N;
		for (int i = 0; i < N; i++)cin >> a[i];
		for (int i = 0; i < N; i++)cin >> b[i];
		sort(a, a + N);
		sort(b, b + N);
		cout << "Case #" << t++ << ": " <<solve1() << " " << solve2() << endl;
	}

}

