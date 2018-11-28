#include <iostream>
#include <cstdio>
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}

using namespace std;

int main()
{
    freopen ("B-small-attempt0 (1).in", "r", stdin);
    freopen ("porno.txt", "w", stdout);
    int cases=in();
    int tc=1;
    while(cases--){
        int a=in(),b=in(),c=in(),ans=0;
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++){
                if((i&j)<c){ans++;}
            }
        }
    printf("Case #%d: %d\n",tc++,ans);
    }
    return 0;
}
