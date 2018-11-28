#include<cstdio>

void f(){
	int t[17];
	int s;
	scanf("%d",&s);
	for(int i=0;i<17;i++)t[i]=0;
	for(int i=1;i<17;i++){
		int r;
		scanf("%d",&r);
		int z=i/4;
		z+=(bool)(i%4);
		if(z==s)t[r]=1;
	}
	scanf("%d",&s);
	for(int i=1;i<17;i++){
		int r;
		scanf("%d",&r);
		int z=i/4;
		z+=(bool)(i%4);
		if(z==s)t[r]+=1;
	}
	int w=0;
	int e=2;//1-bad 2-cheat
	for(int i=1;i<17;i++){
		if(t[i]==2){
			if(w!=0)e=1;
			else {
				w=i;
				e=0;
			}
		}
	}
	if(e==0)printf("%d\n",w);
	else if(e==1)printf("Bad magician!\n");
	else printf("Volunteer cheated!\n");
}

int main(){
	int a;
	scanf("%d",&a);
	for(int i=1;i<=a;i++){
		printf("Case #%d: ",i);
		f();
	}
}
