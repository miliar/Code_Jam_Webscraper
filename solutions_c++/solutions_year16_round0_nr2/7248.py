#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    string input;
    cin>>T;
    for(int t=1; t<=T; t++)
    {
        string pStr;
        cin>>input;
        int i = input.size()-1;
        while(input[i]=='+') i--;
        input = input.substr(0, i+1);
        for(int i=0; i<input.size(); i++){
           if(pStr==""||pStr[pStr.size()-1]!=input[i])
            pStr.push_back(input[i]);
        }
        cout<<"Case #"<<t<<": "<<pStr.size()<<endl;

    }
}
