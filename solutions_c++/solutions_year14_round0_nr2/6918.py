#include <iostream>
#include <vector>
#include <string>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#define infin 2147483647
#define LLinfin 9223372036854775807
#define pb push_back
#define rs resize
#define mp make_pair
#define sz(x) int((x).size())
#define VV(x) vector<vector<x> >
#define all(x) (x).begin(), (x).end()
using namespace std;
typedef pair<int, int> PII;
typedef long long LL;

int main(){
	int tests, farms;
	double c, f, x, latestans, nowstart, nowans, buytime;
	cin>>tests;
	for(int t=1; t<=tests; t++){
		cin>>c>>f>>x;
		nowstart = nowans = 0, latestans = 1000000.0;
		for(farms = 0; true; farms++){
			nowans = nowstart + x/(2 + farms * f);
			// cout<<nowans<<' '<<nowstart<<endl;
			if(nowans >= latestans){
				break;
			}
			latestans = nowans;
			buytime = c/(2 + farms * f);
			nowstart += buytime;
			if(nowstart >= x){
				break;
			}
		}
		printf("Case #%d: %.7f\n", t, latestans);
	}
}