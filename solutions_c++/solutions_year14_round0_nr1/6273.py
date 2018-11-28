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
		set<int> s1, s2, s3;
		int k;
		cin >> k;
		int arr[4][4];
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> arr[i][j];
			}
		}
		for(int i = 0; i < 4; i++){
			s1.insert(arr[k-1][i]);
		}
		cin >> k;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> arr[i][j];
			}
		}
		for(int i = 0; i < 4; i++){
			s2.insert(arr[k-1][i]);
		}
		for(set<int>::iterator it = s1.begin(); it != s1.end(); it++){
			if(s2.find(*it) != s2.end()){
				s3.insert(*it);
			}
		}
		cout << "Case #"<<q+1<<": ";
		if(s3.size() == 0){
			cout << "Volunteer cheated!";
		}
		if(s3.size() == 1){
			cout << *s3.begin();
		}
		if(s3.size() > 1){
			cout << "Bad magician!";
		}
		cout << endl;
	}
	return 0;
}