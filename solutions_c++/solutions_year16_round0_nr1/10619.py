/*|In The Name Of Allah|*/

#include <bits/stdc++.h>

using namespace std;

int FOUND[10] = {0 , 0, 0, 0, 0, 0, 0, 0, 0, 0};

void COUN(int Number){
     string BB;
     ostringstream AA;
     AA << Number;
     AA.str();
     BB = AA.str();
     for(int i = 0; i < BB.size(); i++){
        if(BB[i] == '0')
            FOUND[9] = 1;
        else
            FOUND[BB[i] - '0' - 1] = 1;
     }
}

int SUM(){
    int aaaa = 0;
    for(int i = 0; i < 10; i++)
       aaaa += FOUND[i];
    return aaaa;
}

int Solve(int N){
    int a = N, ii = 1;
    if(N == 0) return -1;

    for(int i = 0; i < 10; i++)
        FOUND[i] = 0;

    while(1){
        COUN(a * ii++);
        if(SUM() == 10)
            break;
    }
    return ii - 1;

}

int main() {
    freopen("in.txt"  , "a", stdin);
    freopen("out.txt" , "w", stdout);
    int N;
    cin >> N;
    for(int i = 1; i <= N; i++){
        int a;  cin >> a;
        int b = Solve(a);
        if(b == -1)
           cout << "Case #" << i << ": INSOMNIA" << endl;
        else
           cout << "Case #" << i << ": " << b * a << endl;
    }

    return 0;
    //system("PAYSE");
}
