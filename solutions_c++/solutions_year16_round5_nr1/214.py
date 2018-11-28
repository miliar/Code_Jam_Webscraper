#include<cstdio>
#include<stack>
#include<cstring>
using namespace std;
const int MAX  = 20000 + 10;
char arr[MAX];
int main(){
    int TN;
    scanf("%d ", &TN);
    for(int casen = 1 ; casen <= TN ; casen++){
        printf("Case #%d: ", casen);
        stack<char> s;
        gets(arr);
        int len = strlen(arr), ans = 0;
        for(int i = 0 ; i < len ; i++){
            if(!s.empty() && s.top () == arr[i]){
                s.pop();
                ans += 10;
            }else{
                s.push(arr[i]);
            }
        }
        ans += (int)s.size() / 2 * 5;
        printf("%d\n", ans);
    }
    return 0;
}
