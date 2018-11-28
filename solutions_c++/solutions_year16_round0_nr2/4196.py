#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAX_LEN=110;

int T,cases=0;
char s[MAX_LEN];
int data[MAX_LEN];

int main()
{
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("Bout.txt","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%s",s);
		int len=strlen(s);
		for(int i=0;i<len;i++){
			if(s[i]=='+') data[i]=1;
			else data[i]=0;
		}
		int ans=0;
		for(int i=len-1;i>=0;i--){
			if(data[i]==0){
				ans++;
				for(int j=i;j>=0;j--){
					data[j]=(data[j]+1)&1;
				}
			}
		}
		printf("Case #%d: %d\n",++cases,ans);
	}
	return 0;
}
