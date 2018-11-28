#include <bits/stdc++.h>

using namespace std;

int main(){

   FILE *in = freopen("A-small-attempt2.in", "r", stdin);
    FILE *out = freopen("A-small-attempt2.out", "w", stdout);

    assert(in != NULL);

    long T;
    cin >> T;
    assert(T>=1 && T<= 100);
    for(int j=1; j<=T; j++){

        string S;
        cin>>S;

        assert(S.length()>=1 && S.length()<= 1000);
     /*   int ij = 0, flag = 0;
        char ch = S[0];
        for(int i=0; i<S.length(); i++)
        if(S[i] > ch){
            ij = i;
            ch = S[i];
        }

        string W = "";
        for(int i=0; i<S.length(); ){
            if(S[i] == ch){
                char R = S[i];
                W = R + W;
                flag = 1;
                i++;
            }
            else{
                if(flag == 0 && S[i] < S[i+1]){
                    char R = S[i+1];
                    W = R + W + S[i];
                    if(S[i]==ch || S[i+1] == ch)
                        flag = 1;
                    i += 2;
                }
                else{
                    W += S[i];
                    i++;
                    }
            }

        } */
        vector< string > A;
        string R = "";
        R += S[0];
        A.push_back(R);
        for(int i=1; i<S.length(); i++){
                int H = A.size();
            for(int k=0; k<H; k++){
                string W = A[k] + S[i];
                A.push_back(W);
                W = S[i] + A[k];
                A.push_back(W);
            }
            A.erase(A.begin(), A.begin() + H);
        }
        sort(A.rbegin(), A.rend());


        cout<<"Case #"<<j<<": "<<A[0]<<endl;
    }

    return 0;
}
