

#include<iostream>
#include <cmath>

using namespace std;

int main(){
  
int t,p,zmiana; 
char a,c;
string b;
cin >> t;

    for(int i=0; i<t; i++){
        p=0; zmiana=0;
        cin >> b;
        p=b.length();
        c=b[0];
        for(int j=1; j<p; j++){
            a=b[j]; 
            if(a!=c){zmiana++;}
            c=a;
        }
        cout << "Case #" << i+1 << ": " ;
        if(a=='+'){cout << zmiana<<'\n';}
        else{cout << zmiana+1 <<'\n';}

    }
    
return 0;}


