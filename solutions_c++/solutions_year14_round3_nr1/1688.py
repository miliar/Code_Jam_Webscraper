#include <fstream>
using namespace std;



ifstream cin ("Lol01.txt");
ofstream cout ("Sol00.txt");

int T;
long long int P,Q;

long long int gcd(int a,int b){
    if(b%a) return gcd(b%a,a);
    else return a;
}

int solve(long long int a,long long int b){
    //cout << a << " " << b << endl;
    int sol=1;
    long long int g=gcd(a,b);
    //cout << g << endl;
    a/=g; b/=g;
    //cout << a << " " << b << endl;
    while(sol<=40){
        a*=2; g=gcd(a,b);
        a/=g; b/=g;
        //cout << a << " " << b << endl;
        long long int t=1;
        while(t<b && b%t==0) {t*=2;}
        if(t != b) return 41;
        if(a>=b) return sol;
        sol++;
    }

    return sol;
}


int main(){
    cin >> T;
    int k=1;
    char c;
    while(T--){
        cin >> P >> c >> Q;
        //cout << P << " " << Q << endl;
        int sol = solve(P,Q);
        cout << "Case #" << k << ": ";
        k++;
        if(sol>40) cout << "impossible" << endl;
        else cout << sol << endl;
    }
    return 0;
}
