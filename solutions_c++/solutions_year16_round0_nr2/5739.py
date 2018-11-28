#include <stdio.h>
#include <fstream>
#include <string>
#include <iostream> 
using namespace std;

int solve(string str) {
	int count = 0;
	char c = str[0];
	int result = 0;
	while (c != '\0') {
		if (c =='+'){
			while (c != '-' && c!='\0') {
				count++;
				c = str[count];
			}
			result+= (c=='-') ? 1 : 0;
		}
		else {
			result++;
			while (c != '+' && c!='\0') {
				count++;
				c = str[count];
			}
		}
	}

	return result;
}

int main()
{
	freopen("pancakes.out","w",stdout);
	int T,i;

	ifstream file("B-large.in");
    string str; 
	file>>T;
   getline(file, str);
    for(i=1;i<=T;i++) {
		getline(file, str);
		printf("Case #%d: %d\n",i,solve(str));
	}
}