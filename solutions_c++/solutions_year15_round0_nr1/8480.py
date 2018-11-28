#include<bits/stdc++.h>
using namespace std;

int main() {
	int t ,index = 1;
	cin >> t;

	while(t--) {
		int n;
		int temp = 0;
		cin >> n ;
		string s;

		int noofclappers = 0;
		cin >> s;
		//cout << s << endl;
		for(int i = 0; i<s.size() ; i++) {
			//printf("isrequired = %d s[%d]=%c noofclappers = %d\n",temp,i,s[i],noofclappers);
				

				if(noofclappers < i && s[i] != '0') {
					//printf(" i = %d\n",i);

					temp += i - noofclappers;
					//printf("i = %d noofclappers = %d \n",i ,noofclappers);
					noofclappers = i;
					//printf("isrequired = %d s[%d]=%c noofclappers = %d\n",temp,i,s[i],noofclappers);
				}
				noofclappers += s[i] - '0';

			
		}
		printf("Case #%d: %d\n",index++,temp);
	}
	return 0;

}