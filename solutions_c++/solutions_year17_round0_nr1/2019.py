#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main(){
	int t, n;
	string s;
	cin >> t;
	for(int c = 1; c<=t;c++){
		cin >> s >> n;
		int size = s.size();
		int count = 0;
		int i = 0, j = 0;
		bool right = true;
		for(int i = 0; i<size;i++){
			if(i<=size-n){
				if(s[i] == '-'){
					for(int j=0,k=i;j<n;j++){
						if(s[k] == '-') s[k++] = '+';
						else s[k++] = '-';
					}
					count++;
				}
			}
			else{
				if(s[i]=='-') {
					right = false;
					break;	
				}
			}
			
		}
		
		if(right) printf("Case #%d: %d\n",c,count);
		else printf("Case #%d: IMPOSSIBLE\n",c);
	}
	
}
