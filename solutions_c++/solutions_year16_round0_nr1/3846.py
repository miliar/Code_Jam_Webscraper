#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<string>

using namespace std;

int main()
{
    freopen("/Users/shitian/Downloads/A-large.in", "r", stdin);
    freopen("/Users/shitian/Downloads/out.txt", "w", stdout);
 
    int tcase;
    cin>>tcase;
    for(int tca=1;tca<=tcase;tca++){
        cout<<"Case #"<<tca<<": ";
        
        int n;
        cin>>n;
        int arr[11];
        memset(arr,0,sizeof(arr));
        int size=0;
        for(int i=1;i<10000;i++){
            int ano=n*i;
            while(ano){
                int curDigit = ano % 10;
                if(arr[curDigit] == 0){
                    size++;
                    arr[curDigit]++;
                }
                ano /= 10;
            }
            if(size == 10) {
                cout<<n*i<<endl;
                break;
            }
        }
        if(size!=10){
            cout<<"INSOMNIA"<<endl;
        }
    }
  
    return 0;
}