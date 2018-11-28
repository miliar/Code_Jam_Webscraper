#include <bits/stdc++.h>

using namespace std;

const char let[] = {'R' , 'P' , 'S'};

string answer , tmp;
int no[309];
int v[3] , r , p , s , n , T , test , i;

string walk(int cnt , int round)
{
    if (round == n)
    {
        string aux;
        aux.clear();
        aux.push_back(let[cnt]);
        return aux;
    }

    if (cnt == 0)
    {
        string a = walk(0 , round + 1);
        string b = walk(2 , round + 1);
        if (a + b < b + a) return a + b;
        return b + a;
    }

    if (cnt == 1)
    {
        string a = walk(1 , round + 1);
        string b = walk(0 , round + 1);
        if (a + b < b + a) return a + b;
        return b + a;
    }

    if (cnt == 2)
    {
        string a = walk(1 , round + 1);
        string b = walk(2 , round + 1);
        if (a + b < b + a) return a + b;
        return b + a;
    }
}

int main()
{
freopen("test.in" , "r" , stdin);
freopen("test.out" , "w" , stdout);

no['R'] = 0;
no['P'] = 1;
no['S'] = 2;

cin >> T;
for (test = 1 ; test <= T ; ++test)
{
    cin >> n >> r >> p >> s;
    answer = "z";
    // rock 0
    // paper 1
    // scissors 2

    tmp = walk(0 , 0);

    v[0] = v[1] = v[2] = 0;
    for (i = 0 ; i < tmp.size() ; ++i)
    v[no[tmp[i]]]++;

    if (r == v[0] && p == v[1] && s == v[2])
    if (answer > tmp) answer = tmp;

    tmp = walk(1 , 0);

    v[0] = v[1] = v[2] = 0;
    for (i = 0 ; i < tmp.size() ; ++i)
    v[no[tmp[i]]]++;

    if (r == v[0] && p == v[1] && s == v[2])
    if (answer > tmp) answer = tmp;

    tmp = walk(2 , 0);

    v[0] = v[1] = v[2] = 0;
    for (i = 0 ; i < tmp.size() ; ++i)
    v[no[tmp[i]]]++;

    if (r == v[0] && p == v[1] && s == v[2])
    if (answer > tmp) answer = tmp;

    cout << "Case #" << test << ": ";
    if (answer == "z") cout << "IMPOSSIBLE\n";
    else cout << answer << '\n';
}

return 0;
}
