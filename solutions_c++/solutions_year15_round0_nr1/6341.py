#include<iostream>
#include<stdio.h>
using namespace std;
char people[1002]={};
int standing=0,friends=0;
int t,sm;
int main(){
    cin>>t;
    for(int k=0;k<t;k++){
        sm=0;
        standing=0;
        friends=0;
        cin>>sm;
        cin>>people;
        standing+=people[0]-'0';

        for(int i=1;i<=sm;i++){
            if(standing>=i)standing+=people[i]-'0';
            else if(people[i]!='0'){
                friends+=i-standing;
                standing+=i-standing;
                standing+=people[i]-'0';
            }
        }
        printf("Case #%d: %d\n",k+1,friends);
    }

}

