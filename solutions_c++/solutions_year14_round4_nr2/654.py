#include<stdio.h>
#include<algorithm>
using namespace std;
int in[100000];
int tmp[10000];
int tab[10000];
int swap(int a,int b){
	int k = tab[a];
	tab[a] = tab[b];
	tab[b] = k;
}
int main(){
	int t;
	scanf("%d",&t);
	for(int e = 0 ; e< t ;e++ ){
		int n;
		scanf("%d",&n);
		for(int i = 0 ; i < n; i++ ){
			scanf("%d",&in[i]);
			tmp[i] = in[i];
		}
		sort(tmp,tmp+n);
		for(int i = 0 ; i < n ;i++ ){
			for(int j = 0 ;j < n ;j++ ){
				if( in[j] == tmp[i] ){
					tab[j] = i;
				}
			}
		}
		int left = 0,right =n-1 ;
		int ans = 0;
		for(int k = 0 ; k < n ; k++ ){
			int pos ;
			for(int i = 0 ; i < n ; i++ ){
				if( tab[i] == k ){
					pos = i;
					break;
				}
			}
			if( pos-left < right-pos ){
				ans += pos-left;
				for(int i = pos-1 ; i >= left ;i-- ){
					swap(i,i+1);
				}
				left++;
			}else{
				ans += right-pos;
				for(int i = pos ; i < right ; i++ ){
					swap(i,i+1);
				}
				right--;
			}
		}
		printf("Case #%d: %d\n",e+1,ans);
	}
}
