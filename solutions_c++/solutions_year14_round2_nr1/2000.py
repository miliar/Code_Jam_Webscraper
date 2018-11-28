#include<stdio.h>
#include<algorithm>
using namespace std;
struct string
{
	char str[105];
	int num[105];
	int df;
};
string data[105];
int now[105];
int main ()
{
	int T,n;
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		printf("Case #%d: ",_);
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%s",data[i].str);
		}
		for(int i=0;i<n;i++){
			int pos = 0;
			data[i].num[0] = 1;
			for(int j=1;data[i].str[j]!='\0';j++){
				if(data[i].str[j]!=data[i].str[j-1]){
					data[i].str[++pos] = data[i].str[j];
					data[i].num[pos] = 1;
				}
				else{
					data[i].num[pos]++;
				}
			}
			data[i].df = pos+1;
		}
		bool ctn = true;
		for(int i=1;i<n&&ctn;i++){
			if(data[i].df!=data[0].df){
				ctn = false;
				break;
			}
			for(int j=0;j<data[0].df;j++){
				if(data[i].str[j]!=data[0].str[j]){
					ctn = false;
					break;
				}
			}
		}
		int r1,r2,q1,q2,tot,ans = 0;
		if(!ctn){
			printf("Fegla Won\n");
		}else{
			for(int i=0;i<data[0].df;i++){
				tot = 0;
				for(int j=0;j<n;j++){
					now[j] = data[j].num[i];
					tot+=now[j]; 
				}
				r1 = (tot+n-1)/n;
				r2 = tot/n;
				q1 = q2 = 0;
				for(int j=0;j<n;j++){
					 q1 += (now[j]>r1) ?now[j]-r1:r1-now[j];
					 q2 += (now[j]>r2) ?now[j]-r2:r2-now[j];
				}
				ans +=min(q1,q2);
			}
			printf("%d\n",ans);
		}
	}
	return 0;
}
