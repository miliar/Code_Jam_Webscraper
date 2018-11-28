#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<set>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<sstream>
#include <stdio.h>

using namespace std;

int n, test , A , B;
bool p[2000];

bool checkpalin(int i) {
	ostringstream os;
	os<<i;
	string s = os.str();
	int left = 0; int right = s.length() - 1;
	while(left < right) {
		if (s[left] != s[right]) {
			return false;
		}
		left++; right--;
	}
	return true;
}

int solve() {
	
	for(int i = 1 ; i <= 1001; i++) {
		p[i] = false;
		p[i] = checkpalin(i);
	}
	
	int res = 0;
	
	for(int i = A; i<=B ; i++) {
		if (p[i]) {
			int j = int(sqrt(i) + 0.001);
			if (j * j == i && p[j]) {
				res++;
			}
		}
	}
	
	return res;
}

int main(){
    cin>>test;
    string a;
	n = 4;
    for(int t = 1;t<=test;t++){
        cin>>A>>B;
        cout<<"Case #"<<t<<": ";
        cout<<solve();
        if (t < test) {
        	cout<<endl;
        }
    }               
}
