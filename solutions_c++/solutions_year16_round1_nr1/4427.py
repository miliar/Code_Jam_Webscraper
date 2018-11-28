#include <bits/stdc++.h>
using namespace std;
int main()
{
int tc;
freopen("k.in", "r", stdin);
freopen("b.out", "w+", stdout);
cin >> tc;
for (int j = 1; j <= tc ; j++)
{
    string str;
    cin >> str;
    string str1,str2;
    for (int i= 1 ; i < str.size(); i++)
    {

        if ((str[i] - 'A') >= (str[0] - 'A'))
            {
             if (i == (str.size() - 1))
               str1 = str[i] + str.substr(0,i) ;
                else
            str1 = str[i] + str.substr(0,i) + str.substr(i+1, str.size() -i -1);
            str = str1;
            str2 = str1;
            str1 = "";
            }


    }
    if (str2 == "") str2 = str;
cout << "Case #" << j << ": " << str2 << endl;


}
return 0;
}
