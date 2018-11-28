#include <iostream>
#include <cstdio>
using namespace std;

int a[10][10] , b[10][10];

int main(){
    int t , cs = 0 , ans , i , j , n1 , n2 , cnt;
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    cin >> t;
    while(t--){
	cnt = 0; ans = 0;
	cin >> n1; n1--;
	for(i = 0; i < 4; i++)
	    for(j = 0; j < 4; j++)
		cin >> a[i][j];

	cin >> n2; n2--;
	for(i = 0; i < 4; i++)
	    for(j = 0; j < 4; j++)
		cin >> b[i][j];

	for(i = 0; i < 4; i++){
	    for(j = 0; j < 4; j++)
		if(a[n1][i] == b[n2][j]) {ans = a[n1][i];cnt++;}
	}
	if(!cnt) cout << "Case #" << ++cs << ": " <<"Volunteer cheated!" << endl;
	if(cnt > 1) cout << "Case #" << ++cs << ": " << "Bad magician!" << endl;
	if(cnt == 1) cout << "Case #" << ++cs << ": " << ans << endl;
    }
    return 0;
}
