#include<iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>
#include<memory.h>
#include <cmath>

#define FOR(i,s,e) for(int i=s;i<e;i++)
#define PII pair<int,int>

using namespace std;

int main() {
	int t,fa,sa,x = 1;
	int a[4][4],b[4][4];
	cin >> t;
	while( t ){
		cin >> fa;
		FOR(i,0,4){
			FOR(j,0,4) cin >> a[i][j];
		}
		cin >> sa;
		FOR(i,0,4){
			FOR(j,0,4) cin >> b[i][j];
		}
		
		int c = 0, flag, ans;
		FOR(i,0,4){
			flag = 0;
			///cout << "alan inam " << a[fa][i] <<"\n";
			FOR(j,0,4){
				//cout << "ba in " << b[sa][j] <<"\n";	
				if( a[fa-1][i] == b[sa-1][j] ){
					ans = a[fa-1][i];
					flag = 1;
					//cout << i << " "<<j << " "<<ans<<"\n";
					
				}
			}
			//system("pause");
			if( flag == 1 ){
				c++;
				
			}
		}
		cout << "Case #" << x <<": ";
		if( c == 0){
			cout << "Volunteer cheated!";
		}else if( c == 1){
			cout << ans;
		}else  {
			cout << "Bad magician!";
		}
		cout << "\n";
		x++;
		t--;
	}
	
    return 0;
}
