#include <bits/stdc++.h>
using namespace std;

int main(){

	int n, t = 1;
	char entrada[2000];
	scanf("%d", &n);

	while(n--){
		scanf(" %s", entrada);
		string resp;
		resp = entrada[0];
		for(int i=1; i<strlen(entrada); i++){
			if(entrada[i] >= resp[0]){
				resp = entrada[i] + resp;
			}else{
				resp += entrada[i];
			}
		}
		printf("Case #%d: %s\n", t++, resp.c_str());
	}



	return 0;
}