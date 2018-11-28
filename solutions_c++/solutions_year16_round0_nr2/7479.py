#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>
#include <map>

using namespace std;

map<string, int> myMap;

bool checkAllPlus(string s) {

    for (int i = 0; i < s.length(); i++)
        if (s[i] != '+')
            return false;

    return true;
}


int findMin(vector<int> v) {

    int min = INT_MAX;
    for (int i = 0; i < v.size(); i++) {
        if (min > v[i])
            min = v[i];
    }

    return min;
}

string flip(string s) {

    string new_s;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '+')
            new_s.push_back('-');
        else
            new_s.push_back('+');
    }
    return new_s;
}

int solve(string s) {

    if (s.length() == 1) {

        //cout << s << endl;
        if (s.compare("-") == 0) 
            return 1;
        else 
            return 0;
    }

    else {
        int toPush;
        int minresult;
        vector<int> v;

        //cout << s << endl;

        if (myMap.count(s))
            return myMap[s];
    
        if (checkAllPlus(s))
            return 0;

        myMap.insert(std::pair<string, int>(s, -1));

        for (int i = 1; i < s.length(); i++) {

            toPush = solve(flip(s.substr(0,i))) + solve(s.substr(i)) + 1;
            v.push_back(toPush);
        }
        if (myMap.count(flip(s)) == 0)
            v.push_back(solve(flip(s)) + 1);

        minresult = findMin(v);
        myMap[s] = minresult;
        return minresult;
        
    }
}

int main(int argc, const char* argv[]) {
	
	int numtests;
	int casenum = 0;
    string s;

	scanf("%d\n", &numtests);
    //cout << numtests << endl;

	while(++casenum <= numtests) {
         
        getline(cin, s);
        //cout << s << endl;
        myMap.clear();
        cout << "Case #" << casenum << ": " << solve(s) << endl;

	}
}
