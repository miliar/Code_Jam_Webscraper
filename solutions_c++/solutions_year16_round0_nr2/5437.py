#include<iostream>
#include<string>
#include<map>
#include<climits>

using namespace std;

int cnt;

string reverse(string str, int idx){
    if(idx < 0) return str;
    int i, j;
    for(i = 0, j = idx; i < j; i++, j--){
        char tmp = str[i];
        //cout << "$ "<< str << endl;
        if(str[j] == '+')   str[i] = '-';
        else    str[i] = '+';
        if(tmp == '+')  str[j] = '-';
        else    str[j] = '+';
    }
    //cout << "$ "<< str << endl;
    if(idx %2 == 1) return str;
    if(str[i] == '+')     str[i] = '-';
    else    str[i] = '+';
    return str;
}

int calcMinus(string str, int max, bool mode){
    int n = 0;
    int i = 0;
    if(mode)
        for(i = 0; i <= max && str[i] == '-'; i++);
    else
        for(i = 0; i <= max && str[i] == '+'; i++);
    return i;
}

void calcMoves(string str, int max, bool mode){
    if(max < 0) return;
    int finVal = 0;
    int mov = -1;
    for(int i = -1; i <= max; i++){
        int val = calcMinus(reverse(str, i), max, mode);
        if(val > finVal){
            finVal = val;
            mov = i;
        }
    } 
    if(finVal == 0) return;
    if(mov != -1)   cnt++;
    cnt++;
    calcMoves(reverse(reverse(str, mov), max), max - finVal, mode);
}

int main(){
    int t;
    cin >> t;
    for(int itrS = 0; itrS < t; itrS++){
        string in;
        cin >> in;
        cnt = 0;
        string str;
        char lastCh = in[0];
        str += in[0];
        for(int i = 1; i < in.length(); i++){
            if(lastCh != in[i]) str += in[i];
            lastCh = in[i]; 
        } 
        int len = str.length() - 1;
        int j = len;
        for(; j >= 0 && str[j] == '+'; j--);
        if(j < len)   calcMoves(str, j, true);

        j = str.length() - 1;
        for(; j >= 0 && str[j] == '-'; j--);
        if(j < len){
            calcMoves(str, j, false);
            cnt++;
        }

        cout << "Case #" << itrS + 1 << ": " << cnt << endl;
    }
    return 0;
}
