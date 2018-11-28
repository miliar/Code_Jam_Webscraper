#include<vector>
#include<cmath>
#include<complex>
#include<iostream>
#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<float.h>
#include<set>
#include<map>
#include<queue>
#include<math.h>
#include<algorithm>
using namespace std;


typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

#define pb push_back
#define mp make_pair
#define snd second
#define fst first
#define debug printf("--%d--\n",__LINE__)
#define ll long long int

int casenum;
int main(void){
	cin >> casenum;
	for(int i=0;i<casenum;i++){
		string s;
		cin >> s;
		int n = s.size();
		
		char now = '*';
		int cnt = 0;
		for(int j=0;j<n;j++){
			if (now != s[j]){
				cnt++; now = s[j];
			}
		}
		if (now == '+') cnt--;
		cout << "Case #" << i+1 << ": " << cnt << endl;
	}
	
	
	
	return 0;
}
