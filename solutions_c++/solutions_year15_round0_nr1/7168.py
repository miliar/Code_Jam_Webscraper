#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,s,a,ans,d;
	char str[1009];
	scanf("%d",&t);
	for(int k=0;k<t;k++){
		a = ans = 0;
		getchar();
		scanf("%d %s",&s,str);
		a = str[0]-48;
		for(int i=1;i<=s;i++){
			if(a < i){
				d = (i-a);
				a += d;
				ans += d;
				a+= str[i] - 48;
			}
			else{
				a+= str[i]-48;
			}
		}
		printf("Case #%d: %d\n",k+1,ans);
	}
    
    return 0;
}