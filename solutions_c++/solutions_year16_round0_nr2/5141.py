#include <bits/stdc++.h>

using namespace std;

string R;

int check(){

    int flag = 1;
    for(int i=0; i<R.length() - 1; i++){

        if(!(R[i]== R[i+1])) {
            flag = 0;
            for(int j=0; j<=i; j++){
                if(R[i] == '-')
                    R[j] = '+';
                else if(R[i] == '+')
                    R[j] = '-';
            }
            break;
        }
    }
    return flag;
}


int main(){

    FILE *in = freopen("B-large.in", "r", stdin);
    FILE *out = freopen("B-large.out", "w", stdout);

    assert(in != NULL);

    long T;
    cin >> T;
    assert(T>=1 && T<= 100);
    for(int j=1; j<=T; j++){


        string S;
        cin>>S;
        assert(S.length() >= 1 && S.length() <= 100);
        int c = 0, flag = 0;

        R = S;
        if(R.length() == 1 && R[0]=='-')
            c = 1;
        else if(R.length() == 1 && R[0] =='+')
            c = 0;
        else{
            while(check() == 0){
                c += 1;
            }

            if(R[0] =='-')
                c += 1;
        }
        cout<<"Case #"<<j<<": "<<c<<endl;


    }

    return 0;
}
