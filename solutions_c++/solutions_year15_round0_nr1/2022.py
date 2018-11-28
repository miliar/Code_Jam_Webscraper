#include<iostream>
#include<cstdio>
using namespace std;

const int MAX_N = 1555;
int icase, n;
char ch[MAX_N];

int main(){
    ios_base::sync_with_stdio(false);
    cin>>icase;
    for(int c = 1; c <= icase; c++){
        cin>>n>>ch;
        int t = 1, d = 0;
        for(int i = 0; i <= n; i++){
            if(t - i - 1 >= 0){
                t += ch[i] - '0';
            }else {
                d = max(i + 1 - t, d);
                t += ch[i] - '0';
            }
        }
        printf("Case #%d: %d\n", c, d);
    }
    return 0;
}
