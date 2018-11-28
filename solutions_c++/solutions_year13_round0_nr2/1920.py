#include<vector>
#include<cmath>
#include<complex>
#include<iostream>
#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<float.h>
#include<map>
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

int T;
int N, M;
int a[128][128];

int maxi[128],maxj[128];

int main(void){
	cin >> T;
	for(int cn=1;cn<=T;cn++){
		cin >> N >> M;
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				cin >> a[i][j];
			}
		}
		
		for(int i=0;i<N;i++){
			maxi[i] = 0;
			for(int j=0;j<M;j++){
				if (maxi[i] < a[i][j]) maxi[i] = a[i][j];
			}
		}
		for(int j=0;j<M;j++){
			maxj[j] = 0;
			for(int i=0;i<N;i++){
				if (maxj[j] < a[i][j]) maxj[j] = a[i][j];
			}
		}
		
		bool ans = true;
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				if (a[i][j]!=maxi[i] && a[i][j]!=maxj[j]){
					ans = false;break;
				}
			}
			if (!ans) break;
		}
		
		cout << "Case #" << cn << ": " << (ans ? "YES" : "NO") << endl;
		
		
	}
	
	
	
	
	
	return 0;
}
