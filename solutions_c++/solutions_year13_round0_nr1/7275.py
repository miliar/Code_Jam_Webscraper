#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <string>
#include <cmath>
#include <stdio.h>
#include <map>
#include <stack>
#include <fstream>
#define SZ(a) (int)a.size()
#define SS stringstream
#define all(a) (a).begin(),(a).end()
#define rll(a) (a).rbegin(),(a).rend()
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

using namespace std;



int main()
{
    READ("A-large.in");
    WRITE("A-large.out");
    int t;
    string S,z1,z2;
    cin >> t;
    for (int i = 0;i < t;i ++){
        int dot = 0;
        bool check = 0;
         vector <string> s;
         z1.clear();z2.clear();
        for (int x = 0;x < 4;x ++){
            cin >> S;
            z1 += S[x];
            z2 += S[3 - x];
            s.push_back(S);
            }
           if (count(all(z1),'X') == 3 && count(all(z1) , 'T') == 1 || count(all(z1),'X') == 4)
                {cout<<"Case #"<<i + 1<<": X won"<<endl;continue;}
            else if (count(all(z1),'O') == 3 && count(all(z1) , 'T') == 1 || count(all(z1),'O') == 4)
                {cout<<"Case #"<<i + 1<<": O won"<<endl;continue;}
            else if (count(all(z2),'X') == 3 && count(all(z2) , 'T') == 1 || count(all(z2),'X') == 4)
                {cout<<"Case #"<<i + 1<<": X won"<<endl;continue;}
            else if (count(all(z2),'O') == 3 && count(all(z2) , 'T') == 1 || count(all(z2),'O') == 4)
                {cout<<"Case #"<<i + 1<<": O won"<<endl;continue;}
        for (int I = 0;I < 4;I ++){
            int O1 = 0,X1 = 0,T1 = 0,O2 = 0,X2 = 0,T2 = 0;
        check = 0;
            for (int z = 0;z < 4;z ++){
                if (s[I][z] == 'O')O1++;
                else if (s[I][z] == 'X')X1 ++;
                else if (s[I][z] == 'T')T1 ++;
                if (s[z][I] == 'O')O2++;
                else if (s[z][I] == 'X')X2 ++;
                else if (s[z][I] == 'T')T2 ++;
                else dot ++;
                }

        if ((X1 == 3 && T1 == 1) || X1 == 4){cout<<"Case #"<<i + 1<<": X won"<<endl;check = 1;break;}
        else if ((O1 == 3 && T1 == 1) || O1 == 4){cout<<"Case #"<<i + 1<<": O won"<<endl;check = 1;break;}
        else if ((X2 == 3 && T2 == 1) || X2 == 4){cout<<"Case #"<<i + 1<<": X won"<<endl;check = 1;break;}
        else if ((O2 == 3 && T2 == 1) || O2 == 4){cout<<"Case #"<<i + 1<<": O won"<<endl;check = 1;break;}
        }
        if (dot > 0 && check == 0)cout<<"Case #"<<i + 1<<": Game has not completed"<<endl;
        else if (check == 0) cout<<"Case #"<<i + 1<<": Draw"<<endl;
        }
    return 0;
}
