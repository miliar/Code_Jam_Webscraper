#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<cmath>
#include<ctime>
using namespace std;
int T;
int N, J;
vector<int> prime;
void make_prime_list(int limited){
    int i = 3;
    int count = 1;
    prime.push_back(2);
    while(count < limited){
        int flag = 1;
        for(int j=0; prime[j] <= sqrt(i); j++){
            if (i % prime[j] == 0){
                flag = 0;
                break;
            }
        }
        if (flag){
            prime.push_back(i);
            count++;
        }
        i++;

    }
}
vector<int> big[11][32];
void initializing_big(){
    for(int i=2; i<= 10; i++){
        big[i][0].push_back(1);
        for(int j=1; j<32; j++){
            for(int k=0; k< big[i][j-1].size(); k++){
                if (k < big[i][j].size())
                    big[i][j][k] += big[i][j-1][k] * i;
                else
                    big[i][j].push_back(big[i][j-1][k] * i);
                int l = k;
                while(big[i][j][l] > 9){
                    if (l+1 < big[i][j].size())
                        big[i][j][l+1] += big[i][j][k] / 10;
                    else
                        big[i][j].push_back(big[i][j][k] / 10);
                    big[i][j][l] = big[i][j][l] % 10;
                    l++;
                }
            }
        }
    }
}
void trans(int a[], int i, vector<int>& b){
    b.push_back(0);
    for(int j=0; j<N; j++){
        if (a[j]){
            for (int k=0; k<big[i][j].size(); k++){
                if (k < b.size())
                    b[k] += big[i][j][k];
                else
                    b.push_back( big[i][j][k]);
            }
        }
    }
    int l = 0;
    while(l< b.size()){
        if ( b[l] <= 9) { l++; continue;}
        if (l+1 < b.size())
            b[l+1] += b[l] / 10;
        else
            b.push_back(b[l] / 10);
        b[l] = b[l] % 10;
        l++;
    }
}

int divide(vector<int>& b, int p){
    int tmp = 0;
    int sr = 0;
    for(int i= b.size()-1; i >= 0; i--){
        tmp = tmp * 10 + b[i];
        if (sr <= 1){
            sr = sr * 10 + tmp / p;
        }
        tmp = tmp % p;
    }
    if (tmp > 0 || ( tmp == 0 && sr == 1 ))
        return 0;
    else
        return 1;
}

int solve(int a[], int ans[]){
    vector<int> b;
    for(int i=2; i<=10; i++){
        b.clear();
        trans(a, i, b);
        //cout << i << ": ";
        //for (int j=b.size()-1; j>=0; j--) cout << b[j]; cout << endl;
        int flag = 0;
        for(int j=0; j < prime.size(); j++){
            if (divide(b, prime[j])){
                ans[i] = prime[j];
                flag = 1;
                break;
            }
        }
        if (!flag) return 0;
    }
    return 1;
}
void add1(int a[]){
    a[1]++;
    int l = 1;
    while(l < N-1){
        if (a[l]>1){
            a[l] = 0;
            a[l+1]++;
            l++;
        }
        else
            break;
    }
}
int main()
{
    int limited = 10000;
    //cin >> limited;
    //time_t start = clock();
    make_prime_list(limited);
    //cout << prime[0] << " " << prime[limited-1] << endl;
    //time_t end = clock();
    //cout << (difftime(end,start)*1000)/CLOCKS_PER_SEC << endl;
    initializing_big();
//    for(int i=2; i<11; i++){
//        for(int j=0; j<32; j++){
//            printf("big[%d][%d]: ", i, j);
//            for(int k= big[i][j].size()-1; k>=0; k--){
//                cout << big[i][j][k];
//            }
//            cout << endl;
//        }
//    }


    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    cin>>T;
    int t = 0;
    while(t < T)
    {
        t++;
        printf("Case #%d:\n",t);

        cin >> N >> J;
        int a[32];
        a[0] = 1; a[N-1] = 1;
        for(int i=1; i< N-1; i++) a[i] = 0;
        int n_ans = 0;
        int ans[11];
        while(n_ans < J){

            if (solve(a, ans)){
                n_ans++;
                for(int i=N-1; i>=0; i--) cout << a[i]; cout << " ";
                for(int i=2; i<=9; i++) cout << ans[i] << ' '; cout << ans[10] << endl;
            }
            add1(a);
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

