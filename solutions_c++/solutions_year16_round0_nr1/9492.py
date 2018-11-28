#include <cstdio>
#include <iostream>
#include <cstring>
#include <sstream>

using namespace std;

int main(void){
	long long N , res, T, i;
	string str;
	char num[10] = {'0','1','2','3','4','5','6','7','8','9'};
	int arr[10] = {0};	
	
	cin >> T;
	
	long long t = 1;
	
	while(T--){ 
		res = 0;
		i = 1;
		cin >> N;
		if( N == 0) cout << "Case #" << t << ": INSOMNIA" << endl;
		else {
			memset(arr, 0, sizeof(arr));
			while(true){	
				res = i * N;
				stringstream out;	
				out << res;	
				str = out.str();	
				for (int k = 0; k < str.length(); k++){	
					for (int j = 0; j < 10; j++){
						if(str[k] == num[j]) arr[j]++;
					}
				}
				if(arr[0] >= 1 && arr[1] >= 1 && arr[2] >= 1 && arr[3] >= 1 && arr[4] >= 1 && arr[5] >= 1 && arr[6] >= 1 && arr[7] >= 1 && arr[8] >= 1 && arr[9] >= 1) break;
				i++;		
			}	
			cout << "Case #" << t << ": " << res << endl;		
		}	
		t++;
	}
	
	return 0;
}