#include <iostream>
#include <algorithm>
#include <stack>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    //t=1;
    for (int i = 1; i <= t; i++) {
        string s;
        cin >> s;
        int a = 0;
        while (!all_of(s.begin(), s.end(), [](char c){return c == '+';})) {

           // cout << s;
            int p = s.length()-1;
          //  cout << "here";
           // cout << p;
            while (s[p] == '+') p--;
          //  cout << "cil" << p;


            //otocim prve pluska ako jeden tah
            int f = 0;
            while (s[f] == '+') {
                s[f] = '-';
                f++;
            }
            if (f != 0) a++;



            stack<char> stack;
            for (int j = 0; j <= p; j++) {
                stack.push(s[j]);
            }
            for (int j = 0; j <= p; j++) {
                s[j] = stack.top();
                stack.pop();
                if (s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
            a++;
        }
        cout << "Case #" << i << ": " << a << endl;
    }
    return 0;
}

//otacam vrch, keby robila problem
//zle
