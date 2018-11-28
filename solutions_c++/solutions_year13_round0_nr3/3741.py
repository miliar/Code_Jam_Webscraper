#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <stdio.h>
#include <cmath>
#include <sstream>

using namespace std;

vector<int> squares;

int str2int(string str)
{
    int i = 0;
    int n = 0;
    while(i < str.size()) {
        n = n*10 + str[i] - '0';
    }
    return n;
}

bool is_pal_str(string str)
{
    int s = str.size();
    for(int i = 0; i < s; i++)
        if(str[i] != str[s - 1 - i]) return false;
    return true;
}

string int2str(int n)
{
   stringstream ss;
   ss << n;
   string res = ss.str();
   return res;
}

bool is_pal(int n)
{
    string str = int2str(n);
    return is_pal_str(str);
}

int main()
{
    for(int i = 1; i*i < 1000; i++) {
        if (is_pal(i) && is_pal(i*i)) squares.push_back(i*i);
    }

    freopen("C-small-attempt0.in","r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    //for(int i = 0; i < squares.size(); i++) cout << squares[i] << endl;

    int T, A, B, count;
    //string line;
    //string num_A, num_B;

    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        scanf("%d %d", &A, &B);
        count = 0;
        int i = 0;
        while(squares[i] < A) i++;
        while(squares[i] <= B) {++i; ++count;}
        printf("Case #%d: %d\n", t, count);
    }


    return 0;
}
