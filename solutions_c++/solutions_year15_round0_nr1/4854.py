#include<cstdio>
#include<cstring>
using namespace std;
int main(){
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    int T,num;
    char s[1010];
    scanf("%d",&T);
    int kase=0;
    while(T--){
	scanf("%d%s",&num,s);
	int len=strlen(s),now=0,ans=0;
	for(int i=0;i<=len;i++){
	    int temp=s[i]-'0';
	    if(i>now){
		ans+=i-now;
		now=i+temp;
	    }else{
		now+=temp;
	    }
	}
	printf("Case #%d: %d\n",++kase,ans);
    }
    return 0;
}

