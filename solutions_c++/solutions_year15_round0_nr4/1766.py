#include<cstdio>

const char* result[] = {"GABRIEL", "RICHARD"};
//0-1 map can solve it all, but let's make sure for small points
//Is ok to find one to make all impossible
bool isok(int x, int l, int r){
	if(x==1){
		return 0;
	}
	if(x==2){
		return (l*r)%2!=0;
	}
	if(x==3){
		if(l*r==3)
			return 1;
		return (l*r)%3!=0;
	}
	if(x==4){
		if(l*r%4!=0) return 1;
		if(l*r==4||l*r==8) return 1;
		if(l*r==12) return 0;
		if(l*r==16) return 0;
	}
}

void doCount(int k){
	int x,l,r;
	scanf("%d%d%d",&x,&l,&r);
	printf("Case #%d: %s\n", k, result[isok(x,l,r)]);
}

int main(){
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++){
		doCount(i+1);
	}
}
