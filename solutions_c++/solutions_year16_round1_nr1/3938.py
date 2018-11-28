#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int Test(){
    vector<char> Output;
    vector<char> assist;
    int i,j,len;
    char String[1001]={0};
    len = strlen(gets(String));
    Output.push_back(String[0]);
    for(i=1;i<len;i++){
        if(Output.front() <= String[i]){
            Output.insert(Output.begin(),String[i]);
        }
        else{
            Output.push_back(String[i]);
        }
    }
    for(i=0;i<len;i++){
        putchar(Output[i]);
    }
    printf("\n");
}

int main(){
    int i,T;
    scanf("%d",&T);
    getchar();
    for(i=1;i<=T;i++) {
        printf("Case #%d: ",i);
        Test();
    }
}