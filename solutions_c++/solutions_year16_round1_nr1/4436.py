#include <bits/stdc++.h>

using namespace std;

bool sync_with_stdio (bool sync = false);

typedef long long ll;




int main(){
		
		int t, cont = 1;;
		scanf("%d", &t);
		char str[1011], aux[2][1011], ans[1011];
		while(t--){
			scanf(" %s", str);
			int tam = (int)strlen(str);
			for(int i = 0; i <= tam; i++){
				ans[i] = '\0';
			}
			ans[0] = str[0];
			for(int i = 1; i < tam; i++){
				//printf("ans = %s\n", ans);
				int tam2 = (int)strlen(ans);
				if(ans[0] <= str[i]){
					//printf("tam2 = %d\n", tam2);
					for(int j = tam2; j > 0; j--)
						ans[j] = ans[j-1];
					ans[0] = str[i];
				}
				else{
					//printf("oi\n");
					ans[tam2] = str[i];
				}
			}	
			
			printf("Case #%d: %s\n", cont++, ans);
			
		}

	return 0;
}
