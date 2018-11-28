#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
using namespace std;

int test,row1,row2,ans;
set<int>Hash;

int main(){
	freopen("i.txt","r",stdin);
	scanf("%d",&test);
	for (int testcase=1;test--;testcase++){
		printf("Case #%d: ",testcase);
		scanf("%d",&row1);
		int cnt=0;
		Hash.clear();
		for (int i=1;i<=4;i++){
			for (int j=1;j<=4;j++){
				int x;
				scanf("%d",&x);
				if (i==row1) Hash.insert(x);
			}
		}	
		scanf("%d",&row2);
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++){
				int x;
				scanf("%d",&x);
				if (i==row2){
					if (Hash.count(x)){
						cnt++;
						ans=x;
					}
				}
			}
		if (cnt==1){
			printf("%d\n",ans);
		}else{
			if (cnt==0)
				puts("Volunteer cheated!");
			else
				puts("Bad magician!");
		}
	}
	return 0;
}
