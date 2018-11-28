#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t;
	cin >> t;
	int c = 1;
	while(t--){
		int a , b , k;
		int cnt=0;
		cin >>a >> b >> k;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				int temp = i&j;
				if(temp<k)
				cnt++;
			}
		}
		cout << "Case #" << c << ": " ;
		cout << cnt << endl;
		c++;
	}
	return 0;
}
