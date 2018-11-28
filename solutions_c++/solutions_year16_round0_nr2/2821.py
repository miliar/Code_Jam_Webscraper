#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define D(x) cout << #x << " = " << (x) << endl;
#define all(x) (x).begin(),(x).end()
char s[10000];
int n;

int main()
{
    freopen("/home/khaled/file.in","r",stdin);
    freopen("/home/khaled/file.out","w",stdout);
    int T,tc(1);
    scanf("%d",&T);
    while(T--){
		scanf("%s",s);
		n = (int) strlen(s);
		int ans = 0;

		for(int i=n-1;i>=0;i--){
//			printf("%d = %s\n",i,s);
			if(s[i]=='+') continue;
			if(s[0]=='-'){
				reverse(s,s+i+1);
				for(int j=0;j<=i;j++){
					if(s[j]=='+') s[j] = '-';
					else s[j] = '+';
				}
				ans++;
				continue;
			}
			int j=i-1;
			for(;j>=0;j--)
				if(s[j]=='+')
					break;
			reverse(s,s+j+1);
			for(int k=0;k<=j;k++){
				if(s[k]=='+') s[k] = '-';
				else s[k] = '+';
			}
			reverse(s,s+i+1);
			for(int k=0;k<=i;k++){
				if(s[k]=='+') s[k] = '-';
				else s[k] = '+';
			}
			ans += 2;
		}
		printf("Case #%d: %d\n",tc++,ans);
    }
    return 0;
}



