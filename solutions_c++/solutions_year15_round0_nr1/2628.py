#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main() {
	string input;
	int t,shy;
	scanf("%d",&t);
	for (int tc=1;tc<=t;tc++) {
		scanf("%d",&shy);
		int sum = 0;
		int neededPeople = 0;
		cin>>input;
		for (int i=0;i<=shy;i++) {
			if ((sum<i) && (input[i]-48 != 0)) {
				neededPeople += (i-sum);
				sum += (i-sum);
			}

			sum += input[i]-48;

		}
		cout<<"Case #"<<tc<<": "<<neededPeople<<endl;
	}
	return 0;
}