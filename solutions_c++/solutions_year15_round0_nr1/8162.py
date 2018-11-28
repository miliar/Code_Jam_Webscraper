#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
   // freopen("A-large.in","r",stdin);
   // freopen("izlaz.txt","w",stdout);
    int t,s;
    scanf("%d",&t);
    for(int t1=0;t1<t;t1++){
        scanf("%d",&s);
        char ni[s+5];
        scanf("%s",ni);
        int nov=0,tr=0;
        int niz[s+1];
        for(int i=0;i<=s;i++){
            niz[i]=(int)(ni[i]-'0');
        }
        tr=niz[0];
        for(int i=1;i<=s;i++){
            if(i>tr){
                nov+=(i-tr);
                tr+=(i-tr);
                tr+=niz[i];
            }else{
                tr+=niz[i];
            }
        }
        printf("Case #%d: %d\n",(t1+1),nov);
    }
    return 0;
}
