/* 
 * File:   main.cpp
 * Author: Zhu Hanfeng <me@mlnotes.com>
 *
 * Created on 2014年4月12日, 上午7:50
 */

#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;

void calc(int num, set<int> &X, set<int> &Y, vector<int> &result){
    vector<int>::iterator iter;
    iter = set_intersection(X.begin(), X.end(), Y.begin(), Y.end(), result.begin());
    int size = iter-result.begin();
    
    if(size == 1){
        cout << "Case #" << num << ": " << result[0] << '\n';
    }else if(size > 1){
        cout << "Case #" << num << ": Bad magician!\n";
    }else{
        cout << "Case #" << num << ": Volunteer cheated!\n";
    }
    
}

int main() {
    int T;
    int line;
    int tmp;
    set<int> X;
    set<int> Y;
    vector<int> result(4);
    cin >> T;
    for(int i = 0; i < T; ++i){
        X.clear();
        Y.clear();
        
        cin >> line;
        for(int j = 0; j < (line-1)*4; ++j){
            cin >> tmp;
        }
        for(int j = 0; j < 4; ++j){
            cin >> tmp;
            X.insert(tmp);
        }
		for(int j = line*4; j < 16; ++j){
			cin >> tmp;
		}
        
        cin >> line;
        for(int j = 0; j < (line-1)*4; ++j){
            cin >> tmp;
        }
        for(int j = 0; j < 4; ++j){
            cin >> tmp;
            Y.insert(tmp);
        }
		for(int j = line*4; j < 16; ++j){
			cin >> tmp;
		}

        calc(i+1, X, Y, result);
    }
    
    return 0;
}

