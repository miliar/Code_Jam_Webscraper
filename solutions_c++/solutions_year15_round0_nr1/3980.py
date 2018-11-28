#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <climits>
#include <numeric>
#include <stdlib.h> 
#include <time.h> 
#include <math.h>
#include <string>
using namespace std;
string str1;
int main(){
//freopen("A-large.in", "r", stdin);
//freopen("A-small-attempt0.out", "w", stdout);
	int T, n, ans, s, i,x ;
	cin>>T;
	for(int I=0; I<T; I++){
		cin>>n>>str1;
		ans = 0; s = 0;
		for(i=0; i<=n; i++){
			if (i<=s){
				x = str1[i]-48;
				s+=x;
			} else {
				ans += i-s;

				s=i+str1[i]-48;
			}
		}
		cout<<"Case #"<<I+1<<": "<<ans;
		if(I!=T-1) {
			cout<<endl;
		}

		
	}
		//fclose(stdin);
		//fclose(stdout);
			return 0;
}