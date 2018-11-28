//
//  main.cpp
//  Google_a
//
//  Created by 윤성빈 on 2016. 4. 10..
//  Copyright © 2016년 MeteorBin. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;
bool check( string l,int a[],int j){
    int u = 0;
    u = atoi(l.c_str());
    u = u * j;
    l = to_string(u);
    int c = 0;
    for( int i = 0 ; i< l.length();i++){
        a[l.at(i) - '0'] = 1;
    }
    for(int i = 0; i < 10; i++){
        if(a[i] == 0) {
            c = 1;
            break;
        }
    }
    if( c == 1) return true;
    else return false;
}

string calc( string l, int i){
    int u = 0;
    u = atoi(l.c_str());
    u = u * i;
    l = to_string(u);
    return l;
}
int main(int argc, const char * argv[]) {
    
    int n;
    cin >> n;
    for(int i = 1; i<=n;i++){
        string line;
        cin >> line;
        if(line.compare("0") == 0) cout << "Case #"<<i<<": INSOMNIA\n";
        else {
            int arr[10]={0,};
            int j = 1;
            while(check(line,arr,j)){
                j++;
            }
            
            cout << "Case #"<<i<<": "<<calc(line,j)<<"\n";
        }
    }
    return 0;
}
