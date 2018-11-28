#include <cstdio>
#include <vector>
using namespace std;
int ar[128];
int Len,Num;
vector <int> vec;
int main(){
	int tt,Test;
	scanf(" %d",&Test);
	for(tt = 1 ; tt <= Test; tt++){
		printf("Case #%d:\n", tt);
		scanf(" %d %d",&Len,&Num);
		int beg = (1<<(Len-1)) + 1;
		int	end = (1 << (Len)); 
		for(int i = 1 ;Num ;i+=2){
			int n = i;
			int cnt = 0;
			while(n){
				ar[cnt++] = n%2;
				n/=2; 
			}
			while(cnt < Len)
				ar[cnt++] = 0;
			ar[cnt-1] = 1;
			vec.clear();
			for(int base = 2 ; base <= 10 ;base++){
				
				int t = 0;
				for(int j = 2 ; j < 100 ; j++ ){
					int sum = 0;
					for(int k = cnt-1 ; k >=0  ; k--){
						sum = sum * base + ar[k];
						sum %= j;
					}
					if(sum == 0){
						t = j;
						break;
					}
				}
				if(!t) break;
				vec.push_back(t);
			}
			if(vec.size() == 9){
				Num--;
				for(int j = cnt - 1 ; j >= 0 ; j--){
					printf("%d",ar[j]);
				}
				printf(" ");
				for(int i = 0 ; i < vec.size(); i++){
					printf("%d ", vec[i]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}