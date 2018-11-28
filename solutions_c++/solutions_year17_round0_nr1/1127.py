#include<bits/stdc++.h>
using namespace std;
#define maxn 1005
char s[maxn];
int n,k;
int check(){
    for(int i=1;i<=n;i++){
        if(s[i]=='-') return 0;
    }
    return 1;
}
void foo(int x){
    for(int i=x;i<=x+k-1;i++){
        if(s[i]=='+') s[i]='-';
        else s[i]='+';
    }
}

int main(){
    FILE *fp1=fopen("C:\\Users\\Administrator\\Downloads\\A-large.in","r+");
    FILE *fp2=fopen("C:\\Users\\Administrator\\Downloads\\ans.out","w+");
    int t;
    fscanf(fp1,"%d",&t);
    int ansnum=0;

    while(t--){
        int ans=0;
        fscanf(fp1,"%s",s+1);
        n=strlen(s+1);
        fscanf(fp1,"%d",&k);
        for(int i=1;i<=n-k+1;i++){
            if(s[i]=='+'){
                if(check()){
                    break;
                }
            }
            else{
                foo(i);
                ans++;
                if(check()){
                    break;
                }
            }
        }
        if(check()){
            fprintf(fp2,"Case #%d: %d\n",++ansnum,ans);
        }
        else{
            fprintf(fp2,"Case #%d: IMPOSSIBLE\n",++ansnum);
        }
    }


}
