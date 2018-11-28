#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main(){
    int N, i, j, Cnt, b;
    string K;
    cin >> N;
    for(i=1;i<=N;i++){
        cin >> K;
        Cnt = (K[0] == '-')?1:0;
        b = K[0];
        for(j=1;j<K.length();j++){
            if(K[j] == '-' && b == '+'){
                Cnt+=2;
            }
            b = K[j];
        }
        cout << "Case #" << i << ": " << Cnt<<endl;
    }
}
