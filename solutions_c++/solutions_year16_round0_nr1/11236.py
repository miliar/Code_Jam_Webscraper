#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long int t,number,temp,process;
    ostringstream ss;
    string n;
    set<int> st;
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    char buffer[10000];
    in >> t;
    for(int i = 0; i < t; ++i){
        in >> number;
        if(number == 0){
            out << "Case #" << i + 1 << ": " << "INSOMNIA" << '\n';
            st.clear();
        }
        else{
        for(int j = 1; j < 100000000; ++j){
                    process = number * j;
                    //ss.clear();
                    //ss << process;
                    //n = ss.str();
                    n = itoa(process,buffer,10);
                    cout << n << endl;
                    for(int b = 0; b < n.length(); ++b){
                        temp = n[b] - '0';
                        st.insert(temp);
                    }
                    if(st.size() == 10){
                        out << "Case #" << i + 1 << ": " << process << '\n';
                        st.clear();
                        //ss.clear();
                        break;
                    }
                }
        }
    }

}

