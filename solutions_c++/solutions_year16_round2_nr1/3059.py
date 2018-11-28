#include<iostream>
#include<string>
#include<string.h>
#include<algorithm>
#include<functional>
#include<fstream>

using namespace std;
int main (){
    int n,j=1,i;
	string m;
	ifstream infile("codejam.txt");
	ofstream offile("output.txt");
    infile>>n;
    while(infile>>m){
      // m="OOEWIENERROOZNZTRUF";
    	int a[26] = {0};
    	int b[10] = {0};
    	for(i = 0 ; i < m.length(); i++){
    		a[m[i]-'A']++;
		}
		if(a[25] != 0){
			a[4] -= a[25];
			a[17] -= a[25];
			a[14] -= a[25];
			b[0] = a[25];
			a[25] = 0;
		}
		if(a[22] != 0){
			a[19] -= a[22];
			a[14] -= a[22];
			b[2] = a[22];
			a[22] = 0;
		}
		if(a[23] != 0){
			a[18] -= a[23];
			a[8] -= a[23];
			b[6] = a[23];
			a[23] = 0;
		}
		if(a[18] != 0){
			a[4] -= 2*a[18];
			a[21] -= a[18];
			a[13] -= a[18];
			b[7] = a[18];
			a[18] = 0;
		}
		if(a[6] != 0){
			a[4] -= a[6];
			a[8] -= a[6];
			a[7] -= a[6];
			a[19] -= a[6];
			b[8] = a[6];
			a[6] = 0;
		}
		if(a[21] != 0){
			a[5] -= a[21];
			a[8] -= a[21];
			a[4] -= a[21];
			b[5] = a[21];
			a[21] = 0;
		}
		if(a[7] != 0){
			a[19] -= a[7];
			a[17] -= a[7];
			a[4] -= 2*a[7];
			b[3] = a[7];
			a[7] = 0;
		}
		if(a[17] != 0){
			a[5] -= a[17];
			a[14] -= a[17];
			a[20] -= a[17];
			b[4] = a[17];
			a[17] = 0;
		}
		if(a[14] != 0){
			a[13] -= a[14];
			a[4] -= a[14];
			b[1] = a[14];
			a[14] = 0;
		}
		if(a[13] != 0){
			a[8] -= a[13];
			a[4] -= a[13];
			b[9] = a[13]/2;
			a[13] = 0;
		}
		
		offile<<"Case #"<<j++<<": ";
		for(i =0; i < 10; i++){
			while(b[i]--){
				offile<<i;
			}
		}
		offile<<"\n";
		}
}

