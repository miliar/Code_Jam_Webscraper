#include<cstdio>
#include<string.h>
char str[2005];
int n;
int cnt[26];
int ans[10];
int main(){
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int turn=1;turn<=t;turn++){
        for(int i=0;i<=2001;i++) str[i]='\0';
        for(int i=0;i<26;i++){
            cnt[i]=0;
        }
        scanf("%s",str);
        n=(int)strlen(str);
        for(int i=0;i<n;i++){
            cnt[str[i]-'A']++;
        }
        ans[0]=cnt['Z'-'A'];
        ans[2]=cnt['W'-'A'];
        ans[3]=cnt['H'-'A']-cnt['G'-'A'];
        ans[4]=cnt['U'-'A'];
        ans[5]=cnt['F'-'A']-cnt['U'-'A'];
        ans[6]=cnt['X'-'A'];
        ans[7]=cnt['S'-'A']-cnt['X'-'A'];
        ans[8]=cnt['G'-'A'];
        ans[1]=cnt['O'-'A']-ans[0]-ans[2]-ans[4];
        ans[9]=(cnt['N'-'A']-ans[1]-ans[7])/2;
        printf("Case #%d: ",turn);
        for(int i=0;i<10;i++){
            for(int j=0;j<ans[i];j++){
                printf("%d",i);
            }
        }
        printf("\n");
    }
}
