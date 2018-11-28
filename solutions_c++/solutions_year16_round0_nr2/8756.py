#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    string x;
    int flag = 0;
    for(int i = 1;i<=t;i++){
        cin>>x;
        x = x + '+';
        int c = 0;
        int cn = 0;
        flag = 0;
        if(x[0]=='-'){
            c+=1;
            while(x[cn]!='+'){
                cn+=1;
            }
        }
        for(int j = cn;j<x.length();j++){
                if(x[j]=='-'){
                    flag = 2;
                }if(x[j]=='+'&&flag == 2){
                    c+=2;
                    flag= 1;
                }
        }
        cout<<"Case #"<<i<<": "<<c<<endl;
    }
    return 0;
}
