#include <bits/stdc++.h>

#define forn(i,n) for(int i = 0; i < n; i++)
#define WATCH(x) cout << #x << ": " << x << endl

using namespace std;

void exec(){

    string str, delstack = "";
    vector<short> v;
    cin >> str;

    sort(str.begin(), str.end(), greater<char>());

    int slen = str.length();
    vector<bool> strmask(slen, false);

    forn(i, slen){
        if(str[i] == 'Z' and !strmask[i]){
            v.push_back(0);
            delstack += "ZERO";
        }
        else if(str[i] == 'W' and !strmask[i]){
            v.push_back(2);
            delstack += "TWO";
        }
        else if(str[i] == 'U' and !strmask[i]){
            v.push_back(4);
            delstack += "FOUR";
        }
        else if(str[i] == 'X' and !strmask[i]){
            v.push_back(6);
            delstack += "SIX";
        }
        else if(str[i] == 'G' and !strmask[i]){
            v.push_back(8);
            delstack += "EIGHT";
        }
    }

    sort(delstack.begin(), delstack.end(), greater<char>());
    
    int j = 0;
    forn(i, slen){
        if(delstack[j] == str[i] and !strmask[i]){
            strmask[i] = true;
            j++;
        }
    }

    delstack = "";

    forn(i, slen){
        if(str[i] == 'O' and !strmask[i]){
            v.push_back(1);
            delstack += "ONE";
        }
        else if(str[i] == 'T' and !strmask[i]){
            v.push_back(3);
            delstack += "THREE";
        }
        else if(str[i] == 'F' and !strmask[i]){
            v.push_back(5);
            delstack += "FIVE";
        }
        else if(str[i] == 'S' and !strmask[i]){
            v.push_back(7);
            delstack += "SEVEN";
        }
    }

    sort(delstack.begin(), delstack.end(), greater<char>());
    
    j = 0;
    forn(i, slen){
        if(delstack[j] == str[i] and !strmask[i]){
            strmask[i] = true;
            j++;
        }
    }

    delstack = "";

    forn(i, slen){
        if(str[i] == 'I' and !strmask[i]){
            v.push_back(9);
            delstack += "NINE";
        }
    }

    sort(delstack.begin(), delstack.end(), greater<char>());

    j = 0;
    forn(i, slen){
        if(delstack[j] == str[i] and !strmask[i]){
            strmask[i] = true;
            j++;
        }
    }

    // DEBUG
    // int cont = 0;
    // forn(i, slen){
    //     if(!strmask[i]) cont++;
    // }
    // cout << cont;


    sort(v.begin(), v.end());
    int vlen = v.size();
    forn(i, vlen){
        cout << v[i];
    }
    cout << endl;

}

int main(){

    int testCases;

    cin >> testCases;
    forn(tt, testCases){
        cout << "Case #" << tt + 1 << ": ";
        exec();
    }

    return 0;
}
