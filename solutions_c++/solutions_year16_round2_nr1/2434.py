#include<iostream>
#include<cstdio>
#include<cstring>

#include<algorithm>
#include<cassert>
#include<sstream>
#define FORFROM(var, start, end) for(int var = (start); var < (end); ++var)
#define FOR(var, end) FORFROM(var, 0, end)
#define ALL(x) (x).begin(), (x).end()
using namespace std;

int N[128];
int D[10];
char S[10] = { 'Z', 'O', 'W', 'R', 'U', 'F', 'X', 'S', 'G', 'I'};

string words[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void del_word(int i)
{
    for(auto c: words[i])
    {
	N[c]--;
    }
    D[i]++;
}

string solveCase(){
    memset(N, 0, sizeof(N));
    memset(D, 0, sizeof(D));
    string d;
    cin >> d;
    for(auto c: d)
       N[c]++;
    string result;

    for(int i = 0; i < 10; i+=2)
	while(N[S[i]] > 0)
	    del_word(i);

    for(int i = 1; i < 10; i+=2)
	while(N[S[i]] > 0)
	    del_word(i);

    FOR(i, 10)
	result += string(D[i], '0' + i);

    return result;
}


int main(int argc, char** argv){
    if(argc > 1){
	    freopen(argv[1], "r", stdin);
    }
    int T;
    cin >> T;
    FOR(c, T){
        cout << "Case #" << (c + 1) << ": " << solveCase() << endl;
    }
}
