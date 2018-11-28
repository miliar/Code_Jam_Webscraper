#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Loo,Loop;
    cin>>Loop;
    bool A[10];
    for(Loo=1; Loo<=Loop;Loo++)
    {
        string s;
        cin>>s;
        s = s + '+';
        int res = 0;
        for(int i=1;i<s.length();i++)
            if(s[i] != s[i-1])
                res++;

        printf("Case #%d: %d\n",Loo, res);
    }
    return 0;



}