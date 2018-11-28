#include <cstdio>
#include <cstring>

int psnumbers[10000009];
int pscounter = 0;

#define DIEZ7 10000000
#define DIEZ14 100000000000000

bool isPal(int n){
	char s[20];
	sprintf(s,"%d",n);
	int len = strlen(s);
	for(int i=0;i<len/2;i++){
		if ( s[i] != s[len-i-1] )
			return false;
	}
	return true;
}

void pre(){

	for(int i=1;i<=DIEZ7;i++){
		if ( isPal(i) && isPal(i*i) )
		{
			psnumbers[pscounter++] = i*i;
		}
	}

}

int main(){
	pre();

	int t;
	scanf("%d",&t);
	int caso = 1;
	while(t--){
		int a,b;
		int cont = 0;

		scanf("%d %d",&a,&b);

		for(int i=0;i<pscounter;i++){
			if ( a <= psnumbers[i] && psnumbers[i] <= b ){
				//printf(">%d\n",psnumbers[i]);
				cont++;
			}
		}

		printf("Case #%d: %d\n",caso++,cont);

	}



	return 0;
}
