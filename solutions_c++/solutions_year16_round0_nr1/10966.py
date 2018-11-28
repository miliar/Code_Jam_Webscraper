#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<iostream>
using namespace std;

int main(){
	int t,i,cnt=0,cnt2=0,num=0,j=0,b,k,l;
	string str;
	char c[1000001],c2[1000001];
	char tmp,a[10]={'0','1','2','3','4','5','6','7','8','9'};
	for(i=0;i<1000001;++i){c[i]='a'; c2[i]='a';}
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	while(scanf("%d",&t)!=EOF){
		for(l=1;l<=t;++l){
			cin>>str;
			strcpy(c,str.c_str());
			printf("Case #%d: ",l);
			for(i=0;i<1000001;++i){
				if(c[i]=='a'){cnt=i-1; break;}	
			}
			if(cnt==1 && c[0]=='0'){
				printf("INSOMNIA\n");
				continue;
			}
			for(i=0;i<(cnt/2);++i){
				tmp=c[i];					
				c[i]=c[cnt-i-1];
				c[cnt-i-1]=tmp;
			}
			while(num!=10){
				for(i=0;i<=cnt2;++i) c2[i]='a';
				++j;
				for(i=0;i<cnt;++i){
					b=(c[i]-'0')*j;
					if(b>9) c2[i+1]=b/10+'0';
					if(c2[i]!='a'){
						c2[i]=(c2[i]-'0')+b%10+'0';
						if(c2[i]>'9'){
							if(c2[i+1]!='a') c2[i+1]=(c2[i+1]-'0')+(c2[i]-'0')/10+'0';
							else c2[i+1]=(c2[i]-'0')/10+'0';
							c2[i]=(c2[i]-'0')%10+'0';	 
						}
					}
					else c2[i]=b%10+'0';
				}
				for(i=0;i<1000001;++i){
					if(c2[i]=='a'){cnt2=i; break;}
				}
				for(i=0;i<cnt2;++i){
					if(num==10) break;
					for(k=0;k<10;++k){
						if(c2[i]==a[k] && a[k]!='a'){
							++num;
							a[k]='a';
							break;
						}
					}
				}
			}
			for(i=0;i<cnt2;++i){
				printf("%c",c2[cnt2-i-1]);
				c2[cnt2-1-i]='a';
			}
			printf("\n");
			for(i=0;i<=cnt;++i) c[i]='a';
			for(i=0;i<10;++i) a[i]='0'+i;
			cnt=0; cnt2=0;
			j=0; num=0;
		}
	}
	
}
