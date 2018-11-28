#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define f(a,b,c)                for(int a=b;a<c;a++)
#define s(x)                    scanf("%d",&x);
int main(){
	int t;
	s(t);
	int a[10000];
	f(i1,1,t+1){
		int n,maxv=-100;
		s(n);
		f(i,0,n) {
			s(a[i]);
			if(a[i]>maxv) maxv = a[i];
		}
		int total = maxv;
		f(i,1,maxv+1){
			int temp1=0,temp2=0;
			f(j,0,n){
				if(a[j]>i){
					if(i>temp2) temp2 = i;
					temp1 += a[j]/i;
					if(a[j]%i == 0) temp1--;
					
				}
				else if(a[j]>temp2) temp2 = a[j];
				
			}
			temp1+=temp2;
			if(temp1<total) total = temp1;
			//cout<<i<<" "<<temp1<<endl;
		}
		printf("Case #%d: %d\n",i1,total);
	}
}