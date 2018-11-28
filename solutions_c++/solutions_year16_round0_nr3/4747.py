#include <bits/stdc++.h>
using namespace std;


bool isprime(long long x){
    for(long long e = 2; e * e <= x; e++){
        if(x % e == 0){
            return false;
        }
    }
    return true;
}
int main(){
    freopen("in.c","r",stdin);
    freopen("on.c","w",stdout);

    int tc , n , cant;
    cin >> tc;
    for(int number_case = 1; number_case <= tc; number_case++){
        cin >> n >> cant;

        vector< vector<long long> > sol(cant , vector<long long>());

        int c = 0;
        for(int mask = 1; mask  < 1<<n && c < cant; mask++){
            int len = 0 , tmp = mask;
            while(tmp > 0){
                tmp/=2;
                len++;
            }
            if(len != n){
                continue;
            }

            if(mask & 1){

                vector<long long> numbers(11 , 0);
                for(int i = 0; i < n; i++){
                    for(int idx = 2; idx <= 10; idx++){
                            numbers[idx] *= idx;
                    }
                    if(mask & (1<<(n - i - 1)) ){
                        for(int idx = 2; idx <= 10; idx++){
                            numbers[idx]++;
                        }
                    }
                }

                bool ok = true;
                for(int idx = 2; idx <= 10; idx++){
                    if(isprime(numbers[idx])){
                        ok = false;
                        break;
                    }
                }

                if(ok){
                    sol[c].push_back(mask);
                    for(int idx = 2; idx <= 10; idx++){
                        sol[c].push_back(numbers[idx]);
                    }
                c++;
                }
            }
        }

        assert(c == cant);

        printf("Case #%d:\n",number_case);
        for(int i = 0; i < cant; ++i){
            long long elem = sol[i][0];
            vector<int> imp;
            while(elem > 0){
                imp.push_back(elem % 2);
                elem/=2;
            }
            reverse(imp.begin() , imp.end());
            for(int ee : imp){
                printf("%d",ee);
            }

            for(int j = 1; j < sol[i].size(); ++j){
                for(long long divisor = 2; divisor < sol[i][j]; divisor++){
                    if(sol[i][j] % divisor == 0){
                        cout <<" "<< divisor ;
                        //printf(" %lld",sol[i][j]);
                        break;
                    }
                }
            }
            printf("\n");
        }
    }





    return 0;
}
