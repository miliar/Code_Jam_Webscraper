#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T,smax;
	cin >> T;
	int index=1;
	while(T--){
		
		cin>>smax;
		string s;
		cin>>s;
		int count = s[0] -'0',frnd =0;
		
		for(int i=1;i<=smax;i++){
			int temp = s[i] - '0';
			if(temp>0)
			{
		
			if(i-count>frnd){
				frnd = (i - count);
			}
			count+= temp;
		}
			
			
		}
		printf("Case #%d: %d\n",index, frnd);
		index++;
	}

	return 0;
}
