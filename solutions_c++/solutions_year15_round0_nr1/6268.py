#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <limits>

using namespace std;

int tonumber(char c){
    return c - '0';
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T, i;
    cin >> T;
    for (i=1; i<=T; i++)
    {
        int m, p=0, f=0;
        cin >> m;
        string S;
        cin >> S;
        for (int i=0; i<S.length(); i++){
                int s = tonumber(S[i]);
                if (p>=i)
                    p+= s;
                else{
                    f+= (i-p);
                    p+= (i-p) + s;
                }
        }
        cout <<"Case #" << i << ": " << f <<endl;
    }
    return 0;
}
