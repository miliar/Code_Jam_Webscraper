#include <cstdio>
#include <cstring>
int main()
{
    FILE *fin=fopen("A.in","r");
    FILE *fout=fopen("A.out","w");
    int t,t2;
    fscanf(fin,"%d",&t);
    t2=t;
    while(t--){
        int ans=0,k,len;
        char s[1003];
        fscanf(fin,"%d %s",&len,s);
        len=strlen(s);
        k=s[0]-'0';
        for(int i=1;i<len;i++){
            if(s[i]=='0')continue;
            if(k<i){
                if(ans<i-k)
                    ans=i-k;
            }
            k+=s[i]-'0';
        }
        fprintf(fout,"Case #%d: %d\n",t2-t,ans);
    }
}
