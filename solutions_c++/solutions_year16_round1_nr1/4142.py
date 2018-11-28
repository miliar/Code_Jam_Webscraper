#include <iostream>
#include<string>
using namespace std;

int main() {
  int t;
string str,str1;
char temp;
int i;
  cin >> t;

  for (int j = 1; j <= t; ++j) {
    cin>>str;
    str1.append(1 , str.at(0) ) ;

    for (i = 1 ; i < str.length()  ;i++)
    {
        temp = str1.at(0);

        if (str.at(i) >= temp){

            str1.insert(0,  1,  str.at(i) );

        }

        else{
            str1.append(1,str.at(i));
        }

    }
    cout << "Case #" << j << ": " << str1 << endl;

    str1.clear();
  }
}
