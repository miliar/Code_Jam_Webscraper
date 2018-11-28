#include<stdio.h>
#include<iostream>
#include<conio.h>
#include<set>
#include<vector>
#include<string.h>
#include<fstream>
#include<stdlib.h>
#include<math.h>

#define len 101

using namespace std;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int TestCases;
    cin>>TestCases;
    char c[2];
    gets(c);
    for(int testcase=0; testcase<TestCases; testcase++){
            cout<<"Case #"<<(testcase+1)<<": ";
            char str[len];
            gets(str);
            int i = strlen(str)-1;
            while(str[i]=='+'&&i>=0)
                i--;
            char s='-';
            int count;
            if(i>=0)
                count=1;
            else
                count=0;
            while(i>=0){
                    if(str[i]!=s){
                        s=str[i];
                        count++;
                    }
                    --i;

            }
            cout<<count<<endl;
    }
    return 0;
}
