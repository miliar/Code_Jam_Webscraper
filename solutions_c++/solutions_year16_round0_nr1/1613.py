#include <bits/stdc++.h>

using namespace std;

long long num;
int cnt = 0;
bool h[12];

void clearmem(){
    cnt = 0;
    memset (h,0,sizeof h);
}

bool tickAllDigit(long long cn){
    for (;cn>0;){
        if (h[cn%10]==false){
            cnt++;
            h[cn%10] = true;
        }
        cn /= 10;
        if (cnt == 10){
            return true;
        }
    }
    return false;
}

void solve(){
    clearmem();
    scanf ("%I64d",&num);
    int ans = 1;
    if (num==0){
        printf ("INSOMNIA\n");
        return;
    }
    long long cur = num;
    while (!tickAllDigit(cur)){
        cur += num;
    }
    printf ("%d\n",cur);
}

int main(){
    freopen ("A-large.in","r",stdin);
    freopen ("Alarge.out","w",stdout);
    int TC;
    scanf ("%d",&TC);
    for (int tc=1;tc<=TC;tc++){
        printf ("Case #%d: ",tc);
        solve();
    }
return 0;
}
