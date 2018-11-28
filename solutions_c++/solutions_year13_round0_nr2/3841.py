#include<string.h>
#include<map>
#include<iostream>
#include<utility>
using namespace std;
    int rowMax[105];
    int colMax[105];
    int rowMin[105];
    int colMin[105];
void process(int arr[105][105], int N, int M) {
    int status =1;
    
    for(int i =0; i<N;i++) {
        for(int j=0;j<M;j++) {
             if(rowMax[i]>arr[i][j] && colMax[j]>arr[i][j]) {
                  status = 0;
                  break;
             }            
        }
    }
    switch(status) {
        case 1:
            cout<<"YES";
            break;
        case 0:
            cout<<"NO";
            break;
    }
}

int main() {
    int T;
    int N, M;
    int arr[105][105];
    cin>>T;
    int count=0;
    while(T>0) {
        cin>>N;cin>>M;
        count++;
        T--;
        for(int i =0; i<N;i++) {
            for(int j=0;j<M;j++) {
                cin>>arr[i][j];
                if(i==0) {//initialize colMin and colMax
                    colMax[j]=colMin[j]=arr[i][j];
                }
                if (j==0) {//initialize rowMax and rowMin
                    rowMax[i]=rowMin[i]=arr[i][j];
                }
                if (rowMax[i] < arr[i][j])
                    rowMax[i] = arr[i][j];
                if (rowMin[i] > arr[i][j])
                    rowMin[i] = arr[i][j];
                if (colMax[j] < arr[i][j])
                    colMax[j] = arr[i][j];
                if (colMin[j] > arr[i][j])
                    colMin[j] = arr[i][j];
            }
        }
        cout<<"Case #"<<count<<": ";
        process(arr, N, M);
        cout<<"\n";
    }
    return 0;
}
