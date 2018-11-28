#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

int t,n,m,ans;
long long p,q;

int get2(long long n){
    int res = 0;
    while(n!=1){
        ++res;
        if(n % 2 != 0) return -1;
        n /= 2;
    }
    return res;
}

int gcd(long long a,long long b){
    if (a % b == 0) return b;
    return gcd(b,a%b);
}

int main(){
    ifstream fin("A-small-attempt3.in");
    ofstream fout("out.txt");
    fin>>t;
    long long pa = 1;
    for (int i = 0; i < 40; ++i)
    {
        pa *=2;
    }
    for (int iii = 0; iii < t; ++iii){
        cout<<"Case #"<<iii+1<<": ";
        fout<<"Case #"<<iii+1<<": ";
        char c;
        fin>>p>>c>>q;
        int temp= gcd(q,p);
        p /= temp;
        q /= temp;
        if (pa % q != 0) {cout<<"impossible"<<endl;fout<<"impossible"<<endl;continue;}
        ans = 1;
        while (p != 1){
            p/=2;
            q/=2;
        }
        while( q != 2){
            q/=2;
            ++ans;
        }
        cout<<ans<<endl;
        fout<<ans<<endl;
    }
    fout.close();
}
