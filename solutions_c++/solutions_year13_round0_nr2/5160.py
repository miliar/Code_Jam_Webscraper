#include<iostream>
using namespace std;
int n,m;
int a[105][105];
int main(){
	int t;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	cin>>t;
	for(int c=1;c<=t;++c){
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				scanf("%d",&a[i][j]);
		int yes=0;
		for(int i=0;i<n;++i){
			if(yes==2)break;
			yes=0;
			for(int j=0;j<m;++j){
				if(yes==2)break;
				yes=0;
				for(int k=0;k<m;++k)
					if(a[i][k]>a[i][j])
					{
						yes++;
				break;
				}
				for(int k=0;k<n;++k)
					if(a[k][j]>a[i][j])
					{
						yes++;break;
				}
				if(yes==2)
				{
					printf("Case #%d: NO\n",c);
			}
			}}
		if(yes==2)continue;
		printf("Case #%d: YES\n",c);
	}
//	system("pause");
}