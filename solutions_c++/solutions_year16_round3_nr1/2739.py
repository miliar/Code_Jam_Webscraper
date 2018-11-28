//
//  main.cpp
//  political_evacuation
//
//  Created by Peter Matta on 5/8/16.
//  Copyright © 2016 Peter Matta. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

class Party {
public:
    char name;
    int count;
    
    Party(char name, int count) {
        this->name = name;
        this->count = count;
    }
    
};

struct comparator {
    bool operator()(const Party& lhs, const Party& rhs) {
        return lhs.count < rhs.count;
    }
};

int main(int argc, const char * argv[]) {
    int t, n, count;
    
    fstream in_file;
    in_file.open("A-large.in.txt", ios::in);
    
    in_file >> t;
    
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": ";
        priority_queue<Party, vector<Party>, comparator> pq;
        
        in_file >> n;
        
        for (int j = 0; j < n; j++) {
            in_file >> count;
            pq.push(Party(65 + j, count));
        }
        
        
        vector<string> evac;
        string str;
        
        int j = 0;
        while (!pq.empty()) {
            Party top = pq.top();
            pq.pop();
            top.count--;
            if (top.count) {
                pq.push(top);
            }
            if (j++ % 2) {
                str += string(&top.name);
                evac.push_back(str);
            } else {
                str = string(&top.name);
            }
        }
        
        if (str.length() == 1) {
            evac.push_back(str);
            swap(evac[evac.size() - 1], evac[evac.size() - 2]);
        }
        
        for (auto evc : evac) {
            cout << evc << " ";
        }
        
        cout << endl;
        
    }
    
    return 0;
}
