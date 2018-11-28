#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	int T;
	cin>>T;
	int ans;
	int a,b,c;
	for(int x=0;x<T;x++){
		ans=0;
		cin>>a;
		cin>>b;
		cin>>c;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				if( (i&j) < c)
					ans++;
			}
		}
		printf("Case #%d: %d\n",x+1,ans);
	}
}