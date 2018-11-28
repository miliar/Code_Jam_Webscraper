#include <stdio.h>
#include <fstream>
#include <vector>
#include <iostream>
using namespace std;


int main() {
	int nTest;
	ifstream cin("input.txt");
	cin>>nTest;
	for(int k=1; k<=nTest; k++){
		int n, count=0, need=0;
		cin>>n;
		string s; cin>>s;
		for(int i=0; i<s.size(); i++){
			if(count < i ){
				need += i-count;
				count+=i-count;
			}
			count += s[i]-'0';
		}
		printf("Case #%d: %d\n", k, need );
	}
}
