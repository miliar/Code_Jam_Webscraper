#include<iostream>
#include<climits>
using namespace std;

int mark[11];

bool updateMarker(long long N) {
	int x=0;
    while(N>0) {
        x=N%10;
        mark[x]=1;
        N/=10;
    }
    int cnt=0;
    for(int i=0;i<=9;i++) {
	if(mark[i]==1)
	   cnt++;
    }
    if(cnt==10)
		return true;
    else
		return false;
}

int main() {
    freopen("A-large.in","rb",stdin);
    freopen("A-large.out","wb",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++) {
        memset(mark,0,sizeof mark);
        long long int N;
		int flag=1;
        scanf("%lld",&N);
        printf("Case #%d: ",i);
		for(int k=1;flag;k++)
        	if(N==0) {
	            printf("INSOMNIA");
	            flag=0;
	        } else {
    	        if(updateMarker(k*N)==true) {
					printf("%lld",k*N);
					flag=0;
    	        }
	        }
			printf("\n");
    	}
    return 0;
}
