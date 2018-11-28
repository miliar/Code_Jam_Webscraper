#include<iostream>

using namespace std;

#include <math.h>

void printArr(int arr[],int length){
    for(int i=0;i<length;i++){
        cout<<arr[i] <<" ";
    }
    cout<<endl;
}
int main(){

    int t;
    cin>>t;
    int x=1;

    while(x<=t){

        int arr[] = {0,1,2,3,4,5,6,7,8,9};
        int n;
        cin>>n;
        if(n == 0){
            cout<<"Case #"<<x<<": "<<"INSOMNIA"<<endl;
            x++;
            continue;
        }

        long m=1;
        long num = 0;
        while(1){
            num = n * m;
            long number = num;
            int len = (int)floor(log10((float)num)) + 1;
            int tmpArr[len];
            int i = 0;

            do {
                tmpArr[i] = number % 10;
                number /= 10;
                i++;
            } while (number != 0);


            for(int i=0;i < 10;i++){
                for(int j=0;j<len;j++){
                    if(tmpArr[j] == arr[i]){
                        arr[i] = -1;
                    }
                }
            }

            int flag=0;
            for(int i=0;i<10;i++){
                if(arr[i] != -1 ){
                    flag = 1;
                }
            }
            if(flag == 0){
                break;
            }
            m++;
        }
        cout<<"Case #"<<x<<": "<<num<<endl;
        x++;
    }
}
