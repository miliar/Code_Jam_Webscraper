#include<cstdio>
#include<string>
#include<cstdlib>

using namespace std;

int n;
char s[205];
string pie;

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%s",s);
		pie = s;
		int ans = 0, idx = pie.length();
		for(int j=0;j<pie.length();j++)
			if (pie[j] != '-'){
				idx = j;
				break;
			}
		if (idx != 0) ans++;
		for(int j=idx;j<pie.length()-1;j++){
			if (pie[j] == '+' && pie[j+1] == '-'){
				ans+=2;
			}		
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
}
