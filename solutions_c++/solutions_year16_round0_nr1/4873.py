#include <iostream>
using namespace std;

void count(int N){
    bool digit[10];
    for(int i=0;i<10;i++)digit[i]=false;
    if(N==0){
        cout << "INSOMNIA" << endl;
        return;
    }
    int count=1,p;
    while(true){
        p=count*N;
        while(p>0){
            if(digit[p%10]!=true){
                digit[p%10]=true;
                for(int i=0;i<10;i++){
                    if(digit[i]==false) break;
                    if(i==9){
                        cout << count*N << endl;
                        return;
                    }
                }
            }
            p/=10;
        }
        count++;
    }
}

int main(void){
    int N,T;
    cin >> T;
    for(int i=1;i<=T;i++){
        cin >> N;
        cout << "Case #" << i <<": ";
        count(N);
    }
}