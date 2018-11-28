
/*
B name oooo
ID: amin_un1
PROG: ride
LANG: C++

my ID
uva = "sir sbu"
codforsec = "sir_sbu"
topcoder = "sir_sbu"
usaco = "amin_un1"
*/

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <cmath>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <bitset>
#include <complex>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <time.h>
using namespace std;

#define ll long long
#define ld long double

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int MAX = 100001;
const long long mod = 1000 * 1000 * 1000 + 7;

#define mp make_pair
#define pb(a) push_back(a)
#define L(s) (int)((s).size())
#define all(c) (c).begin(), (c).end()

#define INF (1e9)
#define EPS (1e-9)
#define E (2.718281828459045)


////////////////////////////////////////////////////code///////////////////////////////////////
int temp;
int n, j;
vector<int>vec[100]; 
string ans[100]; 


ll isPrime(ll num)
{
	for (int i = 2; i <= sqrt(num); i++){
		if (num % i == 0)
			return i;
	}
	return 0;
}
string toBinery(int num){
	string ans = "";
	for (int i = 0; i < n; i++)
		ans += "0"; 
	ans[0] = '1'; 
	ans[n - 1] = '1';
	int tempp = 1; 
	while (num){
		if (num % 2 == 1){
			ans[n - 1 - tempp] = '1';
		}
		tempp++;
		num /= 2;
	}
	return ans;
}
ll convert(ll base, string name){
	ll num = 0; 
	for (int i = 0; i < n; i++){
		num = base * num + (ll)(name[i] - 48);
	}
	return num;
}
void f()
{
	int count = j; 
	for (int i = 0; i < 100000; i++){
		if (count == 0)break;
		string name = toBinery(i);
		ll arr[10];
		bool can = true;
		for (int k = 2; k < 11; k++)
		{
			ll num = convert((ll)k, name);
			int curr = isPrime(num);
			if (curr == 0){
				can = false;
				break;
			}
			arr[k - 2] = curr;
		}
		if (can == true){
			count--;
			ans[j - count - 1] = name;
			for (int k = 0; k < 9; k++)
				vec[j - count - 1].push_back(arr[k]);
		}
	}
}



int main()
{
	ofstream cout("test2.out");
	ifstream cin("C-small-attempt0.in");
	cin >> temp;
	int tc = 0;
	while (temp--){
		cin >> n >> j;
		tc++;
		f();
		cout << "Case #" << tc << ": " << endl;
		for (int i = 0; i < j; i++){
			cout << ans[i];
			for (int k = 0; k < vec[i].size(); k++)
			{
				cout << " " << vec[i][k];
			}
			cout << endl;
		}
	}
	return 0;
}