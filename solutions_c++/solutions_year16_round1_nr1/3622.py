#include <iostream>
#include <string>     // std::string, std::to_string
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;


string winning_word (string inword)
{
    string ans, tmp_str;
    char ch;
    ans = inword[0];
    int count = 0;
    //cout << "begin:" << ans << endl;


    for (auto i: inword)
    {
        //cout << '"' << i ;
        ch = i;
        if (count >0)
        if (i>=ans[0])
            ans = string(&ch) + ans;
        else
            ans = ans + string(&ch);
        //cout << ans << endl;
        count++;
    }

    return ans;
}

int main ()
{

  int CaseCount;
  cin >> CaseCount;

  for (int cc=0; cc<CaseCount ; cc++)
  {
    int number;
    string str;
    cin >> str;


    cout << "Case #" << (cc+1) << ": " ;
    cout <<  winning_word(str);

    cout << endl;
  }



  return 0;
}
