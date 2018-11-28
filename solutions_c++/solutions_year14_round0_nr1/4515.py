/*************************************************************************
Author: zjut_polym
Created Time:   2014/4/12 21:24:39
File Name: A.cpp
************************************************************************/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>
#include <queue>
using namespace std;


//----------------------[ZJUT-polym for div2]-------------------------------------
#define ll long long
#define MOD 1000000007
#define PII pair<int, int>
#define ff first
#define ss second
#define sz(v) (int)v.size()
#define _mst(buf, val) memset(buf, val, sizeof(buf))
#define rep(i, l, r) for(i = (l); i <= (r); i++)
#define srep(i, l, r) for(i = (l); i >= (r); i--)
#define repi(it, c) for(typeof(c.begin())it = c.begin(); it != c.end(); it++)
#define inf 0x3f3f3f3f
#define N 100005
#define eps 1e-8
#define pi (2.0 * acos(0.0))
//--------------------------------------------------------------------------------

int a[2][4];
int main() {
	int T, n, val, cas = 1;
	cin >> T;
	while(T--){
		for(int k = 0; k < 2; k++){
			cin >> n;
			for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){
					cin >> val;
					if(i == n - 1) a[k][j] = val;
				}
			}
		}
		int num = 0;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(a[0][i] == a[1][j]) {num++; val=a[1][j];}
			}
		}
		printf("Case #%d: ", cas++);
		if(num == 0){
			cout << "Volunteer cheated!" << endl;
		}
		else{
			if(num == 1){
				cout << val << endl;
			}
			else{
				cout << "Bad magician!" << endl;
			}
		}
	}
		
		
    return 0;
}

