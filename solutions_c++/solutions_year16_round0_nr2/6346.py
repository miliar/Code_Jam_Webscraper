//
//  Pancakes.cpp
//  
//
//  Created by Udaya Bhaskar Rao on 09/04/16.
//
//

#include<vector>
#include<map>
#include<unordered_map>
#include<iostream>
#include<fstream>
#include <sstream>
#include<string>
#include<set>
using namespace std;

int main(){
    
    int T,t=0;
    cin >> T;
    int N;
    while(t < T){
        
        string str;
        cin >> str;
        
        int l = str.size();
        l--;
        while (l >= 0){
            if(str[l] == '+'){
                l--;
            }else{
                break;
            }
        }
        int flips = 0;
        int i = 0;
        char cursym = str[0];
        while(i <= l){
            if(cursym != str[i]){
                flips++;
                cursym = str[i];
            }
            i++;
        }
        if(l < 0){
            cout << "Case #" << t+1 <<": 0" << endl;
        }else{
            cout << "Case #" << t+1 <<": " << flips+1 << endl;
        }
        
        t++;
    }
    
    return 1;
}