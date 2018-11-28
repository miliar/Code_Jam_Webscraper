#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);cin.tie(NULL);

    ifstream cin("large.in");
    ofstream cout("a.out");

	int TC, t, rta, i, j, k;
	string s;
	bool flag;
	
	cin >> TC;
	t = 1;
	
	while( t <= TC ){
		cin >> s >> k;
		
		rta = 0;
		flag = true;
		
		for( i = 0; i < s.size(); i++ ){
			if( s[i] == '-'){
				if( s.size() - i >= k ){
					for( j = 0; j < k; j++ ){
						s[i + j] = s[i + j] == '-' ? '+' : '-';
					}
					rta++;
				}else{
					flag = false;
					break;
				}
			}
		}
		
		cout << "Case #" << t << ": ";
		if(flag){
			cout << rta << "\n";
		}else{
			cout << "IMPOSSIBLE\n";
		}
		
		t++;
	}
	
	return 0;
}