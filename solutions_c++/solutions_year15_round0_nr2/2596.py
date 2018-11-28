#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <time.h>
#include <map>
using namespace std;
const int INF = 1e9;
map<multiset<int>, int> f;

int calc(multiset<int> ans){

	if (f.count(ans) != 0){
		return f[ans];
	}
	if (ans.empty())
		return 0;
	
	//for (multiset<int>::iterator it = ans.begin(); it != ans.end(); it++){
	//	cout << *it << " ";
	//}
	//cout << endl;

	int ans1 = *ans.rbegin();

	multiset<int> ans2 = ans;

	for (multiset<int>::iterator it = ans.begin(); it != ans.end(); it++){
		
		if (*it < 2) continue;

		int was = *it;

		ans2.erase(ans2.find(was));

		int will1 = 0;
		int will2 = *it;
		for (int j = 0; j < *it / 2; j++){
			will1++;
			will2--; 
			if (will1 > 0)
				ans2.insert(will1);
			if (will2 > 0)
				ans2.insert(will2);

			ans1 = min(ans1, 1 + calc(ans2));

			ans2.erase(ans2.find(will1));
			ans2.erase(ans2.find(will2));

		}
		
		ans2.insert(was);
		
	}
	f[ans] = ans1;

	return ans1;
}

int solve3(vector<int> a){
	multiset<int>b;
	for (int i = 0; i < a.size(); i++)
		b.insert(a[i]);
	return calc(b);
}

int solve1(vector<int> a){
	int ans = INF;
	int already = 0;

	for (;;){
		sort(a.rbegin(), a.rend());
		//for (int i = 0; i < a.size(); i++)
		//	cout << a[i] << " ";
		//cout << endl;
		int can = a[0];
		ans = min(ans, already + can);
		int j = 1;
		while (j < a.size() && a[j] == can){
			j++;
		}
		int r = 0;
		if (j < a.size()) r = a[j];

		int nr1 = can / 2;
		int nr2 = can - nr1;
		r = max(nr1, r);
		r = max(nr2, r);

		//if (r + j > can){
		//	break;
		//}
		if (can < 2) {
			break;
		}


		for (int k = 0; k < j; k++){
			a[k] = nr1;
			a.push_back(nr2);
		}
		already += j;

	}
	return ans;
}


int solve2(vector<int> a){
	int ans = INF;
	int already = 0;

	for (;;){
		sort(a.rbegin(), a.rend());
		int can = a[0];
		ans = min(ans, already + can);

		if (can % 2 != 0){
			for (int j = 0; j < a.size(); j++)
				a[j]--;
			already++;
			continue;
		}

		int j = 1;
		while (j < a.size() && a[j] == can){
			j++;
		}
		int r = 0;
		if (j < a.size()) r = a[j];

		int nr1 = can / 2;
		int nr2 = can - nr1;
		r = max(nr1, r);
		r = max(nr2, r);


		if (r + j > can){
			break;
		}


		for (int k = 0; k < j; k++){
			a[k] = nr1;
			a.push_back(nr2);
		}
		already += j;

	}
	return ans;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++){
		int t;
		scanf("%d", &t);
		vector<int> a(t);
		for (int j = 0; j < a.size(); j++){
			scanf("%d", &a[j]);
		}
		
		printf("Case #%d: %d\n", i, solve3(a));
	}
	return 0;
}
