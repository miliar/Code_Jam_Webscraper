#include <bits\stdc++.h>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <deque>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;
//#define f  cin
//#define ff cout
string arr[4][4] = {{"1" , "i" , "j" , "k"} ,
                     {"i" , "-1" , "k" , "-j"} ,
                     {"j" , "-k" , "-1" , "i"} ,
                     {"k" , "j" , "-i" , "-1"}};
map <string , int> ma;
string fun(string s1 , string s2)
{
    if((s1[0] == '-' && s2[0] != '-')||(s1[0] != '-' && s2[0] == '-'))
        swap(s1 , s2);
    int n = ma[s1];
    int u = -1;
    for(int i = 0; i < 4; i++)
        if(arr[n][i] == s2){
            u = i;
            break;
        }
    if(u == 0)
        return "1";
    else if(u == 1)
        return "i";
    else if(u == 2)
        return "j";
    else if(u == 3)
        return "k";
}
int main()
{
    ios_base::sync_with_stdio(false);
    fstream f("C-small-attempt1.in" , ios::in);
    fstream ff("A-small-attempt0.out" , ios::out);
    int t; f >> t;
    ma["1"] = 0;
    ma["i"] = 1;
    ma["j"] = 2;
    ma["k"] = 3;

    for(int q = 0; q < t; q++)
    {
        bool Oki = false , Okk = false;
        int n , L , c = 0; f >> n >> L;
        string str , s , ans[10005] , ch = "";
        f >> str;
        ch += str[0];
        ans[c++] = ch;
        int SZ = L*n;
        if(ch == "i")
           Oki = true;
        if(ch == "k" && Oki)
            Okk = true;
        for(int i , r = 1; r < SZ; r ++)
        {
            i = r%n;
            int row , col;
            bool mi = (ch[0] == '-');
            if(mi)
                ch.erase(0 , 1);
            row = ma[ch];
            string temp = ""; temp += str[i];
            col = ma[temp];
            ch = arr[row][col];
            if(mi)
            {
                if(ch[0]=='-')
                    ch.erase(0,1);
                else
                {
                    string ch1 = "-";
                    ch1 += ch;
                    ch = ch1;
                }
            }
            ans[c++] = ch;
            if(ch == "i")
               Oki = true;
            if(ch == "k" && Oki)
                Okk = true;
        }
    /*cout << endl;
    for(int i = 0; i < SZ; i ++)
        cout << ans[i] << endl;*/
        string sol = "NO";
        if(ans[SZ-1] == "-1" && Okk)
            sol = "YES";
        ff << "Case #"; ff << q+1; ff << ": "; ff << sol; ff << '\n';
    }
}
