#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>
#include <queue>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		string s;
		int n;
		int ans = 0;
		cin >> s >> n;
		for(int b=0;b<s.size();b++){
			for(int e=b;e<s.size();e++){
				int max = 0;
				int temp = 0;
				//cout << s.substr(b,e-b+1) << endl;
				for(int i=b;i<=e;i++){
					if(s[i]=='a' ||
						s[i]=='i' ||
						s[i]=='u' ||
						s[i]=='e' ||
						s[i]=='o'){
							temp = 0;
					}else{
						temp++;
						if(temp>max)	max = temp;
					}
				}
				//cout << temp << endl;
				if(max>=n)	ans++;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}