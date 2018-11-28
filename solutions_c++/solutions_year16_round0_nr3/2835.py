#include<iostream>
#include<utility>
#include<string>
#include<vector>
#include<math.h>

#define N 33333333
#define L 16
#define J 50

using namespace std;

vector<int> erastotenes(){
    bool* aux = new bool[N+1];
    for (int i = 0; i <= N; i++)
        aux[i] = true;
    aux[0] = false;
    aux[1] = false;
    vector<int> out;
    for (int i = 2; i <= N; i++){
        if (aux[i]){
            for (int j = 2*i; j <= N; j += i)
                aux[j] = false;
            out.push_back(i);
        }
    }
    return out;
}

bool verifyPrime(vector<int> aux, string n){
    long long val;
    int s;
    int* div = new int[9];
    bool out = true;
    bool prime;
    for (int i = 2; i <= 10 && out; i++){
        prime = true;
        val = stoll(n, nullptr, i);
        s = sqrt(val);
        for (int j = 0; j < aux.size() && prime; j++){
            if (aux[j] > s)
                break;
            if (val%aux[j] == 0){
                div[i-2] = aux[j];
                prime = false;
            }
        }
        if (prime)
            out = false;
    }
    if (out){
        cout << n;
        for (int i = 2; i <= 10; i++)
            cout << " " << div[i-2];
        cout << "\n";
        return true;   
    } 
    return false;
}

void exploration(vector<int> aux, string& n, int& k){
    if (k >= J)
        return;
    if (n.size() == L && n[0] == '1' && n[L-1] == '1' && verifyPrime(aux, n))
        k += 1;
    else if (n.size() < L){
        n.push_back('1');
        exploration(aux, n, k);
        n.pop_back();
        n.push_back('0');
        exploration(aux, n, k);
        n.pop_back();
    }
}

int main(){
    ios::sync_with_stdio(false);
    int k = 0;
    string n = "1";
    vector<int> aux = erastotenes();
    cout << "Case #1:\n";
    exploration(aux, n, k);
    return 0;
}
