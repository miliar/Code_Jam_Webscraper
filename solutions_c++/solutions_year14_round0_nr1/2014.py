//
//  main.cpp
//  magicTrick
//
//  Created by Yitao Liang on 14-4-11.
//  Copyright (c) 2014年 Yitao Liang. All rights reserved.
//

#include <iostream>
using namespace std;
#include <set>

int main(){
    freopen("A-small-attempt1.in.txt","r",stdin);
    freopen("A-small-attempt1.out.txt","w",stdout);
    int t,m1,m2;
    int number=0;
    int s=0;
    int key=0;
    set<int> s1;
    cin>>t;
    for (int i=1;i<=t;i++){
        cin>>m1;
        for (int j=0;j<4;j++){
            if (m1==j+1){
                for (int k=0;k<4;k++){
                    cin>>number;
                    s1.insert(number);
                }
            }else{
                for (int k=0;k<4;k++){
                    cin>>number;
                }
            }
        }
        cin>>m2;
        s=0;
        for (int j=0;j<4;j++){
            if (m2==j+1){
                for (int k=0;k<4;k++){
                    cin>>number;
                    if (s1.count(number)){
                        key=number;
                        s+=1;
                    }
                }
            }
            else{
                for (int k=0;k<4;k++){
                    cin>>number;
                }
            }
        }
        if (s==0){
            cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
        }else if (s==1){
            cout<<"Case #"<<i<<": "<<key<<endl;
        }else{
            cout<<"Case #"<<i<<": Bad magician!"<<endl;
        }
        s1.clear();
    }
    
    return 0;
}