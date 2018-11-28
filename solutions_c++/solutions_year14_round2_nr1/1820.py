// problem1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set> 
#include <algorithm>

using namespace std; 

struct Rec {
    char c; 
    int num; 
};

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream inf (argv[1]);
    // ifstream inf("D:\\codejam\\problem1\\Debug\\test.txt"); 

	int TC;
    inf >> TC; 

	for (int T = 1; T <= TC; T++){
		int n; 
        inf >> n; 
        vector<string> v; 
        for (int i=0; i<n; i++) {
            string s ;
            inf >> s;
            v.push_back(s);
        }

        vector< vector<Rec> > recs; 
        for (int i=0; i<v.size(); i++) {
            Rec rec; 
            rec.c = v[i][0];
            rec.num = 1;
            vector<Rec> tempv; 
            for (int j=1; j<v[i].size(); j++) {
                if (v[i][j] == rec.c) rec.num++;
                else {
                    tempv.push_back(rec);
                    rec.c = v[i][j];
                    rec.num = 1;
                }
            }
            tempv.push_back(rec);
            recs.push_back(tempv);
        }

        bool nowin = false;
        int maxm = recs[0].size(); 
        for (int i=1; i<recs.size(); i++) {
            if (maxm != recs[i].size()) {
                nowin = true;
                break;
            }
        }

        int minnum = 0; 
        if (!nowin) {
            for (int seq=0; seq<maxm; seq++) {
                char c = recs[0][seq].c;
                int total = recs[0][seq].num;
                for (int i=1; i<recs.size(); i++) {
                    if (recs[i][seq].c != c) {
                        nowin = true;
                        break;
                    }
                    else {
                        total += recs[i][seq].num;
                    }
                }
                if (nowin) {
                    break;
                }
                else {
                    total /= n; 
                    for (int i=0; i<recs.size(); i++) {
                        minnum += abs(recs[i][seq].num - total);
                    }
                }
            }
        }

        if (nowin) {
            cout << "Case #" << T << ": Fegla Won" << endl;
        }
        else {
            cout << "Case #" << T << ": " << minnum << endl;
        }
	}
	return 0;
}

