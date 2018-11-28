#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt", "w", stdout);
    int T;
    double c,f,x,pro,cfab,ti,t;
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>c>>f>>x;
        pro=2;
        cfab=0;
        ti=(x/pro)+cfab;
        while(true){
            cfab+=(c/pro);
            pro+=f;
            t=(x/pro)+cfab;
            if(ti>t){
                ti=t;
            }else{
                break;
            }
        }
        printf("Case #%d: %.7f\n",i,ti);
    }
    //fclose(stdout);
    return 0;
}
