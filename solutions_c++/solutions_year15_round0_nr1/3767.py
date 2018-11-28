#include <bits/stdc++.h>

#define MAX 1010

using namespace std;

typedef long long int ll;

int T,tam;
char s[MAX];

int main(){
	scanf("%d",&T);

	for(int caso=1;caso<=T;caso++){
		
		scanf("%d %s",&tam,s);

		int cont=0;
		int resp=0;
		for(int i=0;i<=tam;i++){
			if(i>cont){ resp+=i-cont; cont=i;}
			cont+=s[i]-'0';
		}	
	
		printf("Case #%d: %d\n",caso,resp);	
	}
}
