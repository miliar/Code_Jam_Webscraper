#include <cstdio>

bool b[10];

int len(int n){
	if(n/10) return 1+len(n/10);
	else return 1;
}
int kth(int n,int k){
	if(k<=1) return n%10;
	else return kth(n/10,k-1);
}

int main()
{
	FILE* f= fopen("A-large.in","r");
	FILE* w = fopen("out.out","w");
	int T;
	fscanf(f,"%d",&T);
	for(int i=0;i<T;i++){
		for(int j=0;j<10;j++) b[j] = false;
		bool bb = false;
		int n,cn;
		fscanf(f,"%d",&n);
		cn=0;
		if(n==0) fprintf(w,"Case #%d: INSOMNIA\n",i+1);
		else{
			while(!bb){
				cn+=n;
				for(int k=1;k<=len(cn);k++){
					b[kth(cn,k)] = true;
				}
				bb=true;
				for(int k=0;k<10;k++) bb=bb&&b[k];
			}
			if(bb) fprintf(w,"Case #%d: %d\n",i+1,cn);
		}
	}
	return 0;
}
