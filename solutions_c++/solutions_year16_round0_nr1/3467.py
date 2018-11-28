#include <bits/stdc++.h>
using namespace std;

bool vis[10];
int lt;

void reset(){
    for(int i=0; i<10; ++i) vis[i] = false;
    lt = 10;
}

void check(long long n){
    long long a = n;
    while(a){
        if(!vis[a%10]) --lt;
        vis[a%10] = true;
        a /=10;
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Aout1.txt","w",stdout);
    int t;
    cin >> t;
    for(int i=0; i<t; ++i){
        reset();
        long long n;
        cin >> n;
        if(n == 0){
            cout << "Case #" << i+1 << ": " <<  "INSOMNIA" << endl;
            continue;
        }
        long long a=1;
        while(lt){
            check(a*n);
            ++a;
            //cout << a*n << " " << lt << endl;
        }
        cout << "Case #" << i+1 << ": " << (a-1)*n << endl;
    }
}
