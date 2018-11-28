#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>

using namespace std;

int isPalindrome(int n){
    char s[10];
    sprintf(s,"%d",n);
    string s1(s),s2(s);
    reverse(s2.begin(),s2.end());
    return !s1.compare(s2);
}

int main(){
    int T;
    scanf("%d",&T);
    for(int c=1; c<=T; c++){
        int fs[] = {1,4,9,121,484};
        int u,l;
        scanf("%d %d",&l,&u);
        int q=0;
        for(int i=0; i<5; i++)
            if(fs[i] >= l && fs[i] <= u)
                q++;
        printf("Case #%d: %d\n",c,q);
    }
    return 0;
}
