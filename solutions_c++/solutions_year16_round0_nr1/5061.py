#include <bits/stdc++.h>

using namespace std;

int A[10];

void init(){
    for(int i=0; i<10; i++)
        A[i] = 0;
}


int check(){

    for(int i=0; i<10; i++)
        if(A[i] == 0)
            return 0;
    return 1;
}

long long getNumber(long long N){

    int i = 1;
    long long P;
    while(check() == 0){

        P = i * N;
        stringstream st;
        st << P;

        string S = st.str();
        for(int j=0; S[j]!='\0'; j++)
            A[S[j] - 48] = 1;

        i += 1;
    }
    return P;
}


int main(){

    FILE *in = freopen("A-large.in", "r", stdin);
    FILE *out = freopen("A-large.out", "w", stdout);

    assert(in != NULL);

    long T;
    cin >> T;
    assert(T>=1 && T<= 100);
    for(int j=1; j<=T; j++){


        long long N;
        cin>>N;
        assert(N>=0 && N<=1000000);
        init();

        if(N == 0)
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
        else{
            long long X = getNumber(N);
            cout<<"Case #"<<j<<": "<<X<<endl;
        }

    }

    return 0;
}
