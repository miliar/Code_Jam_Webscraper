#include "iostream"
#include "cstdio"
#include "cstring"

using namespace std ; 
int N , bit[100] ; 
int a[1000] , vis[1000];
int J ; 

bool div(int x , int y , int z){
	int res = 1 , t = y ;
	for(int i = 2 ; i <= N - 1 ; ++ i , x >>= 1 , t = t * y % z)
		if(x & 1) res = (res + t) % z ; 
	res = (res + t) % z ; 
	return res == 0 ; 
}

bool check(int x , int y){
	for(int i = 0 ; a[i] ; ++ i)
		if(div(x , y , a[i])) return true ; 
	return false ;
}

void out(int x){
	int X = x ; 
	for(int i = 2 ; i <= N - 1 ; ++ i , X >>= 1) bit[i] = X & 1 ; 
	bit[1] = bit[N] = 1 ; 
	for(int i = N ; i ; -- i) printf("%d",bit[i]);

	for(int i = 2 ; i <= 10 ; ++ i)
		for(int j = 0 ; a[j] ; ++ j)
			if(div(x , i , a[j])){
				printf(" %d",a[j]);
				break ; 
			}
	printf("\n");
}

const int M = 500 ; 
void make(){
	int t = 0 ; 
	for(int i = 2 ; i <= M ; ++ i)
		if(!vis[i]){
			a[t++] = i;
			for(int j = i ; j <= M ; j += i) vis[j] = 1 ; 
		}
}

int main(int argc, char const *argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	make();
	int ts ; 
	cin >> ts ; 
	printf("Case #1:\n");
	int cnt = 0 ; 
	cin >> N >> J ; 
	for(int i = 0 ; i < 1 << (N - 2) ; ++ i){
		bool flag = 1 ; 
		for(int j = 2 ; j <= 10 && flag ; ++ j)
			flag = check(i , j) ; 

		if(flag)
			out(i) , cnt ++ ;
		if(cnt == J) break ; 
	}
	return 0;
}