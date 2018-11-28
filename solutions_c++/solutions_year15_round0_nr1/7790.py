#include<iostream>
#include<cstdio>
#include<string>

using namespace std;


int main(){
    freopen("A-large.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int ntest;
    while(cin>>ntest){
        for(int tt=0; tt<ntest; tt++){
            int npeople;
            int nstand = 0;
            int ans = 0;
            string level_state;
            cin >> npeople >> level_state;
            for(int i = 0; i < npeople + 1; i++){
                if(level_state[i] != '0'){
                    if(nstand < i){
                        ans = ans + (i - nstand);
                        nstand = nstand + (i - nstand);
                    }
                    nstand = nstand + (level_state[i] - '0');

                }
            }


            cout << "Case #" << tt+1 << ": " << ans << endl;
        }

    }

    return 0;
}
