#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

int Test(){
    vector<char> stack;
    char arr[101]={0};
    int i,j,len,ret=0;
    scanf("%s",arr);
    len = strlen(arr);
    for(i=0;i<len;i++){
        stack.push_back(arr[i]);
    }
    while(!stack.empty()){
        for(i=stack.size()-1;0<=i;i--) {
            if(stack[i] == '+'){
                stack.erase(stack.begin()+i);
            }
            else{
                break;
            }
        }
        if(stack.empty()) return ret;
        else{
            for(i=0;i<stack.size();i++){
                stack[i] == '+' ? stack[i] = '-' : stack[i] = '+';
            }
        }
        ret++;
    }
}

int main(){
    int i,T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++) printf("Case #%d: %d\n",i,Test());
}