#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
const int N=1100;
char ss[N];
int main(){
    #ifdef DouBi
    freopen("in.cpp","r",stdin);
    freopen("out.cpp","w",stdout);
    #endif // DouBi
    int T;scanf("%d",&T);
    int cas=1;
    while(T--){
        scanf("%s",ss);
        string tt="";
        int n=strlen(ss);
        tt=tt+ss[0];
        for(int i=1;i<n;i++){
            string tmp="";tmp+=ss[i];
            if(tmp[0]>=tt[0])tt=tmp+tt;
            else tt=tt+tmp;
        }
        printf("Case #%d: ",cas++);
        cout<<tt;printf("\n");
    }
    return 0;
}
