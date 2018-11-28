#include <iostream>
#include <cstdio>
using namespace std;

int flip(string &s,int k)
{
    int i;
    for(i=k;i>=0;i--) {
        if(s[i]=='-') {
           s[i]='+';
        }
        else {
           s[i]='-';
        }
    }
    i=k;
    while(i>=0&&s[i]=='+') {
        i--;
    }
    return i;
}

int main()
{
    int i,t,n,count,k,T;
    string s;
    cin>>T;
    for(t=1;t<=T;t++) {
        cin>>s;
        n=s.size();
        count=0;
        k=n-1;
        while(k>=0&&s[k]=='+') {
            k--;
        }
        while(k>=0) {
            k=flip(s,k);
            count++;
        }
        printf("Case #%d: %d\n",t,count);
    }
    return 0;
}
