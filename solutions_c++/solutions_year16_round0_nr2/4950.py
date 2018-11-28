#include <iostream>
using namespace std;

char stack[100];
int S;

void reverse(int n){
    char temp[n+1];
    for(int i=0;i<=n;i++){
        temp[i]=stack[i];
    }
    for(int i=0;i<=n;i++){
        stack[i]=temp[n-i];
    }
}

void inv(int n){
    for(int i=0;i<=n;i++){
        if(stack[i]=='+'){
            stack[i]='-';
        }else{
            stack[i]='+';
        }
    }
}

void flip(int n){//index:nまでをひっくり返す
    //printf("\n n:%d %s ",n,stack);
    inv(n);
    reverse(n);
    //printf("%s",stack);
}

int solve(){
    scanf("%s",stack);
    int length;
    for(length=0;stack[length]!='\0';length++);
    int count=0;
    while(true){
        while(true){
            if(stack[length-1]=='+'){
                length--;
                if(length==0){
                    return count;
                }else {
                    continue;
                }
            }else{
                break;
            }
        }

        if(stack[0]=='-'){
            flip(length-1);
            count++;
        }else{
            for(int i=0;i<length;){
                if(stack[i+1]=='+'){
                    i++;
                }else{
                    flip(i);
                    count++;
                    break;
                }
            }
            flip(length-1);
            count++;
        }
    }
    return 0;
}

int main(void){
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        cout << "Case #" << i <<": " << solve() << endl;
    }
    return 0;
}