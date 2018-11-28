#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <list>
using namespace std;
int mx,cnt;
list<char> l;
char s[10005];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("Aoutput.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        scanf("%s",s);
        int ss=strlen(s);
        l.clear();
        mx=0;
        for(int i=0;i<ss;i++){
//            printf("%d",s[i]-'A');
            if(s[i]-'A'>=mx){
                mx=s[i]-'A';
                l.push_front(s[i]);
//                printf("*%d\n",i);
            }
            else{
                l.push_back(s[i]);
//                printf("-%d\n",i);
            }
        }
        printf("Case #%d: ",t);
        for(list<char>::iterator it=l.begin();it!=l.end();it++){
            printf("%c",*it);
        }
        printf("\n");
    }
}
