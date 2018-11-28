#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<stack>
#include<deque>
#include<queue>
#include<string>
#include<math.h>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
#include<map>
#include<set>
#include<iomanip>
#include<cmath>
#include<cstdio>
#include<time.h>
#include<random>

#define pb push_back
#define endl '\n'
#define vvi vector<vector<int> >
#define str string
#define vi vector<int>
#define vs vector<string>
#define vll vector<long long>
#define ll long long
#define mp make_pair
#define ld long double
#define itn int 
#define vvll vector<vector<long long> >


const clock_t tl = 0.9 * CLOCKS_PER_SEC;
double start;
ll p = 307, mod = 99999989;//999999937;
#pragma comment(linker, "/STACK:25600000")
using namespace std;
struct qu{
	int x0, x1, y0, y1;
};
bool operator < (qu a, qu b){
	if(a.x0 == b.x0){
		return a.y0 < b.y0;
	}
	return a.x0 < b.x0;
}

int main(){
	//freopen("road.in", "r", stdin);
	//freopen("road.out", "w", stdout);
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int q = 0; q < t; q++){
		ld c, f, x, p=2;
		cin >> c >> f >> x;
		ld t=0;
		while(x/p > c/p + x/(p+f)){
			t += c/p;
			p += f;
		}
		cout << "Case #"<<q+1<<": ";
		cout <<fixed<<setprecision(7)<< t + x/p;
		cout << endl;
	}
	return 0;
}