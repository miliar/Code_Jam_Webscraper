#include <bits/stdc++.h>
#include <iostream>
#include <cstring>

using namespace std;
int numbers[10];

bool checkArray(){
    if(numbers[0]==0 && numbers[1]==1 && numbers[2]==2 && numbers[3]==3 && numbers[4]==4 && numbers[5]==5 && numbers[6]==6 && numbers[7]==7 && numbers[8]==8 && numbers[9]==9)
    {return true;}
    else{return false;}
}

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int c;
    scanf("%d", &c);
    for (int i = 1; i <= c; i++){
        numbers[0]=1;
        for(int k=1;k<=9;k++){numbers[k]=0;}
        printf("Case #%d: ", i);
        int n;
        scanf("%d", &n);
        for(int j=1;j<=123456;j++){
            int finalnum=n;
            if(finalnum==0){cout << "INSOMNIA" << endl; break;}
            finalnum *= j;
            int temp;
            int num=finalnum;
            while(num!=0){
                temp = num%10;
                if(numbers[temp]!=temp){
                    numbers[temp]=temp;
                }
                num /=10;
            }
            if(checkArray()){
                n=finalnum;
                break;
            }
        }
        if(n!=0){cout << n << endl;}
    }
    return 0;
}
