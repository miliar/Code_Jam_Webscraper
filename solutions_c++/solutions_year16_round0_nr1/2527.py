#include <iostream>
#include <vector>

using namespace std;

void update(long long int n, vector<bool> &Q){
    long long int k = n;
    while(k != 0){
        Q[k%10] = true;
        k = k/10;
    }
    return;
}

bool find(vector<bool> &Q){
    bool sta = true;
    for (int i=0; i<10; ++i){
        sta = sta && Q[i];
    }
    return sta;
}

long long int f(int n){
    long long int k = n, i=0;
    if (n <= 0) return -1;
    vector<bool> Q(10, false);

    bool sta;

    do{
        update(k, Q);
        sta = find(Q);
        k = k + n;
        i++;
    }
    while(!sta);

    return (k-n);

}

int main(){
    int t; cin>>t;
    int i,j;
    for (int q=1; q<=t; ++q){
        cin>>i;
        j = f(i);
        if(j==-1){
            cout<<"Case #"<<q<<": INSOMNIA"<<endl;
        }
        else{
            cout<<"Case #"<<q<<": "<<j<<endl;
        }
    }
    return 0;
}
