#include<iostream>
#include<string>

using namespace std;

int main(){
    int t, case_i;
    cin >> t;
    for(case_i=0; case_i<t;case_i++){
        int smax, friends=0, standing=0;
        string s;
        cin >> smax >> s;
        standing = s[0]-'0';
        for(int i=1; i<=smax;i++){
            if(standing < i && s[i] != '0'){
                friends += i-standing;
                standing = i;
            }
            standing += s[i]-'0';
        }
        cout << "Case #"<<(case_i+1)<<": "<<friends<<endl;
    }
    return 0;
}
