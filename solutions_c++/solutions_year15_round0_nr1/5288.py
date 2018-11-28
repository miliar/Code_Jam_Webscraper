//
//  StandingOvaition.cpp
//  
//
//  Created by Jefvin Viriya on 11/4/15.
//
//

#include <cstdio>
#include <iostream>

using namespace std;

int main(){
    int t;
    int k;
    char s;
    int ss[1005];
    int i,j;
    int neededPerson;
    int answer;
    scanf("%d",&t);
    for(int c=1;c<=t;c++){
        scanf("%d ",&k);
        neededPerson = 0;
        answer = 0;
        for(i=0;i<=k;i++){
            scanf("%c",&s);
            ss[i] = ((int)s)-48;
//            printf("shy %d n= %d",i,ss[i]);
            if(i>neededPerson){
                answer+=(i-neededPerson);
                neededPerson+=(i-neededPerson);
            }
            neededPerson+=ss[i];
        }
        printf("Case #%d: %d\n",c,answer);
    }
    
    return 0;
}