#include <cstdio>
#include <cstdlib>

bool integer[20];

void init(){
	for(int x = 0;x <20;x++) integer[x] = false;
	return;
}

bool fff(int n){
	int h = n;
	while(h!=0){
		integer[ h % 10]  = true;
		h/=10;
	}
	for(int x = 0;x<=9;x++) if(!integer[x]) return false;
	return true;
}

int dofind(int num){
	for(int z = 1;z < 1000;z++){
		int  k = num * z;
		if(fff(k)) return z;
	}
	return -20;
};

main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for(int z = 1;z <= t;z++){
		int r= z;
		int test;
		init();
		scanf("%d",&test);
		int a = dofind(test);
		if(a!=-20) printf("Case #%d: %d\n",r,test*a);
		else printf("Case #%d: INSOMNIA\n",r);
	}

	fclose (stdin);
	fclose (stdout);

	return 0;
}