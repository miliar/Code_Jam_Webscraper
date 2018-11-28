#include <cstdio>
#include <cstring>

bool check_str(char *str,int len) {
	for(int i=0;i<len;i++) {
		if(str[i]=='-') return true;
	}
	return false;
}

void run(int r) {
	char str[200]={};
	scanf("%s",str);
	int len = strlen(str);
	int cou = 0;
	while(check_str(str,len)) {
		if(str[0]=='+') {
			int i=0;
			while(str[i]!='-')i++;
			for(int j=0;j<i/2;j++) {
				int temp = str[j];
				str[j] = str[i-1-j];
				str[i-1-j] = temp;
			}
			for(int j=0;j<i;j++) {
				if(str[j]=='-')str[j]='+';
				else str[j]='-';
			}
			cou++;
		}
		while(str[len-1]=='+') len--;
		if(str[len-1]=='-') {
			for(int i=0;i<len/2;i++) {
				int temp = str[i];
				str[i] = str[len-1-i];
				str[len-1-i] = temp;
			}
			for(int i=0;i<len;i++) {
				if(str[i]=='-')str[i]='+';
				else str[i]='-';
			}
			cou++;
		}
	}
	printf("Case #%d: %d\n",r,cou);
}

int main() {
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
		run(i);
}