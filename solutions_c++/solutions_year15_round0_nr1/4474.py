#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define f(a,b,c)                for(int a=b;a<c;a++)
#define s(x)                    scanf("%d",&x);
int main(){
	
	int t;
	s(t);
	char a[1000];
	f(i1,1,t+1){
		int len;
		s(len);
		scanf("%s",a);
		int Xtra=0,total=0;
		f(i,0,len+1){
			if(a[i]-'0'){
				if(total<i){
					Xtra += i - total;
					total = i;
				}
			    total += a[i]-'0';
			}
		}
		printf("Case #%d: %d\n",i1,Xtra);
	}
}