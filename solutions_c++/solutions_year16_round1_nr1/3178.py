#include <cstdio>
#include <string.h>
#include <list>

using namespace std;

int main()
{
    int t,l;
    char s[1010];
    scanf("%d",&t);
    list<char> cola;
    for(int i=1;i<=t;i++){
        scanf("%s",s);
        l = strlen(s);
        cola.push_back(s[0]);
        for(int j=1;j<l;j++){
            if(cola.front()>s[j]){
                cola.push_back(s[j]);
            }else{
                cola.push_front(s[j]);
            }
        }
        printf("Case #%d: ",i);
        while(!cola.empty()){
            printf("%c",cola.front());
            cola.pop_front();
        }
        printf("\n");
    }
    scanf("%s",s);

    return 0;
}
