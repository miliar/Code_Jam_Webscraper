#include<stdio.h>
#include<string.h>
#include<string>
#include<set>
using namespace std;

set<string> st[10];
char s[10][100]={{0}};
int len[10]={0};
int color[10]={0},ccnt[10]={0};
int m,n;
int ans=0, cnt=0;
void f(int idx){
    if(idx == m){
        int i,j,tcnt=n;
        for(i=0;i<n;i++){
            if(ccnt[i] == 0) return;
        }
        string temp;
        for(i=0;i<n;i++) st[i].clear();
        for(i=0;i<m;i++){
            temp.clear();
            for(j=0;j<len[i];j++){
                temp.push_back(s[i][j]);
                if(st[color[i]].find(temp) == st[color[i]].end()){
                    tcnt++;
                    st[color[i]].insert(temp);
                }
            }
        }
        if(tcnt > ans){
            ans = tcnt;
            cnt = 1;
        }
        else if(tcnt == ans){
            cnt++;
        }
        return;
    }
    int i;
    for(i=0;i<n;i++){
        ccnt[i]++;
        color[idx] = i;
        f(idx+1);
        ccnt[i]--;
    }
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,t2;
    scanf("%d",&t2);
    int i,j;
    for(t=1;t<=t2;t++){
        ans = cnt = 0;
        scanf("%d%d",&m,&n);
        for(i=0;i<m;i++){
            for(j=0;j<100;j++) s[i][j] = 0;
        }
        for(i=0;i<m;i++) scanf("%s",s[i]);
        for(i=0;i<m;i++) len[i] = strlen(s[i]);
        f(0);
        printf("Case #%d: %d %d\n",t,ans,cnt);
    }
}
