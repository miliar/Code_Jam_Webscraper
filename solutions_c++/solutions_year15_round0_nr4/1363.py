#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i,t,a,b,c;
    cin>>t;
    for(i = 1; i <= t; i++){
        cin>>a>>b>>c;
        printf("Case #%d: ",i);
        if((b*c)%a) {
            puts("RICHARD");
        }
        else {
            if(a<=2) {
                puts("GABRIEL");
            }
            else if(a == 3) {
                if(b*c == 3) puts("RICHARD");
                else puts("GABRIEL");
            }
            else {
                if(b*c == 4 || b*c == 8) puts("RICHARD");
                if(b*c == 12 || b*c == 16) puts("GABRIEL");
            }
        }
    }
}