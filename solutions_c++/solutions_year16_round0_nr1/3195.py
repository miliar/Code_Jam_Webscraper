#include<iostream>

using namespace std;

bool A[10];

void check(int n) {
    while(n>0) {
        A[n%10]=true;
        n/=10;
    }
    return;
}

bool check2() {
    for(int i=0; i<=9; i++)
        if(!A[i])
            return false;
    return true;
}

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    for(int tt=1; tt<=T; tt++) {
        cout<<"Case #"<<tt<<": ";
        int N;
        for(int i=0; i<=9; i++)
            A[i]=false;
        cin>>N;
        if(N==0) {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        int i = 1;
        while(i != 0) {
            check(N*i);
            if(check2())
                break;
            i++;
        }
        cout<<N*i<<endl;
    }
    return 0;
}
