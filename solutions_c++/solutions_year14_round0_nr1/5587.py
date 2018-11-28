#include <stdio.h>
#include<iostream>
#include<cmath>
#include<vector>
#include<set>
#include<algorithm>
#include <fstream>
using namespace std;

int main()
{
    ofstream cout ("A-small.out");
    ifstream cin ("A-small.in");
    int T,line,a,throw1,throw2;
    set<int> theLine1;
    set<int> theLine2;
    vector<int> intersection;

    cin >> T;
    for( int i = 1; i <= T; i++){

        //Line 1
        cin >> line;
        throw1 = (line - 1) * 4;
        throw2 = (4 - line) * 4;

        for( int j = 0; j < throw1; j++)
            cin >> a;
        for( int j = 0; j < 4; j++){
            cin >> a;
            theLine1.insert(a);
        }
        for( int j = 0; j < throw2; j++)
            cin >> a;
        ////////////////////////

        //Line 2
        cin >> line;
        throw1 = (line - 1) * 4;
        throw2 = (4 - line) * 4;

        for( int j = 0; j < throw1; j++)
            cin >> a;
        for( int j = 0; j < 4; j++){
            cin >> a;
            theLine2.insert(a);
        }
        for( int j = 0; j < throw2; j++)
            cin >> a;
        ////////////////////////
        cout << "Case #"<< i <<": ";
        set_intersection(theLine1.begin(), theLine1.end(),
                          theLine2.begin(), theLine2.end(),
                          std::back_inserter(intersection));
        if(intersection.size()==1)
            cout << intersection[0] << "\n";
        else if(intersection.size()==0)
            cout << "Volunteer cheated!"<< "\n";
        else
            cout << "Bad magician!" << "\n";
        intersection.clear();
        theLine1.clear();
        theLine2.clear();
    }
    return 0;
}
