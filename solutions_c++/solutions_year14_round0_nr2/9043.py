#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<set>
#include<vector>
#include<queue>
#define FOR(i,a,b) for(int i = a; i< b; i++)
#define READ(x) freopen(x,"r",stdin)
#define WRITE(x) freopen(x,"w",stdout)

using namespace std;

int main(){
    READ("Bin.txt");
    WRITE("Bout.txt");
    int test;
    scanf("%d",&test);
    int tc = 1;
    while(test--){
        cout<<"Case #"<<tc++<<": ";
        double c,f,x;
        cin>>c>>f>>x;
        double n = (f*x - 2.0*c - f*c) / (f*c);
        double time = 0.0;
        if(n>=0){
            n=(int)((f*x-2.0*c-f*c)/(f*c));
            FOR(i,0,n+1) time+= c/(2.0 + f*i);
            time+=x/(2.0 + f*(n + 1.0));
        }
        else{
            time = x/2.0;
        }
        printf("%.7lf\n",time);
    }
    return 0;
}
