#include<bits/stdc++.h>
using namespace std;
#define ll long long
template<class T> void debug(T v) {
    for(int i=0;i<(int)v.size();i++)cout << v[i] <<" ";cout<<endl;
}
template<class T> void input(T &v) {
    for(int i=0;i<(int)v.size();i++)cin>>v[i];
}


int main() {

//    freopen("a.in", "r", stdin);
   // freopen("c.out", "w", stdout);
    freopen("c_large.out", "w", stdout);


    printf("Case #1:\n");

    long long n = 32, j = 500, mv = 50;

    for(long long tmask = 1;j && 2*tmask < (1LL<<n); tmask+=2) {
        long long mask = tmask + (1LL<<(n-1));
        vector<long long>mod(11,0), f(11, -1);
        long long base;
        for( base = 2; base <= 10; base++) {

            for(long long div=2; div<mv; div++) {

                mod[ base ] = 0;
                long long p = 1;


                for(long long bit=0; bit<n; bit++) {

                    if( mask & (1LL<<bit)  ) {
                        mod[base] += p;
                        mod[base] %= div;
                    }
                    p *= base;
                    p %= div;
                }

            //    cout << base <<" : " << mod[base] <<endl;

                if( mod[base]==0 )  {
                    f[base] = div;
                    break;
                }

            }

        }
        for( base = 2; base<=10; base++ ) if( f[base]==-1 ) break;
        if( base<=10 ) continue;
        for(long long bit=(n-1); bit>=0;bit--) {
            cout << (bool)( mask & (1LL<<bit) );
        }
        j--;
        for( base = 2; base<=10; base++) cout << " " << f[base]; cout << endl;
    }

    return 0;
}

