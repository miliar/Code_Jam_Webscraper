#include<stdio.h>            
#include<stdlib.h>
#include<string.h>

#define SIZE 201

bool valid;
char tmp[SIZE];
int s1[SIZE], s2[SIZE], s3[SIZE], len1, len2, len3, stmp[SIZE];

void SQRT(){

	int tmp1[SIZE], tmp2[SIZE];
	for(int i=0;i<SIZE;++i) tmp1[i] = 0;
	
	int a, b, c, d;
	int top = len1, top2 = 1;
	for(a=(len1-1)/2*2;a>=0;a-=2, ++top2){
		if(top > a + top2 - 2){
			for(b=9;b>=0;--b){	
				for(int i=0;i<SIZE;++i) tmp2[i] = 0;	
				
				tmp1[0] = b;
				for(d=0;d<=top2;++d){
					tmp2[a+d] += (b*tmp1[d]);
					tmp2[a+d+1] += (tmp2[a+d]/10);
					tmp2[a+d]%=10;
				}

				bool find = false;
				for(c=top2+a+1;c>=0;--c){
					if(stmp[c] > tmp2[c]){
						find = true;
						break;
					}
					else if(stmp[c] < tmp2[c]) 
						break;
				}
				
				if(find || c == -1){
					for(c=0;c<=top;++c){
						stmp[c] -= tmp2[c];

						if(stmp[c] < 0){

							int temp=((-stmp[c])/10+((-stmp[c])%10!=0));

							stmp[c] += 10*temp;
							stmp[c+1] -= temp;
						}
					}
					
					break;
				}
			}
		}
		else{ 
			b = 0;
		}
					
		if(a == 0){
			for(c=0;c<=top;++c){
				if(stmp[c] != 0){
					valid = false;
				}
			}
		}

		s3[len3++] = b;
		
		if(top != -1){
			tmp1[0] += b;
			
			for(b=0;b<=top2+1;++b){
				if(tmp1[b]>=10){
					tmp1[b+1] += (tmp1[b]/10);
					tmp1[b] %= 10;
				}
				else break;
			}

			for(b=top2+1;b>=0;--b)     
				tmp1[b+1]=tmp1[b];

			tmp1[0]=0;               

			for(b=top;b>=0;--b){
				if(stmp[b] != 0){
					top = b;
					break;
				}
			}
			
			if(b == -1) top = -1;
		}
	}
}

bool check(int *s, int len){
	for(int i=0;i<len/2;++i){
		if(s[i] != s[len-i-1]){
			return false;
		}
	}
	return true;
}

bool cmp(){
	if(len1 < len2) return true;
	if(len1 > len2) return false;
	for(int i=len1-1;i>=0;--i){
		if(s1[i] < s2[i])  return true;
		if(s1[i] == s2[i]) continue;
		if(s1[i] > s2[i])  return false;
	}
	return true;
}

void add(){
	int i;
	++s1[0];
	for(i=0;i<SIZE-1;++i){
		if(s1[i] >= 10){
			s1[i+1] += (s1[i]/10);
			s1[i] %= 10;
		}
		else break;
	}
	if(i == len1) ++len1;
}

int main(){
    
	int T;
	scanf("%d", &T);
	
	for(int t=1;t<=T;++t){
		scanf("%s", tmp);
		len1 = strlen(tmp);
		for(int i=0;i<SIZE;++i) s1[i] = 0;
		for(int i=0;i<len1;++i)
			s1[i] = tmp[len1-i-1] -'0';
		scanf("%s", tmp);
		len2 = strlen(tmp);
		for(int i=0;i<SIZE;++i) s2[i] = 0;
		for(int i=0;i<len2;++i)
			s2[i] = tmp[len2-i-1] -'0';
		
		int cnt = 0;
		while(cmp()){
			if(check(s1, len1)){
				for(int i=0;i<len1+1;++i){
					stmp[i] = s1[i];
				}
				valid = true;
				len3 = 0;
				SQRT();
				if(valid && check(s3, len3)){
					++cnt;
				}
			}
			add();
		}
		printf("Case #%d: %d\n", t, cnt);
	}
    return 0;
}