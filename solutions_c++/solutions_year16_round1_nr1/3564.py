#include <cstring>
#include <cstdio>
using namespace std;
int T,t,ll,i,ts,te;
char lett[1100];
char tgt[2200];
int main(){
	scanf("%d",&T);
	for(t=0;t<T;t++){
		printf("Case #%d: ",t+1);
		scanf("%s",lett);
		ll=strlen(lett);
		//printf("[%d][%s]\n",ll,lett);
		ts=te=1100;
		tgt[--ts]=lett[0];
		for(i=1;i<ll;i++)
			if (lett[i]<tgt[ts])
				tgt[te++]=lett[i];
			else
				tgt[--ts]=lett[i];
		tgt[te]='\0';
		printf("%s\n",tgt+ts);
	}
}
