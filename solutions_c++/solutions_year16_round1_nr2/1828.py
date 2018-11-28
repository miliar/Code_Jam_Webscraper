#include<bits/stdc++.h>

#define getcx getchar_unlocked
#define putcx putchar_unlocked
#define ll long long int
#define ull unsigned long long int
#define MOD 1000000007

using namespace std;

inline void inpInt(int *n){
	*n=0;
	//bool neg=false;
	register char ch=getcx();
	while(ch<33){
		ch=getcx();
	}
	while(ch>32){
		//if(ch!='-'){
			*n=(*n<<3)+(*n<<1)+ch-'0';
		//}
		/*else {
			neg=true;
		}*/
		ch=getcx();
	}
	/*if(neg){
		*n=-(*n);
	}*/
}

inline void inpLL(ll *n){
	*n=0;
	//bool neg=false;
	register char ch=getcx();
	while(ch<33){
		ch=getcx();
	}
	while(ch>32){
		//if(ch!='-'){
			*n=(*n<<3)+(*n<<1)+ch-'0';
		//}
		/*else {
			neg=true;
		}*/
		ch=getcx();
	}
	/*if(neg){
		*n=-(*n);
	}*/
}

inline void inpULL(ull *n){
	*n=0;
	register char ch=getcx();
	while(ch<33){
		ch=getcx();
	}
	while(ch>32){
			*n=(*n<<3)+(*n<<1)+ch-'0';
		ch=getcx();
	}
}

inline void opInt(int n) {
        /*if(n<0){
                n=-n;
                putcx('-');
        }*/
        int i=21;
        char store[21];
        do{
                store[--i]=(n%10)+'0';
		n/=10;
        }while(n);
        do{
                putcx(store[i++]);
        }while(i<21);
}

inline void opLL(ll n) {
        /*if(n<0){
                n=-n;
                putcx('-');
        }*/
        int i=21;
        char store[21];
        do{
                store[--i]=(n%10)+'0';
		n/=10;
        }while(n);
        do{
                putcx(store[i++]);
        }while(i<21);
}

inline void opULL(ull n) {
        int i=21;
        char store[21];
        do{
                store[--i]=(n%10)+'0';
		n/=10;
        }while(n);
        do{
                putcx(store[i++]);
        }while(i<21);
}


int main(){
	int t,n,x;
	inpInt(&t);
	for(int i=1;i<=t;i++){
		inpInt(&n);

		int cnt[2505]={0};
		int upto=2*n-1;
		for(int j=0;j<upto;j++){
			for(int k=0;k<n;k++){
				inpInt(&x);
				cnt[x]++;
			}
		}
		printf("Case #%d: ",i);
		for(int i=0;i<=2500;i++){
			if(cnt[i]&1){
				printf("%d ",i);
			}
		}
		printf("\n");
	}
	return 0;

}
