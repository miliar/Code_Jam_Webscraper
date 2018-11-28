//
//  main.cpp
//  codejam sheep
//
//  Created by Anuja Lele on 09/04/16.
//  Copyright © 2016 Anuja Lele. All rights reserved.
//
//
//  bpot.cpp
//
//
//  Created by Anuja Lele on 09/04/16.
//
//
#include<iostream>
using namespace std;

int t,n,flag;
int visited[10];

int main(){
    int x,y,ntemp;
    cin>>t;
    for(int i=0;i<t;i++){
       // cout<<i<<endl;
        flag=0;
        for(int i=0;i<10;i++) visited[i]=0;
        cin>>n;
        if(n==0){
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
            continue;
        }

        ntemp=n;

        int j=0;
        int flag=1;


      while(flag){
          j++;
          n=ntemp*j;
             y=n;
            while(y>0){
                x=y%10;
                y=y/10;
                visited[x]=1;
                flag=0;
                for(int i=0;i<10;i++){
                    if(visited[i]==0) flag=1;
                    }
            }
      }cout<<"Case #"<<i+1<<": "<<n<<endl;
    }
    return 0;
}