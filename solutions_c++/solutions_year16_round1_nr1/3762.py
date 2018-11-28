#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main(){
    long long int t,i;
    cin >> t;
    for(long long int a0 = 0; a0 < t; a0++){
        vector<char> ans;
        vector<char>::iterator it;
        long long int n;
        char first='A';
        string str;
       cin >> str;
        n=str.length();
       for(i=0;i<n;++i){
           if(str[i]>=first){
               ans.insert(ans.begin(),str[i]);
               first=str[i];
           }
           else{
               ans.push_back(str[i]);
           }
       }
           
    cout<<"Case #"<<a0+1<<": ";
    for (it=ans.begin(); it<ans.end(); it++)
        cout << *it;
    cout<<endl;    
        
    }
    return 0;
}
