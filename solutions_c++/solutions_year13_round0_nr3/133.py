#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#define MOD 100000
using namespace std;
char rres[102];
char tan[102];
long long bit[102];
long long rmul[102];
char pal[102];
int can2 ;
int can1 ;
int ans = 0;
long long ct = 0;
char goal[100000][102];
int ind[100000];
char ta[1000],aa[1000];
char tb[1000],bb[1000];
int cmp(int a,int b){
	for(int i = 101 ; i >= 0 ; i-- ){
		if( goal[a][i] != goal[b][i] ) return goal[a][i] < goal[b][i] ;
	}
}
int pp(char *sa,char *sb){
	for(int i = 101 ; i>= 0 ;i-- ){
		if( sa[i] != sb[i] ){
			if( sa[i] < sb[i] ) return 0;
			else return 1;
		}
	}
	return 1;
}
int binsearch(char *x){
	int left = 0, right = ans-1;
	for( ; left < right ; ){
		//printf("-- %d %d\n",left,right);
		int mid = (left+right)/2;
		if( pp(goal[ind[mid]],x) == 0 ){
			left = mid+1;
		}else{
			right = mid;
		}
		/*
		for(int i = 0; i<5 ;i++ ) printf("%d",goal[ind[mid]][i]);
		printf("\n");
		for(int i =0 ;i<5 ; i++ ) printf("%d",x[i]);
		printf("\n");*/
	}
	if( pp(goal[ind[left]],x) == 0 ) return left+1;
	else return left;
}

int getpalin(int type){
	int num = 0;
	for(int i = 101 ; i>= 0 ; i-- ){
		if( rres[i] != 0 ){
			num = i;
			break;
		}
	}
	num++;
	if( type == 0 ){
		for(int i = 0 ; i< num ;i++ ){
			tan[num+i] =rres[i];
			tan[num-1-i] = rres[i];
		}
		num*=2;
		for(int i = num ; i < 102 ; i++ ) tan[i] = 0;
	}else{
		for(int i = 0 ;i < num ;i++ ){
			tan[num+i-1] = rres[i];
			if( i != 0 ) tan[num-1-i] = rres[i];
		}
		num = num*2-1;
		for(int i = num ; i < 102 ; i++ ) tan[i] = 0;
	}
}
int getbit(){
	for(int i = 0 ;i < 102 ; i++ ) bit[i] = 0;
	for(int i = 101 ; i >= 0 ; i-- ){
		bit[i/5]*=10;
		bit[i/5]+=tan[i];
	}
}
int mul(){
	for(int i = 0;i < 11 ; i++ ){
		for(int j = 0; j< 11 ;j++ ){
			rmul[i+j] += bit[i] * bit[j];
		}
	}
	for(int i = 0; i < 101 ; i++ ){
		rmul[i+1] += rmul[i]/MOD;
		rmul[i] %= MOD;
	}
}
int ispalin(){
	for(int i = 0;i< 102 ; i++ ){
		pal[i] = rmul[i/5]%10;
		rmul[i/5]/=10;
	}
	int num = -1;
	for(int i = 101 ; i>= 0 ; i-- ){
		if( pal[i] != 0 ){ num = i; break; }
	}
	num++;
	int chk = 1;
	for(int i = 0; i < num/2; i++ ){
		if( pal[i] != pal[num-1-i] ){ chk = 0; break; }
	}
	return chk ;
}

int rec(int k){
	if( k == 26 ){
		int chk = 1;
		ct++;
		//if( ct % 100000 == 0  ) printf("ct == %lld, %lld\n",ct,ans);
		for(int i = 0 ;i <102 ; i++ ){
			if( rres[i] != 0 ){ chk = 0; break; }
		}
		if( chk ) return 0;
		getpalin(0);
		getbit();
		mul();
		if( ispalin() ){
			/*if( 1 ){
				int chk = 0;
				for(int i = 101 ; i>= 0 ;i-- ){
					if( tan[i] != 0 ) chk = 1;
					if( chk ) printf("%d",tan[i]);
				}
				printf("\n");
			}*/
			for(int i = 0 ; i < 102 ; i++ ) goal[ans][i] = pal[i];
			ans++;
		}
		
		getpalin(1);
		getbit();
		mul();
		if( ispalin() ){
			/*if( 1 ){
				int chk = 0;
				for(int i = 101 ; i>= 0 ;i-- ){
					if( tan[i] != 0 ) chk = 1;
					if( chk ) printf("%d",tan[i]);
				}
				printf("\n");
			}*/
			for(int i = 0 ; i < 102 ; i++ ) goal[ans][i] = pal[i];
			ans++;
		}
		return 0;
	}	
		
	rres[k] = 0;
	rec(k+1);
	if( can1 > 0 ){
		can1--;
		rres[k] = 1;
		rec(k+1);
		can1++;
	}
	if( can2 == 1 ){
		can2 = 0;
		rres[k] = 2;
		rec(k+1);
		can2 = 1;
	}
}

int main(){
	can1 = 6;
	can2 = 1;
	rec(0);
	//printf("%lld\n",ans);
	goal[ans][0] = 9;
	for(int i = 1 ;i < 102; i++ ) goal[ans][i] = 0;
	ans++;
	for(int i =0; i < ans ; i++ ) ind[i] = i;
	sort(ind,ind+ans,cmp);

	int t;
	scanf("%d",&t);
	for(int e = 0; e< t ;e++ ){
		scanf("%s %s",ta,tb);
		int na,nb ;
		na = strlen(ta);
		nb = strlen(tb);
		for(int i =0 ; i <103 ; i++ ){
			aa[i] = 0;
			bb[i] = 0;
		}
		for(int i = 0 ; i < na ; i++ ){
			aa[na-1-i] = ta[i]-'0';
		}
		for(int i = 0; i < nb ; i++ ){
			bb[nb-1-i] = tb[i]-'0';
		}
		int ia = binsearch(aa);
		int ib = binsearch(bb);
		int dif = ib-ia;
		int chk = 1;
		for(int i = 0; i < 102 ; i++ ){
			if( bb[i] != goal[ind[ib]][i] ){
				chk = 0;
				break; 
			}
		}
		if( chk ) dif++;
		//printf("ss %d %d\n",ia,ib);
		printf("Case #%d: %d\n",e+1,dif);
	}

	//printf("%d\n",ans);
	/*for(int i = 0;i< ans ; i++ ){
		int chk = 0;
		printf("%d = ",i+1);
		for(int j = 101; j>= 0 ; j-- ){
			if( goal[ind[i]][j] != 0 ) chk = 1;
			if( chk ) printf("%d",goal[ind[i]][j]);
		}
		printf("\n");
	}*/
}
