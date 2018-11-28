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
	for(int casecnt=0;casecnt<casenum;casecnt++){
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << casecnt+1 << ":";
		long long int n = 1;
		for(int i=0;i<c;i++) n *= k;
		for(int i=0;i<k;i++){
			long long int m = 0;
			for(int j=0;j<c;j++){
				m = m * k + (i+1)%k;
			}
			cout << " " << m+1;
		}
		cout << endl;
	}
	
	
	
	
	
	return 0;
}
