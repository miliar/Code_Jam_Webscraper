//
//  main.cpp
//  Problem_D._Deceitful_War
//
//  Created by KoRNz on 4/13/2557 BE.
//  Copyright (c) 2557 KoRNz. All rights reserved.
//

#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>


using namespace std;

bool Less (double i,double j) { return (i<j); };
bool Greater (double i,double j) { return (i>j); };


int findLess(double a, vector<double> b) {
    double diff = b[b.size()-1];
    double num = 0.0;
    int index = -1;
    
    for (int i=0; i<b.size(); i++) {
        if (b[i]>a && b[i]-a>=0 && b[i]-a<=diff) {
            diff = b[i]-a;
            num = b[i];
            index = i;
        }
    }
    return index;
};

int findMax(double a, vector<double> b) {
    double diff = b[b.size()];
    double num = 0.0;
    int index = -1;
    
    for (int i=b.size()-1; i>=0; i--) {
        if (b[i]>a) {
            diff = b[i]-a;
            num = b[i];
            index = i;
//            cout << "found ! " << num << " : " << a << endl;
        }
    }
    return index;
};

int countDWar(vector<double> a, vector<double> b) {
    int countNWin = 0;
    
    for (int i=0; i<b.size(); i++) {
        int index = findMax(b[i], a);
        if(index >= 0) { //found it !
            a[index] = -1;
            countNWin++;
        }
    }
    
    return countNWin;

};


int countWar(vector<double> a, vector<double> b) {
    int countKWin = 0;
    
    for (int i=0; i<a.size(); i++) {
        int index = findLess(a[i], b);
        if(index >= 0) { //found it !
            b[index] = -1;
            countKWin++;
        }
    }
    
    return a.size()-countKWin;
};

pair<int, int> Solve() {
    //number of blocks of each person
    int n = 0;
    cin >> n;
    
    //queue of each person's block
    vector<double> N;
    vector<double> K;
    
    //store data in priority_queue !
    for (int i=0; i<n; i++) {
        double tmp = 0.0;
        cin >> tmp;
        N.push_back(tmp);
    }
    for (int i=0; i<n; i++) {
        double tmp = 0.0;
        cin >> tmp;
        K.push_back(tmp);
    }
    
    sort(K.begin(), K.end()); //min to max
    sort(N.begin(), N.end());
    
    
    
    return make_pair(countDWar(N, K), countWar(N, K));
};

int main()
{
    //To insert number of testcases
    int n=0;
    cin >> n;
    
    vector<string> print;
    
    //To call Solve method
    pair<int, int> answer;
    for (int i=0; i<n; i++) {
        answer = Solve();
        
        int num = i+1;
        ostringstream convert;
        convert << num;
        string sNum = convert.str();
        
        //store answer
        string sAnswer1 = std::to_string(answer.first);
        string sAnswer2 = std::to_string(answer.second);
        
        print.push_back("Case #" + sNum + ": " + sAnswer1 + " " + sAnswer2);
        
    }
    
    //to print
    for (int i=0; i<print.size(); i++) {
        cout << print[i] << endl;
    }
    return 0;
}

