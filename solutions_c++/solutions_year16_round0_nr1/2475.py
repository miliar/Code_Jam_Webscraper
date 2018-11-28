#include<bits/stdc++.h>

using namespace std;

#define pii pair<int,int>
#define ll long long
#define N (int)(1e5+10)
#define mod 1000000007
#define mp make_pair
#define pb push_back
#define nd second
#define st first
#define inf mod
#define endl '\n'
#define sag (sol|1)
#define sol (root<<1)
#define ort ((bas+son)>>1)
#define bit(x,y) ((x>>y)&1)

int main(){
	int i,j,k,n,m,x,y,z,t,H[15];
	cin >> t;
	for(i=1 ; i<=t ; i++){
		scanf("%d",&n);
		printf("Case #%d: ",i);
		bool w=0;
		int s=0;
		memset(H,0,sizeof H);
		for(j=1 ; !w and j<=1000 ; j++){
			int x = j*n;

			while(x){
				if(!H[x%10]){
					s++;
					H[x%10]=1;
				}
				x/=10;
			}
			if(s == 10)
				w=1;
		}
		if(w)
			printf("%d\n",(j-1)*n);
		else
			puts("INSOMNIA");
	}
}
