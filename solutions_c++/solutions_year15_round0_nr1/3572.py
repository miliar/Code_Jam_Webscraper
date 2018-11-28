#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){

    int T;
    cin >> T;

    for(int I=0; I< T; I++){
        int Smax;
        cin >> Smax;

        string S;
        cin >> S;
        long long int n_clapping=0;
        long long int n_friends = 0;
        for(int i=0; i<Smax+1; i++){
            int c = (int)(S[i]-'0');
            //cout << n_clapping <<" "<< i << endl;
            if(n_clapping >= i){
                n_clapping += c;
            } else{
                //cout << "here";
                int new_friends = 0;
                while(n_clapping<i){
                    new_friends++;
                    n_friends++;
                    n_clapping++;
                    //cout << new_friends;
                }
                n_clapping+=c;
            }

        }
        cout << "Case #" << I+1 << ": "<<n_friends <<endl;
    }
}