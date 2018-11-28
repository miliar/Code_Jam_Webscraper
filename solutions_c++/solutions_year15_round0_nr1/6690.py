/* 
 * File:   main.cpp
 * Author: vidit
 *
 * Created on 10 April, 2015, 4:21 AM
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
  //  FILE *fi = freopen("input", "r", stdin);
  //  FILE *fo = freopen("output", "w", stdout);
    
    
    int test;
    cin>>test;
    for(int t=1;t<=test;t++){
        cout<<"Case #"<<t<<": ";
        int n;
        cin>>n;
        string s;
        cin>>s;
        int count=0;
        int ans=0;
        for (int i=0;i<=n;i++){
            if(count < i){
                ans+=i-count;
                count=i;
            }
            count +=s[i]-'0';
            
        }
        cout<<ans<<endl;
    }
    
    
    
   // fclose(fi);
   // fclose(fo);
    return 0;
}

