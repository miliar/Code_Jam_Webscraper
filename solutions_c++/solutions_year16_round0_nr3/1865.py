#include <stdio.h>
int now[16];

int prim[100001];
bool getans;
int out[10];

void getpri(){
	for(int t=2;t<100001;t++){
		prim[t] =0;
	}
	for(int i=2;i<100001;i++){
		if(prim[i]==0){
				prim[i] = 1;
				for(int j=2*i;j<100001;j+=i){
					prim[j]= -1;
				}
			}
	}
	//for(int i=3;i<10001;i++)if(prim[i]!=-1){printf("%d ",i);}
	return ;
}

int cal(long long data){
	for(int i=83;i<100001;i=i+2){
		if(prim[i]!=-1){
			if(data%i==0)return i;
		}
	}
	return -1;
}



long long  getnum(int jinzhi){
	long long ret = 0;
	long long ji = 1;
	for(int i=15;i>=0;i--){
		ret += ji*now[i];
		ji = ji *jinzhi;
	}
	return ret;
}

void jiajia(){
	now[14]++;
	for(int i=14;i>=0;i--){
		if(now[i]==2){
			now[i]=0;
			now[i-1]++;
		}
	}
	return ;
}

int main()
{
	//freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	printf("Case #1:\n");
	getpri();
	int n,j;
	int get = 0;
	now[0] = now[15] = 1;
	for(int i=1;i<=14;i++)now[i]=0;
	while(get!=500){
			bool isans = true;
		for(int i=2;i<=10;i++){
			long long no = 	getnum(i);
			//printf("%d %lld\n",i,no);
			out[i] = cal(no);
			if(out[i] == -1){
				isans = false;
				break;
			}
		}
		if(isans){
			for(int i=0;i<16;i++)printf("%d",now[i]);
			for(int i=0;i<16;i++)printf("%d",now[i]);
			for(int i=2;i<=10;i++)printf(" %d",out[i]);
			printf("\n");
			get++;
		}
		jiajia();
	}
	return 0;
}
