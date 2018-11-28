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
#include<sstream>
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


vi flg(10);
int n;


bool check(int a){
	stringstream ss;
	ss << a;
	string s = ss.str();
	//cout << s << endl;
	for(int i=0;i<s.size();i++){
		flg[s[i] - '0'] = 1;
	}
	for(int i=0;i<10;i++){
		if (!flg[i]) return false;
	}
	return true;
}

int main(void){
	cin >> n;
	for(int i=0;i<n;i++){
		int m;
		cin >> m;
		for(int j=0;j<10;j++){
			flg[j] = 0;
		}
		
		cout << "Case #" << i+1 << ": ";
		if (m==0){
			cout << "INSOMNIA" << endl;
			continue;
		}
		for(int j=1;;j++){
			if (check(j*m)){
				cout << j*m << endl;
				break;
			}
		}
		
		
	}
	
	
	
	return 0;
}
