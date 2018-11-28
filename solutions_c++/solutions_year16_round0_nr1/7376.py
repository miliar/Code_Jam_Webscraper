#include <bits/stdc++.h>

using namespace std;

int main(){
    int t,a;
    long long int n,i,j,value;
    string word;
    cin >> t;
    for(a=0;a<t;a++){
        cin >> n;
        cout << "Case #" << a+1 << ": ";
        if(n==0){
            cout << "INSOMNIA\n";
        } else {
            set<int>group;
            for(i=0;i<=9;i++){
                group.insert(i);
            }
            stringstream S;
            string word;
            i=2;
            value = n;
            while(group.size()>0){
                S.clear();
                S << value;
                S >> word;
                for(j=0;j<word.length();j++){
                    group.erase(word[j]-48);
                }
                if(group.size()>0){
                    value=i*n;
                    i++;
                }
            }
            cout << value << endl;
        }
    }
    return 0;
}
