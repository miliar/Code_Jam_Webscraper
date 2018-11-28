//The Last Word R1 Q1
#include<iostream>

#include<string>

#include<stdio.h>

#define T int test;scanf("%d", &test);int t = test;while(t--)

using namespace std;
int main(){
    string a1,c1;
    char p1;
    int i1;
    T{
        cin>>c1;
        printf("Case #%d: ", test-t);
        p1 = c1[1];
        i1 = 1;
        a1 = c1[0];
        while(p1 != '\0'){
            if(p1>=a1[0]){
                a1 = p1 + a1;
            }
            else{
                a1 = a1 + p1;
            }
            p1 = c1[++i1];
        }
        printf("%s\n",a1.c_str());
    }
}
