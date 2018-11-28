#include<cstdio>
using namespace std;

void doCount(int k){
	char* str = new char[1024];
	int n,bc=0,ac=0;
	scanf("%d%s",&n,str);
	n++;
	for(int i=0;i<n;i++){
		if(bc>=i){
			bc+=str[i]-'0';
		}else if(str[i]-'0'!=0){
			ac+=i-bc;
			bc+=i-bc;
			bc+=str[i]-'0';
		}
	}
	delete str;
	printf("Case #%d: %d\n", k, ac);
}

int main(){
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++){
		doCount(i+1);
	}
}
