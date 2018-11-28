#include <iostream>
#include <cstdio>
#include <algorithm>
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}

using namespace std;
double c,f,x,galleta,tiempoaux,sol;
void solve(){
        galleta=2.0,tiempoaux=0.0,sol=0.0;
        cin>>c>>f>>x;
        while(sol<0.0000001){
            if((tiempoaux+(x/galleta))<(tiempoaux+(c/galleta)+(x/(galleta+f)))){
                sol=(tiempoaux+(x/galleta));
            }
            else{
                tiempoaux+=(c/galleta);
            }
            galleta+=f;
        }
        printf("%.7lf\n",sol);
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases=in();
    for(int tc=1;tc<=cases&&printf("Case #%d: ",tc++);)solve();
    return 0;
}
