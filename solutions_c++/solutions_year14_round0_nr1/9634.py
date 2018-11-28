#include<iostream>
#include<list>
#include<cstdio>
#include<cmath>
#include<numeric>
#include<utility>
#include<list>
#include<set>
#include<map>
#include<bitset>
#include<vector>
#include<algorithm>
#include<bitset>
#include <deque>
#include<limits>
#include<string>
#include<cstring>
#include<cctype>
#include<iomanip>
#include<sstream>
#include<fstream>

using namespace std;

int main(){
	unsigned int T;
	cin >> T;

	for(int t = 1; t <= T; t++){
        int ans1 = 0; 
        cin >> ans1;

        map <int, int> check;

        int num = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin >> num;
                if(i == ans1-1) check[num]++; 
            }
        }
            
        int ans2 = 0; bool justone = false, badmagic = false;
        int ans = 0;
        cin >> ans2;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin >> num;
                if(i == ans2-1){
                    if(check[num] && !ans){ ans = num; justone = true; }
                    else if(check[num] && ans){ badmagic = true; justone = false; }
                }
            }
        }
        cout << "Case #" << t << ": " << flush;
        if(justone) cout << ans << endl;
        else if(badmagic) cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
	}
	return 0;
}
