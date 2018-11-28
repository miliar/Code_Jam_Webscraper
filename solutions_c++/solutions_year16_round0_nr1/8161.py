#include <iostream>
using namespace std;

int CheckAll(int);
void TotalNum(int, int[], int);

int CheckAll(int k[]){
    int n=0;
    for(int i=0;i<10;i++){
        if(k[i]==1)
            n++;
    }
    return n;
}

void TotalNum(int n, int k[], int casenum){
    int num;
    if(n!=0){
        int i=1, timecount = 0, flag = 0;
        while(CheckAll(k)!=10 &&  timecount < 1000000000){
            num = n * i;
            while(num > 0){
                k[num%10] = 1;
                num /= 10;
            }
            i++;timecount++;
        }
        if(CheckAll(k)==10)
            cout << "Case #" << casenum << ": " << timecount * n << endl;
        else
            cout << "Case #" << casenum << ": "<< "INSOMNIA" << endl;

    }else{
        cout << "Case #" << casenum << ": "<< "INSOMNIA" << endl;
    }
}

int main(){

    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int total;
    cin >> total;
    for(int i=0;i<total;i++){
        int num, k[10]={0};
        cin >> num;
        TotalNum(num, k, i+1);
    }


    return 0;
}
