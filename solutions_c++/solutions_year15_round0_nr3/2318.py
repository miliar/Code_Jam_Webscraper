#include <stdio.h>
#include <iostream>
#include <deque>
#include <algorithm>
#include <fstream>
#include <vector>

using namespace std;
#ifdef DEBU
#define debug(...) fprintf(stderr, __VA_ARGS__)
std::ofstream cerr("/dev/null", std::ios::out | std::ios::app);
#else
#define debug(...)
#endif

const char *tostr(int q);
class comp{
    public:
        bool operator()(int a, int b){
            return a > b;
        }
};

const int E1 = 1;
const int Ei = 2;
const int Ej = 3;
const int Ek = 4;

int qmul(int a, int b){
    int asign = a > 0 ? 1 : -1;
    int bsign = b > 0 ? 1 : -1;
    if(a / asign == E1 && b / bsign == E1){
        return E1 * asign * bsign;
    }else if(a / asign == E1 && b / bsign == Ei){
        return Ei * asign * bsign;
    }else if(a / asign == E1 && b / bsign == Ej){
        return Ej * asign * bsign;
    }else if(a / asign == E1 && b / bsign == Ek){
        return Ek * asign * bsign;

    }else if(a / asign == Ei && b / bsign == E1){
        return Ei * asign * bsign;
    }else if(a / asign == Ei && b / bsign == Ei){
        return -E1 * asign * bsign;
    }else if(a / asign == Ei && b / bsign == Ej){
        return Ek * asign * bsign;
    }else if(a / asign == Ei && b / bsign == Ek){
        return -Ej * asign * bsign;

    }else if(a / asign == Ej && b / bsign == E1){
        return Ej * asign * bsign;
    }else if(a / asign == Ej && b / bsign == Ei){
        return -Ek * asign * bsign;
    }else if(a / asign == Ej && b / bsign == Ej){
        return -E1 * asign * bsign;
    }else if(a / asign == Ej && b / bsign == Ek){
        return Ei * asign * bsign;

    }else if(a / asign == Ek && b / bsign == E1){
        return Ek * asign * bsign;
    }else if(a / asign == Ek && b / bsign == Ei){
        return Ej * asign * bsign;
    }else if(a / asign == Ek && b / bsign == Ej){
        return -Ei * asign * bsign;
    }else if(a / asign == Ek && b / bsign == Ek){
        return -E1 * asign * bsign;
    }
    printf("error\n\n");
    fprintf(stderr, "error\n\n");
    exit(-1);
    return -1;
}

// return b in ( a * b = res )
int qdiv(int res, int a){
    for(int i = 1; i <= 4; i++){
        if(qmul(a, i) == res){
            return i;
        }
        if(qmul(a, -i) == res){
            return -i;
        }
    }
}
// return a in ( a * b = res )
int qdiv2(int res, int b){
    for(int i = 1; i <= 4; i++){
        if(qmul(i, b) == res){
            return i;
        }
        if(qmul(-i, b) == res){
            return -i;
        }
    }
}


// quot -> bit
int getbit(int q){
    int sign = q > 0 ? 1 : -1;
    int sign2 = q > 0 ? 1 : 0;
    return 1 << (((q / sign) * 2) + sign2);
}

int check(int le, int ri, int mi, std::vector<int> &mul){
    int ll = 1;
    int rr = 1;
    int mm = 1;
    int tot = mul[mul.size() - 1];
    for(int i = 0; i < le; i++){
        ll = qmul(ll, tot);
    }
    for(int i = 0; i < ri; i++){
        rr = qmul(rr, tot);
    }
    for(int i = 0; i < mi; i++){
        mm = qmul(mm, tot);
    }
    // -----ll-----|--f1--|--f2--|-----mm-----|--f3--|--f4--|-----rr-----
    // ll * f1 = i
    // f2 * mm * f3 = j
    // f4 * rr = k
    debug("ll = %d, mm = %d, rr = %d\n", ll, mm, rr);
    bool left_ok = false;
    // find ll * f1 == i at index-i
    for(int i = 0; i < mul.size(); i++){
        if(qmul(ll, mul[i]) == Ei){
            //int d = qdiv(tot, mul[i]);
            //int can = qdiv(1, qmul(d, mm));
            //bit |= getbit(can);
            debug("left : i can at %d\n", i);
            left_ok = true;
            break;
        }
    }
    if(!left_ok){
        return 0;
    }
    bool right_ok = false;
    // find f4 * rr == k at index-i
    for(int i = 0; i < mul.size(); i++){
        int d = qdiv(tot, mul[i]);
        if(qmul(d, rr) == Ek){
            //bit2 |= getbit(mul[i]);
            debug("right: k can at %d\n", i);
            right_ok = true;
        }
    }
#ifdef RESDEB
    return 0;
#endif
    return right_ok;
}

