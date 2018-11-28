#include <bits/stdc++.h>

using namespace std;

int main() {
	
    int t;
    cin >> t;
    char x;

    int max_si;

	for(int it = 1; it <= t; it++){
		

		string a;
		// size - c0
		cin >> max_si;
		cin >> a;
		int solution = 0;
		int n = a.size();
		int total = 0, people = 0;
		for(int i = 0; i <= max_si; i++){
/*
			if((int)a[i] < (int)a[i+1]) {
				solution++;
			}
			a[i+1]+=a[i];
			a[i+1]-=('0');
			cout << a << endl;


			//if(a[i] == '0') solution++;
			solution = max_si;
			for(int i = 0; i < n-1 && solution >= 0; i++){
				solution -= ((int)(a[i] - '0'));
			}
*/


            if (total<i){
               people+=i-total;
                total=i;
            }
            x=a[i];
            total+= atoi(&x);


		}



		printf("Case #%d: %d\n", it, people);
		
	}
    
	return 0;
}