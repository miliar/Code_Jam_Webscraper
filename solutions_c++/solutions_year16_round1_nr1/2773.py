#include <map>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <bitset>

#define enableFastIO ios_base::sync_with_stdio(false); cin.tie(NULL);
#define inc(i,j,k) for (auto i=j;i<=k;i++)
#define li long int
#define lli long long int

using namespace std;

int main(){
enableFastIO;
int t;
cin >> t ;
string s,tmp="";
inc(i,1,t){
    cin >> s;
    tmp = "";
    for (char c:s)
        tmp = max(tmp+c,c+tmp);
    cout << "Case #" << i << ": " << tmp << endl;
}
}
