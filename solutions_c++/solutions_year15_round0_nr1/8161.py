#include <iostream>
#include <string.h>
using namespace std;

int main() {
	// your code goes here
	int T;
	int smax;
	char people[1000000];
	int bring = 0;
	int stood = 0;
	cin>>T;
	int case1 = 1;
	while(T--) {
		cin>>smax;
		cin>>people;
		bring = 0;
		//cout<<smax<<endl;;
		//cout<<strlen(people)<<endl;
		stood = people[0] - '0';
		//<<stood<<endl;
		for (int i = 1; i <= smax; i++) {
			if (people[i] != '0') {
				if (stood < i) {
					bring += (i - stood);
					stood += (i - stood);
				}
				stood += people[i] - '0';
			}
		}
		cout<<"Case #"<<case1<<": "<<bring<<endl;
		case1++;
	}
	return 0;
}
