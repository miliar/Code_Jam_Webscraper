#include <iostream>

using namespace std;
string l;

void last(string w){
    l = "";
    for(int i = 0; i < w.length(); i++){
        if(w[i] >= l[0])
            l = w[i] + l;
        else
            l = l + w[i];
    }
}

int main()
{
    int t;
    cin >> t;
    string word;
    for(int i = 1; i <= t; i++){
        cin >> word;
        cout << "Case #" << i << ": ";
        last(word);
        cout << l << endl;
    }
    return 0;
}
