#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;
typedef long long LL;
#define F(l,n) for (int l = 0; l < (int)(n); l++)
main(){

	FILE *fin = freopen("B-large.in", "r", stdin);
	assert (fin != NULL);
	
	FILE *fout = freopen("B-large.out", "w", stdout);
	
	int T, n, i, cnt, j;
	string ss;
	vector<char> s;
	
	cin >> T;

	for(int t = 1; t <= T; t++){
		cin >> ss;

		n = ss.length();
		F(k,n){
			s.push_back(ss.at(k));
			//cout << s[k] << ' ';
		}
		//cout << endl;
		i = n-1;
		j = 0;
		cnt = 0;
		while (true){
			while (i >= 0 && s[i] == '+'){

				i--;

				

			}
			if (i < 0){
	
				cout << "Case #" << t << ": ";
				cout << cnt << endl;
				
				break;
			}
			j = 0;
			if (s[j] == '+')
				cnt++;
			while (s[j] == '+'){
				s[j] = '-';
				j++;
			}
			F(c,i+1){
				if(s[c] == '-')
					s[c] = '+';
				else
					s[c] = '-';
			}
			cnt++;


		
			
		}
		s.clear();
	
			

		//cout << "Case #" << t << ": ";
		//cout << cnt << endl;
	
	}
	exit(0);
}
