#include <bits/stdc++.h>

using namespace std;

int main(){

   FILE *in = freopen("A-small-attempt1.in", "r", stdin);
   FILE *out = freopen("A-small-attempt1.out", "w", stdout);

    assert(in != NULL);

    long T;
    cin >> T;
    assert(T>=1 && T<= 50);
    for(int j=1; j<=T; j++){

        long N;
        cin>>N;
        assert(N>=2 && N<=26);

        long A[N], sum = 0, num = 0;
        for(int i=0; i<N; i++){
            cin>>A[i];
            assert(A[i]>=1 && A[i]<=1000);
            sum += A[i];
            num += (10 * num) + A[i];
        }
        string S = "";
        while(sum > 0){
            float half ;

            vector< string > P;
            for(int i=0; i<N; i++){
                string D = "" ;
                D += (char)(i+65);
                P.push_back(D);
                P.push_back(D+D);
            }

            for(int i=0; i<N-1; i++)
            for(int k=i+1; k<N; k++){
                string D = "";
                D += (char)i+65;
                D += (char)k+65;
                P.push_back(D);
            }
            int car = 1;
            for(int i=0; (i<P.size() && car == 1); i++){
                string H = P[i];
                long L[N];
                for(int k=0; k<N; k++)
                    L[k] = A[k];
                for(int k=0; k<H.length(); k++)
                    L[H[k] - 65] -= 1;
                int ss = 0;
                for(int k=0; k<N; k++)
                    ss += L[k];
                half = (float)(ss / 2.0);
              //  cout<<"half : "<<(float)half<<endl;
                int flag = 1;
                for(int k=0;(k<N && flag == 1); k++)
                    if((float)L[k] > half)
                        flag = 0;
                if(flag == 1){
                    S += H + " ";
                 //   cout<<S<<endl;
                    sum -= (H.length());
                    car = 0;
                    for(int k = 0; k<N; k++)
                        A[k] = L[k];
                }
            }
        }

        cout<<"Case #"<<j<<": "<<S<<endl;
    }

    return 0;
}
