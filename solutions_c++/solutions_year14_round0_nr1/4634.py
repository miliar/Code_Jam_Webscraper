#include<string>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<set>
using namespace std;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int cases;
	cin>>cases;
	for(int t=1;t<=cases;t++){
		int n,m;
		int a[4][4];
		int b[4][4];
		scanf("%d",&n);
		set<int> se;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				scanf("%d",&a[i][j]);
				if(i==n-1){
					se.insert(a[i][j]);
				}
			}
		scanf("%d",&m);
		int count=0,num=0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				scanf("%d",&b[i][j]);
				if(i==m-1&&se.find(b[i][j])!=se.end()){
					count++;
					num=b[i][j];
				}
			}
			if(count==1)
			printf("Case #%d: %d\n",t,num);
			else if(count>1)
				printf("Case #%d: Bad magician!\n",t);
			else if(count==0)
				printf("Case #%d: Volunteer cheated!\n",t);
	}
}