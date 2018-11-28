#include <cstdio>

using namespace std;

int cti(char a){
	char angka[] = "0123456789";
	for(int i=0; i<10; i++)
		if(a== angka[i]) return i;
}

int main(){
	int T,n,jumlah,ans,temp;
	char exp[1005];
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
		scanf("%d %s",&n,&exp);
		jumlah = cti(exp[0]);
		ans = 0;
		for(int j=1; j<=n; j++){
			if(cti(exp[j])!= 0){
				
				if(jumlah < j){
					ans +=j-jumlah;
					jumlah += ans + cti(exp[j]);
				}
				else{
					jumlah+=cti(exp[j]);
				}
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
}
