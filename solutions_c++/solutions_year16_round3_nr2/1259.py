      /*  Sourav Verma (Swerve7)
            Code @ CodeJam 2016  */

#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb  push_back
#define mp  make_pair
#define pic pair<int ,char>
#define F  first
#define S  second

/* bool fn1(int b,ll m) {
    ll sum=1;
    for(int i=1;i<=b-2;i++)  sum+=i;
    return sum>=m;
}*/

vector<int> v(55);
int a[55][55];

int main(){
	int tc; scanf("%d",&tc);
	for(int t=1;t<=tc;t++){
		int b;ll m;
		scanf("%d%lld",&b,&m);
     	memset(a,false,sizeof(a));
		v[b-1]=1;
		for(int i=b-2;i>=0;i--){
			v[i]=0;
			for(int j=i+1;j<b;j++){
				if(m>=v[i]+v[j]){
					v[i]+=v[j];
					a[i][j]=1;
				}
			}
		}
		cout<<"Case #"<<t<<": ";
		if(v[0]==m){
			printf("POSSIBLE\n");
			for(int i=0;i<b;i++){
				for(int j=0;j<b;j++){
					printf("%d",a[i][j]);
				}
				printf("\n");
			}
		}
		else printf("IMPOSSIBLE\n");
	}
	// your code goes here
	return 0;
}