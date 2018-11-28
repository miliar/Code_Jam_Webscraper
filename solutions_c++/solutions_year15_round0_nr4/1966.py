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



int main()
{
    ios_base::sync_with_stdio(false);
    fstream f("D-small-attempt7.in" , ios::in);
    fstream ff("A-small-attempt0.out" , ios::out);
    int64_t t; f >> t;
    for(int64_t q = 0; q < t; q++)
    {
        int x , r , c;
        string ans;
        f >> x >> r >> c;
        if(x == 1)
        {
            ans = "GABRIEL";
        }
        else if(x == 2)
        {
            if((r*c)%2)
                ans = "RICHARD";
            else
                ans = "GABRIEL";

        }
        else if(x == 3)
        {
            if((r*c)%3)
                ans = "RICHARD";
            else if(r*c == 3)
                ans = "RICHARD";
            else if(r*c == 6)
                ans = "GABRIEL";
            else if(r*c == 9)
                ans = "GABRIEL";
            else if(r*c == 12)
                ans = "GABRIEL";
        }
        else if(x == 4)
        {
            if((r*c)%4)
                ans = "RICHARD";
            else if(r*c == 4)
                ans = "RICHARD";
            else if(r*c == 8)
                ans = "RICHARD";
            else if(r*c == 12)
                ans = "GABRIEL";
            else if(r*c == 16)
                ans = "GABRIEL";
        }
        ff << "Case #"; ff << q+1; ff << ": "; ff << ans; ff << '\n';
    }
}



/*#include <bits\stdc++.h>
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
map <string , int64_t> ma;
int main()
{
    ios_base::sync_with_stdio(false);
    fstream f("C-large.in" , ios::in);
    fstream ff("A-small-attempt0.out" , ios::out);
    int64_t t; f >> t;
    ma["1"] = 0;
    ma["i"] = 1;
    ma["j"] = 2;
    ma["k"] = 3;

    for(int64_t q = 0; q < t; q++)
    {
        bool Oki = false , Okk = false;
        int64_t n , L; f >> n >> L;
        string str, ch = "";
        f >> str;
        ch += str[0];
        if(ch == "i")
           Oki = true;
        if(ch == "k" && Oki)
            Okk = true;
        int64_t SZ = max(n,min((L*n),11*n));
        for(int64_t i , r = 1; r < SZ; r ++)
        {
            i = r%n;
            int64_t row , col;
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
            if(ch == "i")
               Oki = true;
            if(ch == "k" && Oki)
                Okk = true;
        }
        string sol = "NO";
        if(Okk){
            string ans;
            if(L <= 11)
            {
                if(ch == "-1")
                    sol = "YES";
            }
            else
            {
                L -= 11;
                if(ch == "k" && L%2)
                    sol = "YES";
            }
        }
        ff << "Case #"; ff << q+1; ff << ": "; ff << sol; ff << '\n';
    }
}
*/
/*#include <bits\stdc++.h>
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



int main()
{
    ios_base::sync_with_stdio(false);
    fstream f("D-small-attempt4.in" , ios::in);
    fstream ff("A-small-attempt0.out" , ios::out);
    int64_t t; f >> t;
    for(int64_t q = 0; q < t; q++)
    {
        int x , r , c;
        string ans;
        f >> x >> r >> c;
        if(x == 1)
        {
            if((r*c)%2)
                ans = "RICHARD";
            else
                ans = "GABRIEL";
        }
        else if(x == 2)
        {
            if(r*c == 1)
                ans = "GABRIEL";
            else if(r*c == 2)
                ans = "RICHARD";
            else if(r*c == 3)
                ans = "RICHARD";
            else if(r*c == 4)
                ans = "GABRIEL";
            else if(r*c == 6 && r == 2)
                ans = "GABRIEL";
            else if(r*c == 6 && r == 3)
                ans = "RICHARD";
            else if(r*c == 8)
                ans = "GABRIEL";
            else if(r*c == 9)
                ans = "RICHARD";
            else if(r*c == 12)
                ans = "GABRIEL";
            else if(r*c == 16)
                ans = "GABRIEL";
        }
        else if(x == 3)
        {
            if(r*c == 1)
                ans = "GABRIEL";
            else if(r*c == 2)
                ans = "GABRIEL";
            else if(r*c == 3)
                ans = "RICHARD";
            else if(r*c == 4)
                ans = "RICHARD";
            else if(r*c == 6)
                ans = "GABRIEL";
            else if(r*c == 8)
                ans = "GABRIEL";
            else if(r*c == 9)
                ans = "RICHARD";
            else if(r*c == 12)
                ans = "GABRIEL";
            else if(r*c == 16)
                ans = "RICHARD";
        }
        else if(x == 4)
        {
            if(r*c == 1)
                ans = "GABRIEL";
            else if(r*c == 2)
                ans = "GABRIEL";
            else if(r*c == 3)
                ans = "GABRIEL";
            else if(r*c == 4)
                ans = "RICHARD";
            else if(r*c == 6)
                ans = "RICHARD";
            else if(r*c == 8)
                ans = "RICHARD";
            else if(r*c == 9)
                ans = "RICHARD";
            else if(r*c == 12 )
                ans = "GABRIEL";
            else if(r*c == 16)
                ans = "RICHARD";
        }
        ff << "Case #"; ff << q+1; ff << ": "; ff << ans; ff << '\n';
    }
}
/*#include <bits\stdc++.h>
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
map <string , int64_t> ma;
int main()
{
    ios_base::sync_with_stdio(false);
    fstream f("C-large.in" , ios::in);
    fstream ff("A-small-attempt0.out" , ios::out);
    int64_t t; f >> t;
    ma["1"] = 0;
    ma["i"] = 1;
    ma["j"] = 2;
    ma["k"] = 3;

    for(int64_t q = 0; q < t; q++)
    {
        bool Oki = false , Okk = false;
        int64_t n , L; f >> n >> L;
        string str, ch = "";
        f >> str;
        ch += str[0];
        if(ch == "i")
           Oki = true;
        if(ch == "k" && Oki)
            Okk = true;
        int64_t SZ = max(n,min((L*n),11*n));
        for(int64_t i , r = 1; r < SZ; r ++)
        {
            i = r%n;
            int64_t row , col;
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
            if(ch == "i")
               Oki = true;
            if(ch == "k" && Oki)
                Okk = true;
        }
        string sol = "NO";
        if(Okk){
            string ans;
            if(L <= 11)
            {
                if(ch == "-1")
                    sol = "YES";
            }
            else
            {
                L -= 11;
                if(ch == "k" && L%2)
                    sol = "YES";
            }
        }
        ff << "Case #"; ff << q+1; ff << ": "; ff << sol; ff << '\n';
    }
}
*/
