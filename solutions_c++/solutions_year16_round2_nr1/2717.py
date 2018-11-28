#include <iostream>
#include <string>
#include <stdio.h>
#include <cmath>
#include <bitset>
#include <cstdlib>

using namespace std;
int main(int argc, char* argv[]) {

	int t;
	int n;
	int j;
	cin >> t;

	string nums[10] = {"ZERO", "TWO", "FOUR", "SIX", "EIGHT", "SEVEN", "FIVE", "NINE", "ONE", "THREE"};
	int templ[10] = {0, 2, 4, 6, 8, 7, 5, 9, 1, 3}; 

	for (int e = 1; e <= t; e++) {

		cout << "Case #" << e << ": "; 
		string o;
		cin >> o;
   	    int chars[27] = {0};
  	    int chars2[27] = {0};

   	    int number[10] = {0};

		for (int i = 0; i < o.size();i++)
		{
			//cout << o[i] - 'A' << endl;
			chars[o[i]-'A']++;
		}

		for (int i = 0; i < 10; i++){
			
  			string tt = nums[i];

	   	    for(int k = 0; k <27; k++) {
	   	    	chars2[k] = chars[k];
	   	    }

	   	    bool flag = true;
	   	    while(flag == true) {
	   	    	int count = 0;
				for (int j = 0 ; j < tt.size(); j++) {
					int temp = chars2[tt[j]-'A'];
					if (temp > 0){
						chars2[tt[j]-'A'] = chars2[tt[j]-'A'] - 1;
						count = count + 1;
					}
					else{
						break;
					}
								}
				if(count == tt.size()){
					number[templ[i]]++;
					
					for (int d = 0 ; d < 27; d++) {
						chars[d] = chars2[d];
					}

				}
				else
					{flag = false;}
			}

		}

		for (int t=0; t<10; t++) {
			for (int p = 1; p <= number[t]; p++) {
				cout << t;
			}
		}
		cout << endl;
		
		
	}


}