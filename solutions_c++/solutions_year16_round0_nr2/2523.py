#include <stdio.h>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

bool isAllSmile(string str){
    for(int i=0;i<str.size();i++)
        if(str[i]=='-')
            return false;
    return true;
}
string flipGroup(string str){
    int i,j,nFlip=str.size()-1;
    char newChar;
    if(str[0]=='+')
        newChar = '-';
    else
        newChar = '+';

    for(i=0;i<str.size();i++)
    {
        if(str[i]!=str[0]){
            nFlip=i-1;
            break;
        }
    }
    for(i=0;i<=nFlip;i++)
        str[i] = newChar;
    return str;
}
int main()
{
    int TC;
    scanf("%d",&TC);
    for(int cs=1;cs<=TC;cs++){
        string str;
        cin >> str;
        int ans=0;
        for(;true;){
            if(isAllSmile(str))
                break;
            str = flipGroup(str);
            ans++;
        //    cout << str << endl;
        }

        printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}
