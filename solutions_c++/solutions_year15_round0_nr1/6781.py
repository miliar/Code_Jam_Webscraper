#include <iostream>
#include <vector>

using namespace std;


int main (){

    int c,c1=0;
    cin>>c;
    while (c--){
        int Sm;
        cin>>Sm;
        vector<int> S (Sm+1);
        char Sk;
        for (int i = 0; i <= Sm;++i ){
            cin>>Sk;
            S[i] = Sk - '0';
        }
        int count = S[0];
        int friends = 0;

        for (int i = 1; i<=Sm;++i){
            if (count>=i){count+=S[i];}
            else if (S[i] != 0){
                friends += (i - count);
                count = i + S[i];
            }
        }

        cout<<"Case #"<<++c1<<": "<<friends<<endl;
    }


    return 0;
}
