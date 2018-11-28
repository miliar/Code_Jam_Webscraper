#include <cstdio>
#include <iostream>
#include <sstream>

using namespace std;



int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int i, t, j, cant;
	cin >> t;
	//scanf("%d", &t);
	string s;
	bool empiezaConSum;
	for(i = 1; i <= t; i++){
		cin >> s;
		if(s[0] == '+'){
			empiezaConSum = true;
		}else{
			empiezaConSum = false;
		}
		cant = 1;
		for(j = 1; j < s.size(); j++) {
			if(s[j - 1] != s[j]){
				cant++;
			}
		}
		if(empiezaConSum){
			if(cant % 2 == 0){
				cout << "Case #" << i << ": " << cant << endl; 
			}else{
				cout << "Case #" << i << ": " << (cant - 1) << endl; 
			}
		}else{
			if(cant % 2 != 0){
				cout << "Case #" << i << ": " << cant << endl; 
			}else{
				cout << "Case #" << i << ": " << (cant - 1) << endl; 
			}
		}
		//printf("Case #%d: \n", i);
		

		
		
	}

	return 0;
}