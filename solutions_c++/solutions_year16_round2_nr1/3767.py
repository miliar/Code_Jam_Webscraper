#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
bool wayToSort(int i, int j) { return i > j; }
int main() {
freopen("A-small-attempt3.in","r",stdin);
freopen("output.txt","w",stdout);
int t,T;
cin>>t;T = t; long long int len, Len;
string test;
while(t--){
    int alpha[26];
    long long int a[2000],track = 0;
    for(int i=0;i<26;i++) alpha[i]=0;
    cin>>test;
    len = test.length();
    Len = len;
    while(len--) {
        alpha[test[len] - 65] += 1;
        if(test[len] == 'Z') {
            alpha['Z'-65] -= 1;
            alpha['E'-65] -= 1;
            alpha['R'-65] -= 1;
            alpha['O'-65] -= 1;
            a[track] = 0; track ++;
        }
        else if(test[len] == 'W') {
            alpha['W'-65] -= 1;
            alpha['T'-65] -= 1;
            alpha['O'-65] -= 1;
            a[track] = 2; track ++;
        }
        else if(test[len] == 'U') {
            alpha['U'-65] -= 1;
            alpha['F'-65] -= 1;
            alpha['O'-65] -= 1;
            alpha['R'-65] -= 1;
            a[track] = 4; track ++;
        }
        else if(test[len] == 'X') {
            alpha['X'-65] -= 1;
            alpha['S'-65] -= 1;
            alpha['I'-65] -= 1;
            a[track] = 6; track ++;
        }
        else if(test[len] == 'G') {
            alpha['E'-65] -= 1;
            alpha['G'-65] -= 1;
            alpha['I'-65] -= 1;
            alpha['H'-65] -= 1;
            alpha['T'-65] -= 1;
            a[track] = 8; track ++;
        }
    }

    while((alpha['N' - 65]!=0 && alpha['O' - 65]!=0) || (alpha['N' - 65]>=2 && alpha['I' - 65]!=0)) {
        if(alpha['O' - 65]!=0) {alpha['O' - 65]-= 1; alpha['N' - 65] -= 1; alpha['E' - 65] -= 1; a[track] = 1; track ++;}
        else if(alpha['I' - 65]!=0) {alpha['N' - 65]-= 2; alpha['I' - 65] -= 1; alpha['E' - 65] -= 1; a[track] = 9; track ++;}
    }


    while(alpha['E' - 65] != 0 && alpha['S' - 65] != 0 && alpha['V' - 65] != 0 && alpha['N' - 65] != 0)
        {alpha['E' - 65] -= 2; alpha['S' - 65] -= 1; alpha['V' - 65] -= 1; alpha['N' - 65] -= 1; a[track] = 7; track ++;}
    while(alpha['V' - 65]!=0) {
        alpha['F' - 65]-= 1; alpha['I' - 65] -= 1; alpha['V' - 65] -= 1; alpha['E' - 65] -= 1; a[track] = 5; track ++;
    }
    while(alpha['T'-65]!= 0 && alpha['E' - 65] >= 2) {
        alpha['T' - 65]-= 1; alpha['H' - 65] -= 1; alpha['R' - 65] -= 1; alpha['E' - 65] -= 2; a[track] = 3; track ++;
    }
    sort(a, a + track, wayToSort);

    //for(int i=0;i<26;i++) cout<<" "<<alpha[i]<<" ";
    //cout<<endl;
    //while(track--){
      //  cout<<a[track];
    //}
    //cout<<"\n";
    cout<<"Case #"<<T-t<<": ";
    while(track--){
        cout<<a[track];
    }
    cout<<endl;
}
return 0;
}
