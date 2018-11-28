#include <bits/stdc++.h>

using namespace std;

void fil(long long num, set<int> & st){
    do{
        st.insert(num%10);
        num /= 10;
    }while(num != 0);
}

int main(){
    int te ;
    cin >> te;
    for(int t = 1 ; t<= te ; t++){
        long long num;
        cin>> num;
        set<int> st;
        int cnt = 0;
        long long orig = num;
        fil(num, st);
        while(st.size() < 10 && cnt < 500){
            num += orig;
            cnt ++;
            fil(num, st);
        }
        if(st.size() == 10){
            cout << "Case #" << t << ": " << num << endl;
        }
        else{
            cout << "Case #" << t << ": " << "INSOMNIA" << endl;
        }
    }
    return 0;
}
