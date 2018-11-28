//https://code.google.com/codejam/contest/6224486/dashboard

#include<iostream>
#include<stdio.h>
#include <string>
using namespace std;
int main()
{
    int t,smax,res,i,cnt,c=1;
    scanf("%d", &t);
    string str;
    while (t--) {
        cnt=0;res=0;
        scanf("%d", &smax);
        cin>>str;
        for (i=0;i<=smax;i++) {
            if (cnt < i) {
                res += i-cnt;
                cnt += i-cnt;
            }
            cnt+=str[i]-'0';
        }
        cout<<"Case #"<<c<<": "<<res<<endl;
        c++;
    }
}
