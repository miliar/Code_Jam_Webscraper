#include<iostream>
#include<cmath>
#include<string>
#include<vector>
#include<algorithm>
#include<utility>
#include<memory.h>
#include<cstring>
#include<fstream>

using namespace std;

const long long MOD = 1e9 + 7;

const double eps = 1e-8;


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int q = 1; q <= T; q++){
		double C, F, X;
		cin >> C >> F >> X;
		double t = 0, s = 0, v = 2;
		while (s < X){
			if (X <= C){
				s = X;
				t = X / v;
			}
			else
			if (s < C){
				t += (C - s) / v;
				s = C;
			}
			else{
				if ((X - s) / v>(X - s + C) / (v + F)){
					s -= C;
					v += F;
				}
				else{
					t += (X - s) / v;
					s = X;
				}
			}
		}
		cout << "Case #" << q << ": ";
		printf("%.7lf\n", t);
	}
}