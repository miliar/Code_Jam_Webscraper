#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;
char s[105];
int n, m, tests, id;
int main()
{   freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>tests;
    for(id=1; id<=tests; id++){
            cin>>s;
        cout<<"Case #"<<id<<": ";

        m = 0;
        n = strlen(s);
        s[n] = '+';
        for(int i=0; i<n; i++){
            if(s[i]!=s[i+1])    m++;
        }
        cout<<m<<endl;
    }

   // cout << "by Qalib" << endl;
    return 0;
}
