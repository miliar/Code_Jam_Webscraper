#include<bits/stdc++.h>
using namespace std;
string calc(int lev,int p){
    string k;
    if(p==0)k='1';
    if(p==1)k='0';
    if(p==2)k='2';
    if(lev==0)return k;
    string a=calc(lev-1,p),b=calc(lev-1,(p+2)%3);
    if(a>b)swap(a,b);
    k=a+b;
    return k;
}
main(){
    freopen("A-large.in","r",stdin);
    freopen("pa.txt","w",stdout);
    int T,n,ary[3],i,cas=1;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d%d%d",&n,&ary[1],&ary[0],&ary[2]);
        string a=calc(n,0),b=calc(n,1),c=calc(n,2),ans=".";
        int chk[3]={0};
        for(i=0;i<a.length();i++)chk[a[i]-'0']++;
        if(chk[0]==ary[0]&&chk[1]==ary[1]&&chk[2]==ary[2])
            if(ans=="."||ans>a)ans=a;
        chk[0]=chk[1]=chk[2]=0;
        for(i=0;i<a.length();i++)chk[b[i]-'0']++;
        if(chk[0]==ary[0]&&chk[1]==ary[1]&&chk[2]==ary[2])
            if(ans=="."||ans>b)ans=b;
        chk[0]=chk[1]=chk[2]=0;
        for(i=0;i<a.length();i++)chk[c[i]-'0']++;
        if(chk[0]==ary[0]&&chk[1]==ary[1]&&chk[2]==ary[2])
            if(ans=="."||ans>c)ans=c;
        printf("Case #%d: ",cas++);
        if(ans==".")printf("IMPOSSIBLE");
        else{
            for(i=0;i<ans.length();i++)
                if(ans[i]=='0')printf("P");
                else if(ans[i]=='1')printf("R");
                else printf("S");
        }
        puts("");
    }
}
