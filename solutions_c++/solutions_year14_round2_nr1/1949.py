#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

char s[110][110],c;
bool b[110],go_on;
int len[110],cur[110];

int find(int no,const char *s)
{
    int i,ans=0;
    for(i=cur[no];;i++){
        if(s[i] != c){
            cur[no]=i;
            break;
        }
        ans++;
        if(i==strlen(s)-1){
            b[no]=true;
            go_on=false;
            break;
        }
    }
    if(ans==0)go_on=false;
    return ans;
}

int main()
{
    int N,n,i,j,t,ans,mid;
    double total;
    bool flag;
    scanf("%d",&N);
    for(t=1;t<=N;t++){
        scanf("%d",&n);
        go_on=true;
        flag=true;
        ans=0;
        memset(b,false,sizeof(b));
        memset(cur,0,sizeof(cur));
        for(i=0;i<n;i++){
            scanf(" %s",s[i]);
        }
        while(go_on){
            total=0;
            c=s[0][cur[0]];
            for(i=0;i<n;i++){
                len[i]=find(i,s[i]);
                total+=len[i];
            }
            total=total/n;
            mid=total+0.5;
            for(i=0;i<n;i++){
                ans+=abs(len[i]-mid);
            }
        }
        for(i=0;i<n;i++){
            if(b[i]==false){
                flag=false;
                break;
            }
        }
        printf("Case #%d: ",t);
        if(flag)printf("%d\n",ans);
        else printf("Fegla Won\n");
    }
    return 0;
}
