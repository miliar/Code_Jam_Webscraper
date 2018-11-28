/* 
 * File:   main.cpp
 * Author: Mohamed
 *
 * Created on 11 أبريل, 2015, 01:46 ص
 */

#include<bits/stdc++.h>
#include<string>
#include<cstdio>
using namespace std;

int main(int argc, char** argv) {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t ; cin>>t;
    int t0 = t;
    for(int k=1 ; k<=t ; k++ )
    {
        int s_up = 0 , f = 0, max;
        string s;
        cin>>max>>s;
        
        for(int i=0 ;i<=max ; i++)
        {
            if(s[i] - 48 > 0)
            {
                if(s_up >= i)
                {
                    s_up += s[i]-48;
                }else
                {
                    int n = i - s_up;
                    s_up += n;
                    s_up += s[i]-48;
                    f += n;
                }
            }
        }
        
        cout<<"Case #"<<k<<": "<<f;
        if(k != t)
            cout<<endl;
      
        
    }
    
    return 0;
}

