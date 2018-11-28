#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
#include<stack>

using namespace std;

int main(){
    int t;
    cin>>t;

    for(int k=1;k<=t;++k){
        vector<char> s;
        
        int m,sum =0;
        cin>>m;
        
        for(int i=0;i<=m;++i){
            char ch;
            
            cin>>ch;
            s.push_back(ch);
            int j = ch - '0';
            sum+=j;
         }
        int numPpSt = 0;
        int numFrNdd = 0;
        while(numPpSt!=sum){
                numPpSt = 0;
                
            for(int i=0;i<=m;++i){
                int j= s[i] - '0';
                if(i<=numPpSt) numPpSt+=j;
            }
            if(numPpSt!=sum){
                for(int i=0;i<=m;++i){
                    if(s[i]=='0'){
                        s[i]='1';
                        numFrNdd++;
                        sum++;
                        break;
                    }
                }
            }


        }
        cout<<"Case #"<<k<<": "<<numFrNdd<<endl;

    }

    return 0;
}

