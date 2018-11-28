#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

int a,b;
void Input(){
    cin >> a >> b;
}
int Getans(){
    int ans = 0;
    if(a <= 1 && 1 <= b)
        ans++;
    if(a <= 4 && 4 <= b)
        ans++;
    if(a <= 9 && 9 <= b)
        ans++;
    if(a <= 121 && 121 <= b)
        ans++;
    if(a <= 484 && 484 <= b)
        ans++;
    return ans;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int Ncase;
    cin >> Ncase;
    int ans = 0;
    while(Ncase--){
        Input();
        cout <<"Case #" << ++ans << ": "<< Getans() << endl;
    }
    return 0;
}
