#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<string>

using namespace std;

int main()
{
    freopen("/Users/shitian/Desktop/programmingcCntest/GCJ/gcj/gcj/B-large.in", "r", stdin);
    freopen("/Users/shitian/Desktop/programmingcCntest/GCJ/gcj/gcj/out.txt", "w", stdout);

    int tcase;
    cin>>tcase;
    for(int tca=1;tca<=tcase;tca++){
        cout<<"Case #"<<tca<<": ";
        
        string str;
        cin>>str;
        int ans=0;
        for(int i=str.length()-1;i>=0;i--){
            if(str[i]=='-'){
                ans++;
                for(int j=0;j<i;j++){
                    if(str[j]=='+'){
                        str[j]='-';
                    } else {
                        str[j] = '+';
                    }
                }
            }
        }
        cout<<ans<<endl;
    }
  
    return 0;
}