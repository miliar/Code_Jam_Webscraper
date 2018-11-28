#include <iostream>
#include <string>
#include <vector>
#include <limits.h>
#include <algorithm>
using namespace std;

int main(){
	long long a,b,c,d,e;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%lld", &a);
	for(int i = 0 ; i < a ; i++){
		string str;
		cin >> str;
		b = str.length();
		int cn[101]={0};
		while(true){
			d=-1;
			for(int i=b-1;i>=0;i--){
				if( (cn[i]%2 && str[i]=='+') || ( !(cn[i]%2 ) && str[i]=='-') ){
					d=i;
					break;
				}
			}
			if(d<0)
				break;
			for(int i=0;i<=d;i++)
				cn[i]++;
		}
		printf("Case #%d: %d\n", i+1,cn[0]);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}