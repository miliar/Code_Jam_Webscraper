#include<iostream>
#include<cstring>
using namespace std;

int t,h1,h2,m1[101][101],n,m,m2[101],m3[101],cc;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("b_ans_large.txt","w",stdout);
	cin>>t;
	while(t--){
		scanf("%d%d",&n,&m);
		
		printf("Case #%d: ",++cc);
		
		for(h1=0;h1<n;h1++){
			for(h2=0;h2<m;h2++){
				scanf("%d",&m1[h1][h2]);
			}
		}
		memset(m2,0,sizeof(m2));
		memset(m3,0,sizeof(m3));
		
		for(h1=0;h1<n;h1++)
			for(h2=0;h2<m;h2++)
				m2[h1] = max(m2[h1], m1[h1][h2]);
		
		for(h1=0;h1<m;h1++)
			for(h2=0;h2<n;h2++)
				m3[h1] = max(m3[h1], m1[h2][h1]);
		
		bool ans = 1;
		
		for(h1=0;h1<n;h1++)
			for(h2=0;h2<m;h2++)
				if(!(m2[h1]<=m1[h1][h2]||m3[h2]<=m1[h1][h2]))
					ans = 0;
		printf(ans?"YES\n":"NO\n");
		
	}
	//system("pause");
}
