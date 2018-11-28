#include <sstream>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
using namespace std;

int main(){
    int n;
    cin >> n;
    int kase=0;
    for(int i=0;i<n;i++){
        string s;
        cin >> s;
        int a[30];
        memset(a,0,sizeof(a));
        for(int i=0;i<s.length();i++)
            a[s[i]-'A']++;
        int x[15];
        memset(x,0,sizeof(x));
       // for(int i=0;i<26;i++)
         //   cout << a[i] << endl;
        x[0]=a[25];
        x[4]=a['U'-'A'];
        x[5]=a['F'-'A']-a['U'-'A'];
        x[2]=a['W'-'A'];
        x[7]=a['V'-'A']-x[5];
        x[3]=a['R'-'A']-x[0]-x[4];
        x[8]=a['H'-'A']-x[3];
        x[6]=a['S'-'A']-x[7];
        x[9]=a['I'-'A']-x[8]-x[6]-x[5];
        int len=s.length();
        len-=4*x[0]+3*x[2]+5*x[3]+4*x[4]+4*x[5]+3*x[6]+5*x[7]+5*x[8]+4*x[9];
        x[1]=len/3;
        cout << "Case #" << ++kase << ": ";
        for(int i=0;i<=9;i++)
            for(int j=0;j<x[i];j++)
                cout << i;
        cout << endl;
    }
}
