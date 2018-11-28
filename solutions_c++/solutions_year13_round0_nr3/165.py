//

#include <cstdio>
#include <algorithm>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <set>
#include <cmath>
#include <iostream>
#include <ctime>
#include <cassert>

using namespace std;

#define db(x) cout << #x " == " << x << endl
//#define _ << ", " <<
#define Fr(a,b,c) for( int a = b ; a < c ; ++a )
#define CL(a,b) memset(a,b,sizeof(a))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vpii;
typedef map<int,int> mii;
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3fLL
#define ULMAX 0xffffffffffffffffULL
#define y1 Y1

#define N 1000000
#define BLAH 140

int t,_=1;
char a[BLAH],b[BLAH];
char tmp[20];
ll prep[N];
string resp[N];
int ind=0;

bool palin(ll a){
	sprintf(tmp,"%lld",a);
	int n = strlen(tmp);
	Fr(i,0,n>>1) if(tmp[i]!=tmp[n-i-1]) return 0;
	return 1;
}



char str[BLAH], sq[BLAH], sq2[BLAH], mat[BLAH][BLAH];

bool square(int tam){
	str[tam]=0;
	memset(mat,0,sizeof(mat));
	memset(sq,0,sizeof sq);
	memset(sq2,0,sizeof sq2);
	for(int j=tam-1; j>=0; j--){
		int ac=0;
		for(int i=tam-1; i>=0; i--){
			mat[j][2+i+j]=str[j]*str[i] +ac;
			ac=mat[j][2+i+j]/10, mat[j][2+i+j]%=10;
		}
		mat[j][1+j]=ac;
//		Fr(i,0,1+(tam<<1)) printf("%d ",mat[j][i]);
//		puts("");
		Fr(i,0,1+(tam<<1)) sq2[i]+=mat[j][i];
	}
	for(int i=(tam<<1); i>0; i--) sq2[i-1]+=sq2[i]/10, sq2[i]%=10;
	
	int newtam=1+(tam<<1);
	while(sq2[0]==0){
		Fr(i,0,newtam-1) sq2[i]=sq2[i+1];
		newtam--;
	}
	
	
	Fr(i,0,newtam>>1) if(sq2[i]!=sq2[newtam-i-1]) return 0;
	if(newtam>110) return 0;
	
//	Fr(i,0,tam) printf("%d",str[i]);	printf(":   ");
//	Fr(i,0,newtam) printf("%d",sq2[i]);	puts("");
	
	
	int start=BLAH-(3+newtam);
	Fr(i,0,start) sq[i]=' ';
	Fr(i,0,newtam) sq[start++]=sq2[i]+'0';
	sq[start]=0;
	return 1;
//	printf(">%s\n",sq);
}

bool bitcnt(int a){
	int cnt=0;
	while(a) cnt++, a-=a&-a;
	return cnt<=1;
}

#define WUT 50
ll masks[N], mind=0;

void preproc(){
	masks[mind++]=0;
	Fr(i,0,WUT){
		masks[mind++]=1LL<<i;
		Fr(j,i+1,WUT){
			masks[mind++]=(1LL<<i)|(1LL<<j);
			Fr(k,j+1,WUT){
				masks[mind++]=(1LL<<i)|(1LL<<j)|(1LL<<k);
			}
		}
	}
	sort(masks,masks+mind);
//	printf(">%d\n",mind);
//	Fr(i,0,mind) printf(".%lld\n",masks[i]);
}

