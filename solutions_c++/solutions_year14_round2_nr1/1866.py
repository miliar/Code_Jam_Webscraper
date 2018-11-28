//
//  main.cpp
//
//  Created by Xiaowei Ma.
//  Copyright (c) 2014 Xiaowei Ma. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

struct Node
{
    int letter;
    int num;
    Node(int _val = 0):num(_val){}
};


int main()
{
    //--------------- I/O ---------------------------------
    ifstream in;
    in.open("/Users/xiaoweima/Desktop/CodeJam/in");

    ofstream out;
    out.open("/Users/xiaoweima/Desktop/CodeJam/out");


    int T;
    in>>T;

    //-------------  sovle  ------------------------------

    for (int ca = 1; ca <= T; ca++)
    {
        vector<Node> a[100];

        int n;
        in>>n;

        for (int i = 0; i < n; i++)
        {
            string s;
            in>>s;

            int lastLetter = -1;

            for (int j = 0; j < s.size(); j++)
            {
                int letter = s[j] - 'a';
                if (letter == lastLetter)
                {
                    a[i][a[i].size()-1].num++;
                }
                else
                {
                    Node temp;
                    temp.letter = letter;
                    temp.num++;
                    a[i].push_back(temp);
                    lastLetter = letter;
                }
            }
        }

        // --- test if possible ----
        bool possible = true;

        int baseL = a[0].size();
        for (int i = 0; i < n; i++)
        {
            if (baseL != a[i].size())
            {
                possible = false;
                break;
            }
        }

        if (!possible)
        {
            out<<"Case #"<<ca<<": "<<"Fegla Won"<<endl;
            continue;
        }

        for (int j = 0; j < baseL; j++)
        {
            int baseLetter = a[0][j].letter;
            for (int i = 0; i < n; i++)
            {
                if (a[i][j].letter != baseLetter)
                {
                    possible = false;
                    break;
                }
            }
            if (!possible)
            {
                break;
            }
        }
        if (!possible)
        {
            out<<"Case #"<<ca<<": "<<"Fegla Won"<<endl;
            continue;
        }

        //-----  find  min --------

        int ans = 0;

        for (int j = 0; j < baseL; j++)
        {
            int sum = 0;
            for (int i = 0; i < n; i++)
            {
                sum += a[i][j].num;
            }
            sum = sum/n;

            for (int i = 0; i < n; i++)
            {
                int added = sum - a[i][j].num;
                added = added < 0 ? -added : added;
                ans += added;
            }
        }

        out<<"Case #"<<ca<<": "<<ans<<endl;

    }




    //------------  finishing  -----------------------------
    in.close();
    out.close();
    return 0;
}



