#include<algorithm>
#include<cstdio>
#include<cmath>
#include<iostream>
#include<string.h>
#include<time.h>
#include<queue>
#include<vector>
#include<stack>
#include<map>
using namespace std;
#define ll long long
template <class T>
void read(T &ret)
{
    int f=1; char ch=getchar();
    ret=0;
    while(ch<'0'||ch>'9'){if(ch=='-') f=-f; ch=getchar();}
    while(ch>='0'&&ch<='9'){ret=ret*10+ch-'0'; ch=getchar();}
    ret*=f;
}
const int N=3010;
char s[N];
int A[N];
int main(){
#ifdef gh546
freopen("b.in","r",stdin);
freopen("b.out","w",stdout);
#endif
    int TAT,cas=1;; scanf("%d",&TAT);
    while(TAT--){
        scanf("%s",s);
        int len=strlen(s);
        int L=1000,R=L; A[L]=s[0]-'A';
        for(int i=1;i<len;i++){
            int id=s[i]-'A';
            if(id>=A[L]) A[--L]=id;
            else A[++R]=id;
        }
        printf("Case #%d: ",cas++);
        for(int i=L;i<=R;i++) printf("%c",A[i]+'A');
        printf("\n");
    }
    return 0;
}