int main() {
//	cin.sync_with_stdio(false);
/*	char lixo[] = "100000"; Fr(i,0,6) str[i]=lixo[i]-'0';
	square(6);
	return 0;//*/
	preproc();
	
	resp[ind++]=string("                                                                                                                                        0");
	resp[ind++]=string("                                                                                                                                        1");
	resp[ind++]=string("                                                                                                                                        4");
	resp[ind++]=string("                                                                                                                                        9");
	Fr(tam,0,WUT){
		int tamanho = 2+(tam<<1);
//		printf("tam %d\n",tam);
		
		int lim = (tam<<1)+1;
		int mei = tam+1;
		str[0]=str[lim]=2;
		
		Fr(i,1,lim) str[i]=0;
		if(square(tamanho)) resp[ind++]=string(sq);
//		printf(">%s:%s\n",str,sq);
			
		str[0]=str[lim]=1;
		Fr(it,0,mind) {
			if(masks[it]>=(1<<tam)) break;
			ll mask=masks[it];
			Fr(i,1,mei) str[i] = (mask&(1LL<<(i-1)))>>(i-1);
			Fr(i,mei,lim) str[i] = (mask&(1LL<<(lim-i-1)))>>(lim-i-1);
			if(square(tamanho)) resp[ind++]=string(sq);
//			printf(">%s:%s\n",str,sq);
		}
		
		
		
		int meio=mei;
		tamanho++, lim++, mei++;
		str[0]=str[lim]=2;
		Fr(i,1,lim) str[i]=0;
		if(square(tamanho)) resp[ind++]=string(sq);
		str[meio]=1;
		if(square(tamanho)) resp[ind++]=string(sq);
		
		
		str[0]=str[lim]=1;
		
		Fr(it,0,mind) {
			if(masks[it]>=(1<<tam)) break;
			ll mask=masks[it];
			Fr(i,1,mei) str[i] = (mask&(1LL<<(i-1)))>>(i-1);
			Fr(i,mei,lim) str[i] = (mask&(1LL<<(lim-i-1)))>>(lim-i-1);
			
			str[meio]=0; if(square(tamanho)) resp[ind++]=string(sq);
			str[meio]=1; if(square(tamanho)) resp[ind++]=string(sq);
			if(bitcnt(mask)) {str[meio]=2; if(square(tamanho)) resp[ind++]=string(sq);}
//			printf(">%s:%s\n",str,sq);
		}
	}
	
	sort(resp,resp+ind);
//	printf("ind %d\n",ind);
//	Fr(i,0,ind) cout << resp[i] << endl;
//*/


/*	prep[ind++]=0;
	Fr(i,1,N) if(palin(i) && palin(ll(i)*i)) printf("%d: %lld\n",i,ll(i)*i), prep[ind++]=ll(i)*i;
	Fr(i,1000000,2300000) if(palin(i) && palin(ll(i)*i)) printf("%d: %lld\n",i,ll(i)*i), prep[ind++]=ll(i)*i;
	Fr(i,10000000,23000000) if(palin(i) && palin(ll(i)*i)) printf("%d: %lld\n",i,ll(i)*i), prep[ind++]=ll(i)*i;
	Fr(i,100000000,230000000) if(palin(i) && palin(ll(i)*i)) printf("%d: %lld\n",i,ll(i)*i), prep[ind++]=ll(i)*i;
//*/
	
/*	0000
	0001
	0010
	0011
	0100
	0101
	0110
	0111
	
	1000
	1001
	1010
	1011
	1100
	1101
	1110
	1111
	
	2000
	2100
	2010
	2001//*/
	
	
//	printf("%d\n",ind);
//	Fr(i,0,ind) printf("%lld\n",prep[i]);
	
	for(scanf("%d",&t);t--;){
		scanf("%s%s",&a,&b);
		int tam = strlen(a);
		for(int i=tam-1; i>=0; i--) if(a[i]=='0') a[i]='9'; else {a[i]--; break;}
		while(a[0]=='0' && tam>1){
			Fr(i,0,tam-1) a[i]=a[i+1];
			tam--;
		}
		int start=BLAH-(3+tam);
		Fr(i,0,start) sq[i]=' ';
		Fr(i,0,tam) sq[start++]=a[i];
		
		string um = string(sq);
		
		tam = strlen(b);
		start=BLAH-(3+tam);
		Fr(i,0,start) sq[i]=' ';
		Fr(i,0,tam) sq[start++]=b[i];
		
		string dois = string(sq);
//		cout << um << endl;
		
		int bloh = (upper_bound(resp,resp+ind,dois)-resp) - (upper_bound(resp,resp+ind,um)-resp);
		if(bloh<0) bloh=0;
		
		printf("Case #%d: %d\n",_++,bloh);
		
	}
	return 0;
}
