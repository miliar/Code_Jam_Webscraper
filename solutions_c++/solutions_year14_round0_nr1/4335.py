#include<bits/stdc++.h>
using namespace std;
#define F(n) FO(i,n)
#define FO(i,n) FI(i,0,n)
#define FI(i,f,l) for(int i=(f),ei=(l);i<ei;i++)
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t;cin>>t;
	F(t){
		printf("Case #%i: ",i+1);
		int a[2][4];
		F(2){
			int r;cin>>r;r--;
			FO(j,4){
				if(r==j){
					FO(k,4)cin>>a[i][k];
				}else{
					int t;FO(k,4)cin>>t;
				}
			}
		}
		F(2)sort(a[i],a[i]+4);
		int o[4],*lo;
		lo=set_intersection(a[0],a[0]+4,a[1],a[1]+4,o);
		if(lo-o==1)
			printf("%i\n",o[0]);
		else if(lo-o>1)
			printf("Bad magician!\n");
		else if(lo-o<1)
			printf("Volunteer cheated!\n");
	}
	return 0;
}
