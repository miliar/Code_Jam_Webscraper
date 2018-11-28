#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

string conv(int n) {
    string tmp="0", hsl="";
    if(n==0) return tmp;
    while(n)
    {
        tmp[0] = (n%10) + '0';
        n /= 10;
        hsl = tmp + hsl;
    }
    return hsl;
}

bool palindrome(string s) {
    bool hasil=true;
    for(int a=0;a<s.length();a++) {
        if(s[a]!=s[s.length()-1-a]) hasil=false;
    }
    return hasil;
}

int main() {
    bool cek[1605];
    memset(cek,false,sizeof(cek));
    int hasil,T,m,n;
    for(int a=1;a<=40;a++) {
        if(palindrome(conv(a)) && palindrome(conv(a*a))) cek[a*a]=true;
    }
    scanf("%d",&T);
    for(int z=1;z<=T;z++) {
        hasil=0;
        scanf("%d%d",&m,&n);
        for(int a=m;a<=n;a++) if(cek[a]) hasil++;
        printf("Case #%d: %d\n",z,hasil);
    }
    return 0;
}
