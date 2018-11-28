#include <iostream>
#include <cstdio>
using namespace std;


int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int first;
    int second;
    int arr1[4][4]={};
    int arr2[4][4]={};
    cin>>T;
    for(int i=0; i<T; i++){
        cin>>first;
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
                cin>>arr1[j][k];
        cin>>second;
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
                cin>>arr2[j][k];
        int count=0;
        int number=0;
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                if(arr1[first-1][j]==arr2[second-1][k]){
                    count++;
                    number=arr2[second-1][k];
                }
            }
        }

        if(count==1){
            cout<<"Case #"<<i+1<<": "<<number<<endl;
        }else if(count==0){
            cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
        }else{
            cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
        }
    }

    return 0;
}
