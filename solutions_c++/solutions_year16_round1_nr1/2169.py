#include<cstdio>
#include<vector>
#include<stack>
#include<cstring>
using namespace std;
char a[1100];
stack<char> s1;
vector<char> v2;
int Case = 1;
int main(){
    int T;
    #ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    scanf("%d\n",&T);
    while(T--){
        gets(a);
        while(!s1.empty())
            s1.pop();
        v2.clear();
        s1.push(a[0]);
        v2.push_back(a[0]);
        for(int i=1;a[i]!='\0';i++){
            if(a[i]>=s1.top())
                s1.push(a[i]);
            else
                v2.push_back(a[i]);
        }
        printf("Case #%d: ",Case++);
        while(!s1.empty()){
            printf("%c",s1.top());
            s1.pop();
        }
        for(int i=1;i<v2.size();i++)
            printf("%c",v2[i]);
        puts("");
    }
    return 0;
}
