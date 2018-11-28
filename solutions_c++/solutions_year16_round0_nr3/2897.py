#include<bits/stdc++.h>

typedef long long int lli;

lli v[20],n,j;
char s[400];
lli div(lli a){
    for(lli i=2;i*i<=a;i++){
        if(a%i==0){
            return i;
        }
    }
    return 0;
}
lli conv(char* ss,lli base){
    lli val=0,len=n,mul=1;
    //for(;s[len]!='\0';len++);
    for(lli i=len-1;i>=0;i--,mul*=base){
        if(ss[i]=='1'){
            val+=mul;
        }
    }
    return val;
}
void rec(char* s,lli& j,lli cur){//printf("%s %d\n",s,cur);
    if(j<=0){
        return;
    }
    if(cur==n-1){
        s[cur]='1';
        rec(s,j,cur+1);
        return;
    }
    if(cur<n-1){
        s[cur]='0';
        rec(s,j,cur+1);
        s[cur]='1';
        rec(s,j,cur+1);
        return;
    }
    //printf("%s\n",s);
    lli flag=1;
    for(lli base=2;base<=10;base++){
        v[base]=div(conv(s,base)); //printf("%lld\t",v[base]);
        if(v[base]==0){
            flag=0;
            break;
        }
    }
    if(flag==1){
        printf("%s ",s);
        for(lli base=2;base<=10;base++){
            printf("%lld ",v[base]);
        }
        printf("\n");
        j--;
    }


}

int main(){
    int t;
    scanf("%d",&t);
    for(int ti=1;ti<=t;ti++){
        scanf("%lld %lld",&n,&j);
        s[0]='1';
        printf("Case #%d:\n",ti);
        rec(s,j,1);
    }
    return 0;
}
