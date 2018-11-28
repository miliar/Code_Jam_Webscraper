#include<bits/stdc++.h>

using namespace std;
string s;
char r[2500];
int main(){
	int t,i,j,k,l,c;
	
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		cin>>s;
		r[1200]=s[0];
		j=1200;
		k=1201;
		for(l=1;l<s.length();l++){
			if(s[l]>=r[j]){
				j--;
				r[j]=s[l];
			}else{
				r[k]=s[l];
				k++;
			}
		}
		printf("Case #%d: ",i);
		for(l=j;l<k;l++){
			printf("%c",r[l]);
		}
		printf("\n");
	}
	return 0;
	
}
