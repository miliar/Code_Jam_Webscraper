#include <vector>
#include <iostream>
#include <cstdio>

#define enableFastIO ios_base::sync_with_stdio(false); cin.tie(NULL);
#define inc(i,j,k) for (auto i=j;i<=k;i++)
#define li long int

using namespace std;

int main(){
enableFastIO;
li flips=0,t;
cin >> t;
string s;
inc(i,1,t)  {
    cin >> s;
    flips=0;
    char lastC = '+';
    for (int i=s.length()-1;i>=0;--i){
        if (s.at(i)!=lastC){
            lastC = s.at(i);
            flips++;
        }
    }
    cout << "Case #" << i << ": "<< flips << endl;
    }
}
