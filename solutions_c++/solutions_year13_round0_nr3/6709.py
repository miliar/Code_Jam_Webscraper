# include <iostream>
# include <stdlib.h>
# include <cmath>
# include <string>
# include <sstream>
# include <algorithm>
# include <cstdio>

using namespace std;

template <typename T>
bool palindrome( T Number )
{
     	ostringstream ss;
     	ss << Number;
     	string x = ss.str();
	if(x.size() == 1) return true;
	string y = x;
	reverse(x.begin(),x.end());
	if(x == y) return true;
	return false;
}

int main(){
	freopen("03.in", "rt", stdin);
	freopen("output03.txt", "wt", stdout);
	int t;
	scanf("%d",&t);
	for(int i = 0 ; i < t ; i++){
		bool result = false;
		int s,e;
		int count = 0;
		scanf("%d %d",&s,&e);
		for(int j = s ; j <= e ; j++){
			float a = sqrt(j);
			if(a-(int)a == 0){
				if(palindrome(j) && palindrome(a))
					count++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}
