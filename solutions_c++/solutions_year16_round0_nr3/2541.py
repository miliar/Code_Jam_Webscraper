#include <bits/stdc++.h>

#define verbose 0
#define inf 1e9;
using namespace std;

int N;

void write(int n, vector<vector<long long> > ans){
   ofstream ofs;
   ofs.open ("out.txt", ios_base::app);
   // ofs << fixed << setprecision(6);
   ofs << "Case #" << n << ":" << endl;
   for (int i = 0; i < ans.size(); i++){
       for (int j = 0; j < ans[i].size() - 1; j++){
           ofs << ans[i][j] << " ";
       }
       ofs << ans[i][ans[i].size() - 1] << endl;
   }
   ofs.close();
}

long long get_number(string s, int base){
    long long ret = 1 + (long long) pow(base,N-1);

    for (int i = 0; i < N-2; i++){
        if (s[i] == '1'){
            ret += (long long) pow(base, N-2-i);
        }
    }
    return ret;
}

bool prime(long long n){
    if (n % 2 == 0){
        return false;
    }
    for (long long i = 3; i <= sqrt(n); i++){
        if (n % i == 0){
            return false;
        }
    }
    return true;
}

bool check_base(string s, int base){
    long long n = get_number(s, base);
    if (prime(n)){
        return false;
    }
    else{
        return true;
    }
}

long long get_div(long long n){
    if (n % 2 == 0){
        return 2;
    }
    for (long long i = 3; i <= sqrt(n); i++){
        if (n % i == 0){
            return i;
        }
    }
    cout << "Error" << endl;
    return -1;
}

bool check(string s, vector<vector<long long> > &ret){
    for (int i = 2; i <= 10; i++){
        if (!check_base(s, i)){
            return false;
        }
    }
    // number is okay
    vector<long long> div(10);
    div[0] = get_number(s,10);
    for (int i = 2; i <= 10; i++){
        div[i-1] = get_div(get_number(s,i));
    }
    ret.push_back(div);
    return true;
}

vector<vector<long long> > solve(int J){
    vector<vector<long long> > ret;
    int nbr = 0;
    for (int i = 0; i < N-2; i++){
        string s;
        s.resize(N-2);
        for (int j = 0; j < i; j++){
            s[N-j-3] = '1';
        }
        while (next_permutation(s.begin(), s.end())){
            nbr += check(s, ret);
            if (nbr == J) return ret;
        }
    }
    return ret;
}

int main(void){
   remove("out.txt");
   N = 16;
   write(1, solve(50));
   return 0;
}
