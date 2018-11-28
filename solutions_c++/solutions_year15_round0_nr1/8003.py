#include <iostream>
#include <fstream>
#include <string> 
using namespace std;

int main(){
	ifstream fi;
	fi.open("A-large.in",ios::in);
	ofstream fo;
	fo.open("a.out",ios::out);
	int t;
	fi >> t;
	for (int i = 1; i <= t; i++){
		int j;
		fi >> j;
		int f[1002], s[1002];
		for (int k = 0; k <= j; k++){
			char x;
			fi >> x;
			s[k] = x - '0';
		}
		if (s[0] == 0){
			f[0] = 1;
		}
		else{
			f[0] = s[0];
		}
		int res = s[0];
		for (int k = 1; k <= j; k++){
			if (f[k-1]>=k){
				f[k] = f[k-1]+s[k];
			}
			else{
				f[k] = s[k]+k;
			}
			res += s[k];
		}
		res = f[j] - res;
		fo << "Case #" << i <<": " << res <<endl;
	}
	fi.close();
	fo.close();
	return 0;
}
