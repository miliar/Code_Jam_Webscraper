#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main()
{
	int tc, ti;
	scanf("%d", &tc);
	for (ti =1;ti <=tc;++ti) {
		char str[1010];
		scanf("%s", str);
		
		string target;
		
		int i;
		target = str[0];
		for (i=1;str[i]!=0;++i) {
			if (str[i]>=target[0])
				target = str[i] + target ;
			else
				target = target + str[i];
			
		}
		cout<<"Case #"<<ti<<": "<<target<<endl;
	}
	return 0;

}