#include <bits/stdc++.h>
using namespace std;

unsigned int N, J, T;

int main()
{
    ifstream cin("1A-A-large.in");
    ofstream cout("1A-A-large.txt");

    cin >> T;
    string Si;
    for(int t=1; t<=T; t++){ //combinaciones
        cin >> Si;
        vector<char> So;
        So.push_back(Si[0]);
        for(int i=1; i<Si.length(); i++){
            if(Si[i] >= So[0]){
                vector<char>::iterator it = So.begin();
                So.insert(it, Si[i]);
            } else {
                So.push_back(Si[i]);
            }
        }
        cout << "Case #" << t << ": ";
        for(int i=0; i<So.size(); i++){
            cout << So[i];
        }
        cout << "\n";
    }


    return 0;
}
