#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large_1A.out","w",stdout);
    int t,i,l,j;
    char s[1001];
    char c;
    scanf("%d",&t);
    for(j=1;j<=t;j++){
        scanf("%s",s);
        string str = "";
        str = str + s[0];
        c = s[0];
        l = strlen(s);
        for(i=1;i<l;i++){
            if(s[i] >= c)
                {
                    str = s[i] + str;
                    c = s[i];
                }
            else
                str = str + s[i];
        }
        printf("Case #%d: ",j);
        cout << str << endl;
    }
    return 0;
}
