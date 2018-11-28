#include<iostream>
#include<fstream>
#include<string>
#include<cstdlib>
#include<algorithm>
#include<stdio.h>
using namespace std;

int main()
{
    int T=0;
    int Max=0;
    char dic[1000];
    int Friend = 0;
    int temp1 = 0;
    int temp2 = 0;
    int counter = 0;
    string s;
    freopen("A-small-attempt4.in","r",stdin);
    freopen("A-small-attempt4.out","w",stdout);
    scanf("%d",&T);
    for (int case_counter=0;case_counter<T;case_counter++){
        scanf("%d",&Max);
        scanf("%s",dic);
        for (int i = 0; i<=Max; i++){
            s = dic[i];
            temp1 = atoi(s.c_str());
            if (counter<i && temp1!=0){
                Friend = Friend + i-counter;
                counter = counter + Friend + temp1;
            }
            else
            counter = counter + temp1;
        }
        printf("Case #%d: %d\n", case_counter+1, Friend);
        Friend = 0;
        counter = 0;
    }
}
