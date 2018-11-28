#include<bits/stdc++.h>
using namespace std;
#define read freopen("B-large.in","r",stdin)
#define write freopen("output2.txt","w",stdout)

string str;
int main(){
    read;
    write;
    int T, t=1;
    scanf("%d", &T);
    while(T--){
        cin>>str;
        int cnt=0;
        if(str[0]=='-'){
            for(int i=1; i<str.size(); i++){
                if(str[i-1]!=str[i]) cnt++;
            }
            if(cnt%2) printf("Case #%d: %d\n", t++, cnt);
            else printf("Case #%d: %d\n", t++, cnt+1);
        }
        else{
            for(int i=1; i<str.size(); i++){
                if(str[i-1]!=str[i]) cnt++;
            }
            if(cnt%2) printf("Case #%d: %d\n", t++, cnt+1);
            else printf("Case #%d: %d\n", t++, cnt);
        }
    }
    return  0;
}
