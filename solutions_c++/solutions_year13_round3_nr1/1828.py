#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
typedef unsigned long long int uli;
const int MX = 100+10;
char word[MX];

bool cons(char ch){
    bool ok = true;
    if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u'){
        ok = false;
    }
    return ok;
}

int main(){
    freopen("asmall.in","r",stdin);
    freopen("asmall.out","w",stdout);
    int T,n;
    scanf("%d",&T);
    for(int c=0;c<T;c++){
        scanf("%s %d",word,&n);
        int len = strlen(word);
        int li = 0, ls = n-1;
        int ncons = 0,ans=0;
        int oli = -1;
        for(int i=0;i<n;i++){
            if(cons(word[i])) ncons++;
        }
        if(ncons==n){
            ans += len-ls;
            oli = li;
        }
        for(int li=1;li<len && li+n-1<len;li++){
            ls = li+n-1;
            if(cons(word[li-1])){
                ncons--;
            }
            if(cons(word[ls])){
                ncons++;
            }
            if(ncons==n){
                //cout<<n<<" cons at "<<li<<";"<<ls<<endl;
                ans += (li-oli)*(len-ls);
                oli = li;
            }
        }
        printf("Case #%d: %d\n",c+1, ans);
    }
    return 0;
}
