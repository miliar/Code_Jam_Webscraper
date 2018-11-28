#include <iostream>

using namespace std;
void init();
void read();
void solve();
void print();


int n,sum,total,answer;
string s;



int main()
{
    cin >> n;
    while (n--){
        init();
        read();
        solve();
        print();

    }

    return 0;
}

void init(){
    sum = 0;
    answer = 0;
}
void read(){
    cin >> total >> s;
}
void solve(){
    for (int i = 0; i <= total; i++){
        sum+= s[i]-'0';
        if(sum <= i){
            sum++;
            answer++;
        }
    }
}
void print(){
    static int CASE = 0;
    CASE++;
    cout << "Case #" << CASE << ": " << answer << endl;
}




