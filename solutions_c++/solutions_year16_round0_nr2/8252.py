#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B4large.out","w",stdout);

    int tt; scanf("%d",&tt);
    for(int tc=1; tc<=tt; tc++){
        char s[110]; scanf("%s",&s);
        int flag=0,cnt=0,j=1000;
        for(int i=0; i<strlen(s); i++) {
            if(s[i]=='+') {j=i; break;}
        }
        if(s[0]=='-') cnt++;
        if(j==1000) j=strlen(s);
        for(int i=j+1; i<strlen(s); i++){

            if(s[i]=='-' && flag==0){ cnt=cnt+2; flag=1;}
            else if(s[i]=='+') flag=0;
        }
        printf("Case #%d: %d\n",tc,cnt);
    }
    return 0;
}
