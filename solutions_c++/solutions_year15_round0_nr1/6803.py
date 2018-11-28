#include <cstdlib>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("A-small-attempt0.out");
    int T,Smax,persP,tem,contReal,persR;
    string s;
    cin>>T;
    //cout<<T<<endl;
    for(int k=1;k<=T;k++){
        cin>>Smax;
        cin>>s;
        persP=persR=0;
         persP=s[0]-'0';

        for (int i=1;i<s.size();i++){

            if (i<=persP){
                persP+=s[i]-'0';
            }else{
                    persR+=i-persP;
                    persP+=(i-persP)+s[i]-'0';
                }
         //   cout<<"->>>>>>>>"<<i<<" : "<<persP<<" : "<<persR<<endl;
        }
        cout<<"Case #"<<k<<": "<<persR<<endl;

    }


    return 0;
}
