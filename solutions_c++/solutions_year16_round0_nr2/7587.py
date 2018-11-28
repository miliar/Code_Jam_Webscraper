#include <bits/stdc++.h>
#define S 103
using namespace std;
typedef long long LL;
int in(){int x; scanf("%d", &x); return x;}
int dirX[]={1, 0, -1, 0, 1, -1, 1, -1};
int dirY[]={0, 1, 0, -1, 1, -1, -1, 1};
int rX[] = {1, 1, 2, 2, -1, -1, -2, -2};
int rY[] = {2, -2, 1, -1, 2, -2, +1, -1};
///...............Code Starts From Here...............///

string cake;

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t = in(), cs = 0;
    while(t--){
        cin >> cake;
        stack <char> SS;
        int ans = 0, tz;
        string temp;
        temp = cake;
        while(true){
            tz = temp.size();
            for(int i = 0; i < tz; i++)SS.push(temp[i]);
            while(!SS.empty() && SS.top() == '+')SS.pop();
            if(SS.empty())break;
            temp.clear();
            while(!SS.empty()){
                temp.push_back(SS.top());
                SS.pop();
            }
            tz = temp.size();
            if(temp[tz-1] == '-'){
                for(int i = 0; i < tz; i++){
                    if(temp[i] == '-')temp[i] = '+';
                    else temp[i] = '-';
                }
            }
            else{
                reverse(temp.begin(), temp.end());
                int f = 0;
                for(int i = tz-1; i >= 0; i--){
                    if(temp[i] == '+')break;
                    else f++;
                }
                reverse(temp.begin(), temp.end()-f);
                for(int i = 0; i < tz-f; i++){
                    if(temp[i] == '-')temp[i] = '+';
                    else temp[i] = '-';
                }
            }
            ans++;
        }
        printf("Case #%d: %d\n", ++cs, ans);
    }
    return 0;
}
