#include <iostream>
#include <stdint.h>
#include <vector>
#include <set>
using namespace std;
typedef int64_t ll; //PRId64 SCNd64
typedef uint64_t ull;//PRIu64 SCNu64
//x <= 1...1 < 1.2e17 smallest non-trivial divisor
inline ll get_divisor(ll x)
{
    //d > 1 so d*d != d and d < x
    for(ll d = 2; d <= x/d; d++){
        if((x%d) == 0){
            return d;
        }
    }
    return -1;
}
inline ll gcd(ll a, ll b)
{
    while(b){
        ll tmp = a%b;
        a = b;
        b = tmp;
    }
    return a;
}
//N <= 18 base <= 10
inline ll from_mask(ull mask, int base, int N)
{
    //x <= 1...1 < 1.2e17
    ll x = 0;
    for(int i = N - 1; i >= 0; i--){ 
        x *= base;
        if(mask & (1ULL << i)){
            x ++;
        }
    }
    return x;
}
void show(const vector<vector<vector<ull> > > &res, int N, int J)
{
    //J <= res[N].size();
    for(int i = 0; i < J; i++){
        ull mask = res[N][i][0];
        for(int bit = N - 1; bit >= 0; bit --){
            if(mask & (1ULL << bit)){
                cout << 1;
            }else{
                cout << 0;
            }
        }
        for(int j = 1; j < res[N][i].size(); j++){
            cout << " " << res[N][i][j];
        }
        cout << endl;
    }
}
//debug (do not check the size range)
void check(const vector<vector<vector<ull> > > &res)
{
    for(int N = 2; N < res.size(); N ++){
        bool fail = false;
        set<ull> vis;
        set<ull>::iterator it;
        for(int i = 0; i < res[N].size(); i++){
            const vector<ull> &lst = res[N][i];
            ull mask = lst[0];
            //All of these jamcoins must be different
            it = vis.find(mask);
            if(it != vis.end()){
                fail = true;
                cerr << "error: not different" << endl;
                break;
            }
            vis.insert(mask);
            //check first digit and last digit
            ull first = (mask >> (N - 1)) & 1;
            ull last = mask & 1;
            if((first == 0) || (last == 0)){
                fail = true;
                cerr << "error: first last" << endl;
                break;
            }
            for(int base = 2; base <= 10; base ++){
                //divisor <= 11...1 < 1.2e17
                ull divisor = lst[base - 1];
                //r*base <= (divisor - 1)*base < divisor * 10 < 1.2e18 < 1.8e19
                //so just r*base but not r*(base%divisor)
                //ull can > 1.8e19
                ull r = 0;
                for(int i = N - 1; i >= 0; i--){
                    r *= base;
                    r %= divisor;
                    if(mask & (1ULL << i)){
                        r = (r + 1)%divisor;
                    }
                }
                if(r != 0){
                    fail = true;
                    cerr << "error: divisor" << endl;
                    break;
                }
            }
            if(fail){
                cerr << "error at mask " << mask << endl;
                break;
            }
        }
        if(fail){
            cerr << "N = " << N << " fail" << endl;
        }else{
            cerr << "N = " << N << " ok" << endl;
        }
    }
}
int main(int argc, char **argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(15);
    //res[N][i][0]: mask res[N][i][1, 2, ...] divisor in base 2 to 10
    vector<vector<vector<ull> > > res(32 + 1);
    for(int N = 2; N <= 16 - 3; N++){
        cerr << "try N = " << N << endl;
        int m = N - 2;
        uint32_t mask_end = (1UL << m);
        for(uint32_t mask = 0; mask < mask_end; mask++){
            bool fail = false;
            vector<ull> lst;
            //1mask1
            lst.push_back((1UL << (N - 1)) | (mask << 1) | 1);
            for(int base = 2; base <= 10; base++){
                ll x = 1;
                for(int bit = m - 1; bit >= 0; bit--){
                    x *= base;
                    if(mask & (1UL << bit)){
                        x += 1;
                    }
                }
                //lowest 1
                x *= base;
                x += 1;
                ll divisor = get_divisor(x);
                if(divisor == -1){
                    fail = true;
                    break;
                }
                lst.push_back(divisor);
            }
            if(!fail){
                res[N].push_back(lst);
                if(res[N].size() == 500){
                    break;
                }
            }
        }
        //debug
        cerr << "N = " << N << " JMax = " << res[N].size() <<  endl;
        //show(res, N, res[N].size());
    }
    for(int N = 17 - 3; N <= 32; N++){
        //debug
        cerr << "try N = " << N << endl;
        //1X1 0..0 1X1 here we have found 500 masks without adding center zeros.
        //unique mask
        set<ull> vis; //may fail or not
        set<ull>::iterator it;
        for(int NA = 2; NA <= N - 2; NA++){
            int NB = N - NA;
            if((res[NA].size() == 0) || (res[NB].size() == 0)){
                continue;
            }
            //ll > 9e18 1...1 < 1.2e17 < 9e18
            if((NA > 18) || (NB > 18)){
                continue;
            }
            for(int i = 0; i < res[NA].size(); i++){
                ull maska = res[NA][i][0];
                for(int j = 0; j < res[NB].size(); j++){
                    ull maskb = res[NB][j][0];
                    //at most N bits and <= 1..1 < 2^32 
                    ull mask = (maska << (N - NA)) | maskb;
                    it = vis.find(mask);
                    if(it != vis.end()){
                        continue;
                    }
                    vis.insert(mask);
                    //if gcd > 1 and not vis, merge maska and maskb
                    bool fail = false;
                    vector<ull> lst;
                    lst.push_back(mask);
                    for(int base = 2; base <= 10; base ++){
                        //TODO: can be stored and calculated in O(1)
                        ll x = from_mask(maska, base, NA);
                        ll y = from_mask(maskb, base, NB);
                        ll divisor = gcd(x, y);
                        if(divisor == 1){
                            fail = true;
                            break;
                        }//otherwise works even if x == y == gcd(x, x)
                        lst.push_back(divisor);
                    }
                    if(!fail){
                        res[N].push_back(lst);
                        if(res[N].size() == 500){
                            break;
                        }
                    }
                }
                if(res[N].size() == 500){
                    break;
                }
            }
            if(res[N].size() == 500){
                break;
            }
        }
        //debug
        cerr << "N = " << N << " JMax = " << res[N].size() <<  endl;
        //show(res, N, res[N].size());
    }
    check(res);
    //T = 1
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++){
        cout << "Case #" << cas << ":" << endl;
        //N ?<=32 J ?<=500 or just check only (16, 50)/(32, 500)? 
        //do not check corner case such as J == 0?
        int N, J;
        cin >> N >> J;
        if(J > 0){
            if(J > res[N].size()){
                cerr << "J is too large, J = " << J << " res[N] size " << res[N].size() << endl;
            }else{
                show(res, N, J);
            }
        }
    }
    return 0;
}
