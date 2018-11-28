#include <iostream>
#include <cstdlib>
#include <cmath>
long long ans[11];
using namespace std;

long long f(long long a, int j){//dec to j-ary
    long long inc, tmp=0;
    inc = 0;
    while(a >0){
        if (a%10==1) {
            tmp+=pow(j, inc);
        }
        inc++;
        a /= 10;
    }
    return tmp;
}

long long f2(long long bb){// binary to dec
    long long tmp=0, inc=0;
    while(bb>0){
        if(bb%2==1){
            tmp+=pow(10,inc);
        }
        inc++;
        bb /=2;
    }
    return tmp;
}

bool ptest(long long p, int di){//prime test
    long long m;
    m= (long long) pow(p, .5);
    for (int i=2; i <= m; i++){
        if (p% i ==0) {ans[di]=i; return false;}
    }
    return true;
}
//-------------
bool test(long long aa, int n){
    long long na[11];
    int inc[11];
    for(int j=2;j <10;j++) inc[j]=1;
    if(!ptest(aa, 10)){
    for (int j=2; j<10; j++) {
        na[j]=f(aa, j);
        if (ptest(na[j], j)) return false;
    }
    }
    return true;
}

int main(int argc, const char * argv[]) {
    int t, n, j;
    int cnt;
    long long a, da;
    long long ba, ca, tmp;
    cin >> t;
  
    for (int x=1; x <= t; x++){
        cout << "Case #"<<x<<": "<< endl;
        cin >> n >>j ;
        int m;
        m=n;
        if (n > 16) m=16;
        if(m <=16){
            cnt=0;
            a=pow(10, m -1)+1;
            ba=f(a,2);//binary
            for(long long jj=0; ba < pow(2,m ) && cnt <j; jj+=2){
                ba+=jj;;
                da=f2(ba);
                
                if(test(da, m )) {
                    if(n==16){
                        cnt++;
                        cout << da<< " ";
                        //for(int ii=2; ii < 10; ii++) cout << f(da, ii)<< ":"<< ans[ii   ] <<" ";
                        for(int ii=2; ii < 10; ii++)
                            if(f(da, ii)%ans[ii] !=0) cout << "Wrong ";
                        for(int ii=2; ii <10; ii++) cout << ans[ii] <<" ";
                        cout <<ans[10]<<endl;
                                       }
                     else{/*
                         tmp=1;
                         for (int ii=2; ii<=10; ii++) {
                             tmp*=ans[ii];
                         }
                         
                         cnt++;
                         cout << da << da <<" ";
                         for(int ii=2; ii <10; ii++) cout << ans[ii] <<" ";
                         cout <<ans[10]<<endl;
                        */
                    }
        }
            }
     }
    }
 
    return 0;
}
