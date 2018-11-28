//
//  Counting sheep
//
//
//  Created by Udaya Bhaskar Rao on 08/04/16.
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
        cin >> N;
        set<int> s;
        int num = N;
        int x;
        bool added = true;
        long long curnum = num;
        int sz = 0;
        long val = 1;
        /*while(curnum){
            curnum = curnum/10;
            sz++;
            val = val * 10;
        }
        curnum = num;*/
        while(curnum != 0){
            while(curnum){
                x = curnum%10;
                curnum = curnum/10;
                s.insert(x);
            }
            if(s.size() == 10){
                break;
            }
            num = num + N;
            curnum = num;
        }
        if(s.size() == 10){
            cout << "Case #" << t+1 << ": " << num << endl;
        }else{
            cout << "Case #" << t+1 << ": INSOMNIA" << endl;
        }
        
        t++;
    }
    
    return 1;
}
