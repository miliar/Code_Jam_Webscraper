#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
#include<string>
using namespace std;
string arr[10];
vector<string> str[10];
char s[15];
int val=-1,cnt=0,n,m;
int cal(vector<string> tt){
    int tmp=1,i,j;
    sort(tt.begin(),tt.end());
    string pre="";
    for(i=0;i<tt.size();i++){
        for(j=0;j<pre.size() && j<tt[i].size();j++){
            if(pre[j]!=tt[i][j] || j==pre.size() || j==tt[i].size()) break;
        }
        //printf("%d...",j);
        tmp+=tt[i].size()-j;
        pre=tt[i];
    }
    return tmp;
}
void dfs(int a){
    int i,j;
    if(a==n){
        int flag=1;
        for(i=0;i<m;i++){
            if(str[i].size()==0){
                flag=0;
                break;
            }
        }
        if(!flag) return;
        int tmp=0;
        for(i=0;i<m;i++){
            tmp+=cal(str[i]);
        }
        if(val==-1 || tmp>val){
            val=tmp;
            cnt=0;
        }
        /*if(val==11 && cnt==1){
            for(i=0;i<m;i++){
                for(j=0;j<str[i].size();j++)
                    puts(str[i][j].c_str());
                puts(">");
            }
        }*/
        if(tmp==val) cnt++;
        return;
    }
    for(i=0;i<m;i++){
        str[i].push_back(arr[a]);
        dfs(a+1);
        str[i].pop_back();
    }
}
int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    vector<string> tttt;
    tttt.push_back("AAB");
    tttt.push_back("B");
    printf("%d..",cal(tttt));
    int t,i,j,ans,C=0,l,r;
    scanf("%d",&t);
    while(t--){
        val=-1;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++){
            scanf("%s",s);
            arr[i]=string(s);
        }
        dfs(0);
        printf("Case #%d: %d %d\n",++C,val,cnt);
    }
}
