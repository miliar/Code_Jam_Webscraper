#include <stdio.h>
#include <string.h>

int main(){
	//freopen("B-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t); getchar();
	for(int i=1;i<=t;i++){
		char s[110]={0};
		scanf("%[^\n]",s); getchar();
		int len=strlen(s);
		int ans=0;
		if(len>1){
			for(;;){
				int kanan=-1,kiri=-1;
				for(int j=len-1;j>=0;j--){
					if(s[j]=='-'){
						kanan=j;
						break;
					}
				}//+- kanan=1
				if(kanan==-1) break;
				for(int j=0;j<=kanan;j++){
					if(s[j]=='-'){
						kiri = j-1;
						break;
					}
				}
				for(int j=0;j<=kiri;j++) s[j]='-';
				//printf("%d %s\n",kiri,s); getchar();
				if(kiri!=-1) ans+=1;
				char temp[110]={0};
				
				for(int j=kanan;j>=0;j--){
					if(s[j]=='-') temp[len-j-1]='+';
					else temp[len-j-1]='-';
				}
				for(int j=len-1;j>=0;j--) s[j]=temp[j];
				ans+=1;
				//printf("%s\n",s);
			}
		}
		if(s[0]=='+' && strlen(s)==1) ans=0;
		else if(strlen(s)==1)ans=1;
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
/*
cek dri knan ada min gak
kalo plg ujung knan itu - artinya hrus di plus in dlu
tapi cek kiri min gak kalo ngak, hrus di min dulu sampai di plus ke berapaa itung dri knan
itu yang di flip

++-+-
---+-
+-+++*/
