#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int maxt = 1000;

void main() {
	int t;
	int loop=0, b=0;
	int bmk[1000] = { 0 };
	int j, result, result2;
	int tmp,max;
	char str[1001]; char swap[1001];
	char res[10001];


	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		memset(str,0x00,sizeof(str));
		cin >> str ;  // read n and then m.
		//cout << "Start Case " << i << ": " << b << " - " << n << endl;


		memset(res,0x00,sizeof(res));
		memset(swap,0x00,sizeof(swap));
		res[0] = str[0];
		for(j=1;j<strlen(str);j++){
			if ( str[j] >= res[0] ){
				strcpy( swap, res);
				res[0] = str[j];
				strcpy( &res[1], swap);
			} else {
				res[strlen(res)] = str[j];
			}
		}
		
		

		cout << "Case #" << i << ": " << res  << endl;

	}
}


// Usgae: MY_PROGRAM < input_file.txt > output_file.txt