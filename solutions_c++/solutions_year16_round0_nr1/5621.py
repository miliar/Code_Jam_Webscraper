#include <iostream>
#include <vector>
#include <cstdio>
#include <string.h>
using namespace std;
long long calculate(int temp){
    bool a[10];
    for(int i = 0;i < 10;i++) a[i] = false;
    long long temp2 = temp;
    int i;
    char s[20];
    bool flag;
    for(int i = 1;;i++){
        temp2 = temp*i;
        sprintf(s,"%lld",temp2);
        for(int j = 0;j < strlen(s);j++){
            a[s[j]-'0'] = true;
        }
        flag = true;
        for(int i = 0;i < 10;i++){
            if(!a[i]){
                flag = false;
                break;
            }
        }
        if(flag) return temp2;
        
    }
    
}
int main(){
    
    int n,temp;
    cin >> n;
    for(int i = 0;i < n;i++){
        cin >> temp;
        cout << "Case " << "#" << i << ":" << " ";
        if(temp ==0){
            cout << "INSOMNIA" << endl;
        }
        else{
            cout << calculate(temp) << endl;
        }
    }
    return 0;
}