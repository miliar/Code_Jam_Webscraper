#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int t,cases=1,quads[1001000],cumQuads[1500];
char a[10],b[10];

bool palin(){

	for (int i=0,j=strlen(a)-1;i < strlen(a) ; i++,j--){
		if (a[i] != a[j]) return false;
	}
	return true;
}

void generateQuads(){

	int q;

	for (int i=1;i<1005;i++){

		sprintf(a,"%d",i);
		if ( palin() ){
			q=i*i;
			if (q < 1005){
				sprintf(a,"%d",q);
				if ( palin() ){
					quads[q]++;
				}
			}else{
				break;
			}
		}
	}

}

int main(){

	int a1,b1,cumulative=0;

	memset(quads,0,sizeof(quads));

	generateQuads();


	for (int i=1; i < 1005;i++){
		cumQuads[i] = quads[i] + cumulative;
		cumulative = cumQuads[i];
	}

	scanf("%d\n",&t);

	while(t--){

		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));

		scanf("%d %d\n",&a1,&b1);
		
		if (quads[a1]) printf("Case #%d: %d\n", cases++, cumQuads[b1]-cumQuads[a1]+1);
		else printf("Case #%d: %d\n",cases++, cumQuads[b1]-cumQuads[a1]);

	}

}
