/*
 *Aditya Gourav @ adi.pearl
 */
#include<bits/stdc++.h>
using namespace std;

#define R(f) freopen(f,"r",stdin);
#define W(f) freopen(f,"w",stdout);
#define TEST int num_cases; cin>>num_cases;for(int case_id=1;case_id <= num_cases;++case_id)

typedef unsigned long long ull;

/** Main Code starts here :) **/
ull getComposite(ull n){
    ull r = sqrt(n)+1;
    for(ull i = 2; i <= r; i += (i==2?1:2)){
        if(n%i == 0)
            return i;
    }
    return 0;
}

string toString(int x){
    string res = "";
    while(x){
        res = ((x&1)? "1":"0") + res;
        x >>= 1;
    }
    return res;
}

#define SUBMIT

int main(){

    #ifdef SUBMIT
    R("C-small-attempt1.in");
    W("C-small.txt");
    #endif

    TEST{
        int n,j;
        cin >> n >> j;

        printf("Case #%d:\n", case_id);

        for(int i = (1<<(n-1)); i < (1<<n) && j > 0; ++i){
            if(!(i&1))
                continue;
            vector<ull> divisors;
            for(int base = 2; base <= 10; ++base){
                ull t = 0;
                ull p = 1;
                int x = i;
                while(x){
                    if(x&1)
                        t += p;
                    p *= base;
                    x >>= 1;
                }
                ull div = getComposite(t);
                if(div == 0)
                    break;
                divisors.push_back(div);
            }
            if(divisors.size() == 9){
                cout << toString(i) << " ";
                for(int k = 0; k < divisors.size(); ++k)
                    cout << divisors[k] << " ";
                cout << endl;
                j--;
            }
        }
    }


return 0;
}