int check2(int le, int ri, std::vector<int> &mul){
    int ll = 1;
    int rr = 1;
    int tot = mul[mul.size() - 1];
    for(int i = 0; i < le; i++){
        ll = qmul(ll, tot);
    }
    for(int i = 0; i < ri; i++){
        rr = qmul(rr, tot);
    }
    debug("ll = %d, rr = %d\n", ll, rr);
    // ll * (-----f1-----|------f2-----|-----f3-----) * rr == -1
    // exp == expected mm
    int exp = qdiv(qdiv2(-1, rr), ll);
    int f1 = qdiv(Ei, ll);
    int f3 = qdiv2(Ek, rr);
    debug("f1 = %d, f3 = %d\n", f1, f3);
    for(int i = 0; i < mul.size(); i++){
        if(mul[i] == f1){
            debug("f1 = %d, found on %d\n", f1, i);
            int d = qdiv(tot, mul[i]);
            for(int j = mul.size() - 1; j >= i + 1; j--){
                int he = qdiv(tot, mul[j]);
                debug("j = %d, he = %d, m:%d\n", j, he, mul[j]);
                if(he == f3){
                    // found!
#ifdef RESDEB
                    printf("resdeb\n");
                    return 0;
#endif
                    return 1;
                }
            }
            // not found
            return 0;
            //bit |= getbit(qdiv(1, mul(d, exp)));
        }
    }
    return 0;
}

const char *tostr(int q){
    int qsign = q > 0 ? 1 : 0;
    int qsign2 = q > 0 ? 1 : -1;
    if(q / qsign2 == E1){
        return qsign ? "1" : "-1";
    }else if(q / qsign2 == Ei){
        return qsign ? "i" : "-i";
    }else if(q / qsign2 == Ej){
        return qsign ? "j" : "-j";
    }else if(q / qsign2 == Ek){
        return qsign ? "k" : "-k";
    }
}


void test(){
    debug("qdiv2 : %s\n", tostr(qdiv2(Ek, 1)));
    debug("qmul: %s\n", tostr(qmul(Ek, 1)));
    return;
    for(int i = 1; i <= 4; i++){
        for(int j = -1; j <= 1; j+=2){
            for(int i2 = 1; i2 <= 4; i2++){
                for(int j2 = -1; j2 <= 1; j2+=2){
                    debug("%s * %s = %s\n", tostr(i * j), tostr(i2 * j2), tostr(qmul(i*j,i2*j2)));
                }
            }
        }
    }
}

int main(int argc, char *argv[]){
    int T;

    test();

    cin >> T;
    for(int tcase = 1; tcase <= T; tcase++){
        long long L, X;
        std::string str;

        cin >> L >> X;
        cin >> str;
        std::vector<int> input;
        for(auto ch : str){
            if(ch == 'i'){
                input.push_back(Ei);
            }else if(ch == 'j'){
                input.push_back(Ej);
            }else if(ch == 'k'){
                input.push_back(Ek);
            }
        }
        std::vector<int> mul;

        int tot = E1;
        mul.push_back(tot);
        for(int i = 0; i < L; i++){
            tot = qmul(tot, input[i]);
            //debug("i = %d, %s -> tot = %s\n", i, tostr(input[i]), tostr(tot));
            mul.push_back(tot);
        }

        // check -1
        int remain = X % 4;
        int all_mul = 1;
        for(int i = 0; i < remain; i++){
            all_mul = qmul(all_mul, tot);
            debug("%d / remain : %s\n", i, tostr(all_mul));
        }
        // always NG -> following code except all_mul == -1
        debug("all_mul is %s\n", tostr(all_mul));
        if(all_mul != -1){
            debug("all_mul is not -1\n");
            cout << "Case #" << (tcase) << ": " << "NO" << endl;
            continue;
        }

        int tmpok = 0;
        for(int le = 0; le < 4; le++){
            for(int ri = 0; ri < 4; ri++){
                int mi = (X - 2 - ri - le) % 4;
                if(le + ri + 2 <= X){
                    // ok
                    debug("pat-a : %d %d %d\n", le, mi, ri);
                    int ok = check(le, ri, mi, mul);
                    if(ok){
                        tmpok = 1;
                        break;
                    }
                }
            }
            if(tmpok){
                break;
            }
        }

        if(tmpok){
            cout << "Case #" << (tcase) << ": " << "YES" << endl;
            continue;
        }
        for(int le = 0; le < 4; le++){
            // always mi == 0
            int ri = (X - 1 - le) % 4;
            if(le + 1 <= X){
                debug("pat-b : %d %d\n", le, ri);
                int ok = check2(le, ri, mul);
                if(ok){
                    tmpok = 1;
                    break;
                }
            }
        }
        if(tmpok){
            cout << "Case #" << (tcase) << ": " << "YES" << endl;
            continue;
        }else{
            cout << "Case #" << (tcase) << ": " << "NO" << endl;
        }

    }

}
