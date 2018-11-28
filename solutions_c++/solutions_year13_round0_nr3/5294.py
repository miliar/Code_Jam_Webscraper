#include <iostream>
#include <string>
#include <cmath>
#include <sstream>

using namespace std;

int comprobar(string num){
    if(num.length()==1)return true;
    int j = num.length()-1;
    for(int i=0; i<num.length(); i++){
        if(num[i]!=num[j]){
            return 0;   
        }
        j--;
    }
    return 1;
}

int main(){
    int cases;
    cin>> cases;
    for(int i =1; i<=cases; i++){
      int in, to;
      int max =0;
      cin >> in >> to;
        for(int j=in; j<=to; j++){
             stringstream ss;
             stringstream ss1;
             ss << j;
            string m1 = ss.str();
            float x = sqrt(j);
             ss1 << x;
            string m2 = ss1.str();
           // cout << " la m1 es " << m1 << " la m2 es " << sqrt(j) << endl;
            if((comprobar(m1)==1)&&(comprobar(m2)==1))max++;
            //cout<< comprobar(m1) << " resul 2 " << comprobar(m2)<< endl;
        }
        cout << "Case #" << i << ": " << max << endl;    
    }
    
    
    return 0;   
}
