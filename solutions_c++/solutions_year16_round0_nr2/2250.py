//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define LL long long int
int main(void){
    int t,hh;
    scanf("%d",&t);
    for(hh=1;hh<=t;hh++){
		char s[105];
		scanf("%s",s);
		int n=strlen(s);
		int ans=0,i;
		for(i=n-1;i>=0;i--){
			if(s[i]=='+') continue;
			int j,k;
			for(j=0;j<i&&s[j]=='+';j++);
			if(j>0){
				ans++;
				for(k=0;k<j;k++) s[k]='-';
			}
			ans++;
			for(j=0;j<=i/2;j++)
				swap(s[j],s[i-j]);
			for(j=0;j<=i;j++){
				if(s[j]=='-') s[j]='+';
				else s[j]='-';
			}
		}
		printf("Case #%d: %d\n",hh,ans);
	}
    return 0;
}
