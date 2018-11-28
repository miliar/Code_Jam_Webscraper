#include<iostream>
#include<windows.h>
using namespace std;

long long czytajJakoK(int k, int n) {
    long long r = 0;
    long long p = 1;
    while(n>0) {
        r += (n%2)*p;
        p*=k;
        n/=2;
    }
    return r;
}

int A[15];

void preparea () {
    A[0]=2;
    A[1]=3;
    A[2]=5;
    A[3]=7;
    A[4]=11;
    A[5]=13;
    A[6]=17;
    A[7]=19;
    A[8]=23;
    A[9]=29;
    A[10]=31;
    A[11]=37;
    A[12]=41;
    A[13]=43;
    A[14]=47;
}

long long modmulti(long long a, long long b, long long q) //a*b % q
{
    long long m, r=0;
    for(m=1; m; m<<=1)
    {
        if(b & m) r=(r+a)%q;
        a=(a<<1)%q;
    }
    return r;
}

long long modexpo(long long a, long long k, long long q) {
    if (k==0)
        return 1;

    if (k%2==0)
    {
        long long w=modexpo(a,k/2,q);
        return modmulti(w, w, q);
    }
    else
    {
        long long w=modexpo(a,k-1,q);
        return modmulti(w, a, q);
    }
}

bool sprawdz_mi_kocie_czy_jest_pierwsza_prosze(long long g) {
    if(g == 1) return false;
    long long x, d=g-1, a;
    int s=0;
    bool check=true;
    while(d%2==0)
    {
        d/=2;
        s++;
    }

    for(int nn=0; nn<=14 ; nn++)
    {
        a=A[nn];
        if(g==a) return true;
        x=modexpo(a, d, g);

        if( x!=1 && x!=g-1)
        {
            for(int i=1; i<s && x!=g-1; i++)
            {
                x=modmulti(x, x, g);
                if(x==1)
                {
                    check=false;
                    break;
                }
            }
            if(!check) break;
            if(x!=g-1)
            {
                check=false;
                break;
            }
        }
    }
    return check;
}

void czytaj(int N, int i) {
    while(N>0) {
        cout<<(( (1<<(N-1)) & i)!=0);
        N--;
    }
    cout<<" ";
}

long long getdiv(long long n) {
    long long a = 2;
    while (a*a <= n) {
        if(n%a == 0) return a;
        a++;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    preparea();
    int T;
    cin>>T;
    for(int tt=1; tt<=T; tt++) {
        cout<<"Case #"<<tt<<": "<<endl;
        int N, J;
        cin>>N>>J;
        long long a;
        int c = 0;
        bool f = false;
        //wszystkie ciagi N zer i jedynek
        for(int i=1; i<=(1<<N); i++) {
            if( !(i & 1) || !(i & (1<<N-1)) ) continue;
            for(int j=2; j<=10; j++) {
                f = true;
                a = czytajJakoK(j, i);
                if(sprawdz_mi_kocie_czy_jest_pierwsza_prosze(a)) {
                    f = false;
                    break;
                }
              //  cout<<i<<endl;
            }
            if(f) {
                czytaj(N, i);
                for(int j=2; j<=10; j++)
                    cout<<getdiv(czytajJakoK(j, i))<<" ";
                cout<<endl;
                c++;
            }
            if(c>=J) break;
        }
       // cout<<c<<endl;

    }
    return 0;
}
