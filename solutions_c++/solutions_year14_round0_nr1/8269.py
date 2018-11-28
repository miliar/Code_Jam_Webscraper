#include<iostream>
#include<stdio.h>
#include<map>

using namespace std;

int main() {

    int t,testcase = 0;
    cin>>t;
    while(t--) {
        testcase++;
        int n,m;
        int arr[20];
        for(int i=0;i<20;i++)
            arr[i] = 0;

        cin>>n;
        for(int i=1; i<= 4; i++) {
            for(int j=1;j<=4;j++) {
                int x;
                cin >>x;
                if(i==n) {
                    //cout<<x<<" ";
                    arr[x] = 1;
                }

            }
        }
        //cout<<endl;
        cin>>m;
        bool bad = false;
        bool cheat = false;
        bool single = false;
        int num = -1;

        for(int i=1; i<= 4; i++) {
            for(int j=1;j<=4;j++) {
                int x;
                cin >>x;
                if(i==m) {
                    //cout<<x<<" ";
                    if (arr[x] == 1 && !single){
                        num = x;
                        single = true;
                    } else if(arr[x] == 1 && single){
                        bad = true;
                    }
                }
            }
        }
        //cout<<endl;
        if (num == -1)
            cheat = true;

        if (cheat) {
            cout<<"Case #"<<testcase<<": Volunteer cheated!"<<endl;
        } else if (bad) {
            cout<<"Case #"<<testcase<<": Bad magician!"<<endl;
        } else {
            cout<<"Case #"<<testcase<<": "<<num<<endl;
        }
    }
    return 0;
}
