#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    int t,j=0,count;
    char ch;
    string str;
    cin >> t;
    for(int a0 = 1; a0 <=t; a0++){
         count=0;
         
         cin>>str;
        
       
        ch=str[0];
        for(int i=0;i<str.size();i++)
            {
            if(str[i]==ch)
                {
              continue;
            }
            else{
            count++;
            ch=str[i];
            }
         }
    count++;
    
    if(str[str.size()-1]=='-')
        {
        cout<<"Case #"<<a0<<": "<<count;
    }
    else{
        cout<<"Case #"<<a0<<": "<<count-1;
    }
    cout<<"\n";
    }
    return 0;
}
