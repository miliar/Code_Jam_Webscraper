#include <iostream>
#include <cstdio>
#include <vector>
#define MAX 19
#define LIM 8000000
#define MAXP 100001000
using namespace std;

long long m[11][MAX];
long long primo[LIM], cuad[LIM];

bool es_primo(long long n){
    for(int cont = 0; cuad[cont] <= n; cont++){
        if(n%primo[cont] == 0){
            return false;
        }
    }
    return true;
}

long long es_primo_div(long long n){
    for(int cont = 0; cuad[cont] <= n; cont++){
        if(n%primo[cont] == 0){
            return primo[cont];
        }
    }
    return 0;
}

void primes(){
    primo[0] = 2;es_primo_div
    primo[1] = 3;
    cuad[0] = 4;
    cuad[1] = 9;
    int cont = 2;
    for(long long i = 5; i < MAXP; i+=2){
        if(es_primo(i)){
            cuad[cont] = i*i;
            primo[cont] = i;
            cont++;
        }
    }
//    cout << primo[cont-1] << endl;
    return;
}

void precalculate(){
    long long sum;
    for(int i = 2; i <= 10; i++){
        sum = 1;
//        cout << i << endl;
        for(int j = 0; j < MAX; j++, sum *= i){
            m[i][j] = sum;
//            cout << sum << " ";
        }
//        cout << endl;
    }
    return;
}

vector<long long> cambio_base(long long n){
    vector<long long> sum(11, 0);
    int cont = 0;
    do{
        if(n&1){
            for(int j = 2; j <= 10; j++){
                sum[j] += m[j][cont];
            }
        }
        cont++;
        n>>=1;
    }while(n > 0);
//    cout << "----------";
    cont = 0;
    vector<long long> resp;
    for(int i = 2; i <= 10; i++){
//        cout << sum[i] << " ";
        long long k = es_primo_div(sum[i]);
//        cout << k << ", ";
        if(k > 0)
            resp.push_back(k);
    }
//    cout << endl;
    if(resp.size() == 9){
        resp.push_back(sum[10]);
        return resp;
    }
    return vector<long long> (1, 0);
}

void solve(long long n, int k){
    long long lim = 1LL<<n, ini, lim_inf = (1LL<<(n-1))+1;
    ini = lim_inf/6;
    ini = 6*ini+3;
//    cout << ini << endl;
    for(long long i = ini; i < lim && k > 0; i+=6){
        vector<long long> v = cambio_base(i);
        if(v.size() >= 9){
            printf("%lld ", v[v.size()-1]);
            for(int j = 0; j < v.size()-1; j++)
                printf("%lld%c", v[j], j+1 == v.size()-1 ? '\n':' ');
            k--;
        }
    }
    return;
}

int main(){
	int n, casos, j;
	primes();
	precalculate();
	cin >> casos;
	for(int i = 1; i <= casos; i++){
		cin >> n >> j;
		printf("Case #%d:\n", i);
		solve(n, j);
	}
	return 0;
}
