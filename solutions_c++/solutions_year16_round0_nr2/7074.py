#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;
string stack;
int pcakes[100];

long processdp() {    
    int len = stack.length();    
    for(int i=0;i<len;i++) pcakes[i] = 0;
    if(stack[0] == '-') pcakes[0] = 1;

    else pcakes[0] = 0;
    for(int i=1;i<len;i++) {
        if(stack[i] == '-') {
            if(stack[i-1] == '+') pcakes[i] = pcakes[i-1]+2;
            else pcakes[i] = pcakes[i-1];
        }
        else {
            pcakes[i] = pcakes[i-1];
        }
    }
    return pcakes[len-1];
}

int main(){
    int tcase;
    cin>>tcase;    
    for(int i=1;i<=tcase;i++) {
        cin>>stack;
        long notimes = processdp();
        cout<<"Case #"<<i<<": "<<notimes<<endl;        
    }
    return 0;
}
