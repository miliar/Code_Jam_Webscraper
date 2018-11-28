#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;


int main(int argc, char* argv[]) {
	int t;
	char s[101];
	char prev;
	int y;
	int j;
//	std::vector<int> d;
//	int c[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

	
	freopen("input_file.in","r",stdin);
	freopen("output_file.out","w",stdout);
	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> s;
		prev = s[0];
		y = 0;
		for( j = 0; j < strlen(s); j++){
			if(prev == s[j]){
				
			}
			else {
				y++;
			}
			prev = s[j];
		}
		if(s[j-1] == '-') y++;
		cout << "Case #" << i + 1 << ": " << y << endl;
	}
	return 0;
}
