#include<cstdio>
int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    
    char save[10][10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    int ss[10][26];
    for(int i=0; i<10; i++){
        for(int j=0; save[i][j]!='\0'; j++) ss[i][save[i][j]-'A']++;
    }
    
    int T;
    char S[2005];
    scanf("%d",&T);
    for(int cases=1; cases<=T; cases++){
        int v[26]={0}, ans[10]={0};
        scanf("%s",S);
        for(int i=0; S[i]!='\0'; i++){
            v[S[i]-'A']++;
        }
        if(v['Z'-'A']){
            ans[0]=v['Z'-'A'];
            v['E'-'A']-=v['Z'-'A'];
            v['R'-'A']-=v['Z'-'A'];
            v['O'-'A']-=v['Z'-'A'];
            v['Z'-'A']=0;
        }
        if(v['X'-'A']){
            ans[6]=v['X'-'A'];
            v['S'-'A']-=v['X'-'A'];
            v['I'-'A']-=v['X'-'A'];
            v['X'-'A']=0;
        }
        if(v['U'-'A']){
            ans[4]=v['U'-'A'];
            v['F'-'A']-=v['U'-'A'];
            v['O'-'A']-=v['U'-'A'];
            v['R'-'A']-=v['U'-'A'];
            v['U'-'A']=0;
        }
        if(v['S'-'A']){
            ans[7]=v['S'-'A'];
            v['E'-'A']-=2*v['S'-'A'];
            v['V'-'A']-=v['S'-'A'];
            v['N'-'A']-=v['S'-'A'];
            v['S'-'A']=0;
        }
        if(v['G'-'A']){
            ans[8]=v['G'-'A'];
            v['E'-'A']-=v['G'-'A'];
            v['I'-'A']-=v['G'-'A'];
            v['H'-'A']-=v['G'-'A'];
            v['T'-'A']-=v['G'-'A'];
            v['G'-'A']=0;
        }
        if(v['V'-'A']){
            ans[5]=v['V'-'A'];
            v['F'-'A']-=v['V'-'A'];
            v['I'-'A']-=v['V'-'A'];
            v['E'-'A']-=v['V'-'A'];
            v['V'-'A']=0;
        }        
        if(v['W'-'A']){
            ans[2]=v['W'-'A'];
            v['T'-'A']-=v['W'-'A'];
            v['O'-'A']-=v['W'-'A'];
            v['W'-'A']=0;
        }
        if(v['I'-'A']){
            ans[9]=v['I'-'A'];
            v['N'-'A']-=2*v['I'-'A'];
            v['E'-'A']-=v['I'-'A'];
            v['I'-'A']=0;
        }
        if(v['O'-'A']){
            ans[1]=v['O'-'A'];
            v['N'-'A']-=v['O'-'A'];
            v['E'-'A']-=v['O'-'A'];
            v['O'-'A']=0;
        }
        ans[3]=v['T'-'A'];
        printf("Case #%d: ",cases);
        for(int i=0; i<=9; i++){
            int tmp=ans[i];
            while(tmp--) printf("%d",i);
        }
        printf("\n");
    }
    return 0;
}
