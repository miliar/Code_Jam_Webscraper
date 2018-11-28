#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
double c,f,x;

double clicker(double sp,double tm){
    if(c>x)return x/sp;
    if (x/sp>(c/sp)+(x/(sp+f)))return clicker( sp+f, tm+(c/sp));
    return tm + x/sp;
}

int main(){
    int m,n;
    double sp,tm;

    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    m = 1;
    cin>>n;
    while (m != n+1){
        sp = 2.0;
        tm = 0.0;
        cin>>c>>f>>x;
        tm = clicker(sp,tm);
        printf("Case #%d: %7f\n", m, tm);
//        cout<<"Case #"<<m<<": "<<tm<< endl;
        m++;
    }
    return 0;
}
