#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

bool checkN(bool a[10], long long int m){

    int x;
    while(m){
        x = m%10;
        m/=10;
        a[x] = 1;
    }
    x = 0;
    for(int i=0; i<10; i++){
        if(a[i]==1){
            x++;
        }
    }
    if(x==10)
        return 0;
    else
        return 1;
}

void sleep(long long int n){

    bool a[10], x=1;

    for(int i=0; i<10; i++){
        a[i] = 0;
    }

    long long int m;
    int i=1;
    while(x){
        m=i*n;
        x = checkN(a,m);
        i++;
    }

    cout << m;
}

int main(){

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int t;
    cin >> t;

    long long int n[t];

    for(int i=0; i<t; i++){
        cin >> n[i];
    }

    for(int i=0; i<t; i++){
        cout << "Case #" << i+1 << ": ";
        if(n[i]==0)
            cout << "INSOMNIA";
        else
            sleep(n[i]);

        cout << endl;
    }

    return 0;
}
