#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char flip(char c){
    if(c == '+')    return '-';
    return '+';
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    string s;
    int t,stt,endd,ans;
    scanf("%d",&t);
    for(int k = 1; k <= t; k++){
        cin>>s;
        stt = 0;
        endd = s.size()-1;
        ans = 0;
        while(endd>=0){
            while(endd >= 0 && s[endd] == '+')
                endd--;
            if(endd < 0)   break;
            if(s[stt] == '+'){ // flip top positive segment
                int l = stt;
                while(l <= endd && s[l] == '+')
                    s[l++] = '-';
            }
            else{ // flip all until end
                int l = stt, r = endd;
                while(l<=r){
                    char L = flip(s[l]), R = flip(s[r]);
                    s[l] = R; s[r] = L;
                    l++; r--;
                }
            }
            ans++;
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
