#include<stdio.h>
#include<iostream>
#include<conio.h>
#include<set>
#include<vector>
#include<string.h>
#include<fstream>
#include<stdlib.h>
#include<math.h>

using namespace std;

void solve(){
    char S[1001], temp[1001]="",temp2[1001]="";
    int n=0;
    gets(S);
    for(int i=0;S[i];i++){
        if(temp[0]<=S[i]){
            temp2[0]=S[i];
            temp2[1]='\0';
            strcat(temp2,temp);
        }
        else{
            strcpy(temp2,temp);
            char s1[2];
            s1[0]=S[i];
            s1[1]='\0';
            strcat(temp2,s1);
        }
        strcpy(temp,temp2);
    }
    cout<<temp;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int TestCases;
    cin>>TestCases;
    char c[2];
    gets(c);
    for(int testcase=0; testcase<TestCases; testcase++){
            cout<<"Case #"<<(testcase+1)<<": ";
            solve();
            cout<<endl;
    }
    return 0;
}
