/* Abhiruchi Gupta */
#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <climits>
#include <stack>
#include <queue>
//#include <conio.h>
#include <fstream>
using namespace std;
int main()
{
        long long int t, i;
        cin>>t;
        ofstream in;
        in.open("out.txt");
        long long int cnt = 1;
        while (t--) {
                long long int sm;
                string str;
                cin>>sm>>str;
                long long int ppls = str[0] - '0', nn = 0;
                for (i = 1; i <= sm; i++) {
                        if (str[i] - '0' == 0) continue;
                        if (ppls >= i) {
                                ppls = ppls + str[i] - '0';
                        } else {
                                nn = nn + (i - ppls);
                                ppls = ppls + str[i] - '0' + (i - ppls);
                        }
                }
                in<<"Case #"<<cnt<<": " <<nn<<endl;
                cnt++;
        }
        in.close();









 //getch();
 return 0;
}
