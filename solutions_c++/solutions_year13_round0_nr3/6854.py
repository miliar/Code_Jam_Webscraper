#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	int t;
	cin >> t;
	int j =1;
	while(t--){
		int a,b;
		cin >> a >> b;
		int c = 0;
		if(a <= 4 && b >= 4 )
		 c++;
		if(a == 1 )
		 c++;
		if(a <= 9 && b >= 9 )
		 c++;
		if(a <= 121 && b >= 121 )
		 c++;
		if(a <= 484 && b >= 484 )
		 c++;
		cout <<"Case #" << j << ": " << c << endl;
		j++;
	}

	return 0;
}