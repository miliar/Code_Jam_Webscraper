#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){

	ios::sync_with_stdio(0);
	ifstream input("B-large.in");
	ofstream output("output.txt");
	int t, i, ans, count = 1, j;
	string str;
	char ch;
	getline(input, str, '\n');
	t = atoi(str.c_str());
	

	while(t--){
		getline(input, str, '\n');
		ans = 0;
		i = str.rfind('-');
		while(i != -1){
			
			j = 0;
			while(str[j] == '+'){
				str[j++] = '-';
			}
			if(j > 0)
				ans++;

			for(j=0;j<=i/2;j++){
				ch = str[j];
				if(str[i-j] == '-')
					str[j] = '+';
				else
					str[j] = '-';

				if(ch == '-')
					str[i-j] = '+';
				else
					str[i-j] = '-';
			}
			i = str.rfind('-');
			ans++;
		}

		output << "Case #" << count++ << ": " << ans << "\n";
	}



	return 0;
}