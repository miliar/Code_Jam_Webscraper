#include <cstdio>
#include <iostream>

enum Number{
    One, I, J, K
};

struct Quaternion{
    Quaternion(){}
    Quaternion(Number _n, int _s) : sign(_s), n(_n){}
    inline Quaternion operator*(const Quaternion& rhs) const{
        if(this->n == One && rhs.n == One){
            return {One, this->sign * rhs.sign};
        }else if(this->n == One && rhs.n == I){
            return {I, this->sign * rhs.sign};
        }else if(this->n == One && rhs.n == J){
            return {J, this->sign * rhs.sign};
        }else if(this->n == One && rhs.n == K){
            return {K, this->sign * rhs.sign};
        }else if(this->n == I && rhs.n == One){
            return {I, this->sign * rhs.sign};
        }else if(this->n == I && rhs.n == I){
            return {One, -1 * this->sign * rhs.sign};
        }else if(this->n == I && rhs.n == J){
            return {K, this->sign * rhs.sign};
        }else if(this->n == I && rhs.n == K){
            return {J, -1 * this->sign * rhs.sign};
        }else if(this->n == J && rhs.n == One){
            return {J, this->sign * rhs.sign};
        }else if(this->n == J && rhs.n == I){
            return {K, -1 * this->sign * rhs.sign};
        }else if(this->n == J && rhs.n == J){
            return {One, -1 * this->sign * rhs.sign};
        }else if(this->n == J && rhs.n == K){
            return {I, this->sign * rhs.sign};
        }else if(this->n == K && rhs.n == One){
            return {K, this->sign * rhs.sign};
        }else if(this->n == K && rhs.n == I){
            return {J, this->sign * rhs.sign};
        }else if(this->n == K && rhs.n == J){
            return {I, -1 * this->sign * rhs.sign};
        }else if(this->n == K && rhs.n == K){
            return {One, -1 * this->sign * rhs.sign};
        }
    }
    inline bool operator==(const Quaternion& rhs) const{
        return this->n == rhs.n && this->sign == rhs.sign;
    }
    int sign;
    Number n;
};

inline Quaternion toQ(char c){
    if(c == '1'){return Quaternion{One, 1};}
    else if(c == 'i'){return Quaternion{I, 1};}
    else if(c == 'j'){return Quaternion{J, 1};}
    return Quaternion{K, 1};
}

Quaternion doubling[15][10000];
int D;

// [i, j)
inline Quaternion multiply(int i, int j){
    int l = j - i;
    Quaternion q{One, 1};
    for(int k=0;k<=D;k++){
        if(l >> k & 1){
            q = q * doubling[k][i];
            i += 1 << k;
        }
    }
    return q;
}

const Quaternion PI = {I, 1}, PJ = {J, 1}, PK = {K, 1};

void solve(int t){
    int X, L;
    std::cin >> X >> L;

    std::string S;
    std::cin >> S;

    int N = X * L;
    for(int j=0;j<N;j++){
        doubling[0][j] = toQ(S[j%X]);
    }

    D = 0;
    while((1 << D) < N){++D;}
    
    for(int j=0;j<D;j++){
        int step = 1 << j;
            
        for(int k=0;k<N;k++){
            if(j + 2 * step > N){
                break;
            }

            doubling[j+1][k] = doubling[j][k] * doubling[j][k+step];
        }
    }
    
    for(int j=1;j<N;j++){
        Quaternion q = multiply(0, j);
        
        for(int k=j+1;k<N;k++){
            if(q == PI &&
               multiply(j, k) == PJ &&
               multiply(k, N) == PK){
                std::cout << "Case #" << t << ": YES" << std::endl;
                return;
            }
        }
    }

    std::cout << "Case #" << t << ": NO" << std::endl;
}

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);
    
    int T;
    std::cin >> T;

    for(int i=1;i<=T;i++){
        solve(i);
    }
}
