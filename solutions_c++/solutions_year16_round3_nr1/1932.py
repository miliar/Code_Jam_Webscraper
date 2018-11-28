//
//  main.cpp
//  codejame
//
//  Created by Bui Van Chuong on 5/3/16.
//  Copyright © 2016 Bui Van Chuong. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#define INFILE 0
#define OUTFILE 0

using namespace std;

bool newsort(pair<int, char>  a1, pair<int, char>  a2)
{
    return a1.first > a2.first;
}
int main(int argc, const char * argv[]) {
    // insert code here...
#if INFILE
    
    std::ifstream in("input.txt");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
#endif
#if OUTFILE
    
    std::ofstream out("output.txt");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#endif
    int tt,n,m;
    cin >> tt;
    vector < pair<int, char> > v;
    for (int  t = 1; t <= tt; t++)
    {
        cin  >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> m;
            v.push_back(make_pair(m,i+'A'));
        }
        cout << "Case #" <<t<<": ";
        while (v.size() > 0) {
            sort(v.begin(), v.end(),newsort);
            if (v[0].first == 1 && v.size() == 3) {
                if (v[0].first == 1) {
                    v[0].first--;
                    cout<<v[0].second;
                    if (v[0].first == 0) {
                        v.erase(v.begin()+0);
                    }
                }
            }
            else
            {
                if (v.size() >= 2) {
                    v[0].first--;
                    cout<<v[0].second;
                    v[1].first--;
                    cout<<v[1].second;
                    if (v[1].first == 0) {
                        v.erase(v.begin()+1);
                    }
                    if (v[0].first == 0) {
                        v.erase(v.begin()+0);
                    }
                    
                }
                else
                {
                    if (v[0].first == 1) {
                        v[0].first--;
                        cout<<v[0].second;
                        if (v[0].first == 0) {
                            v.erase(v.begin()+0);
                        }
                    }
                    else if (v[0].first >= 2)
                    {
                        v[0].first--;
                        v[0].first--;
                        cout<<v[0].second<<v[0].second;
                        if (v[0].first == 0) {
                            v.erase(v.begin()+0);
                        }
                    }
                }
            }
            cout << " ";
        }
        cout << endl;
    }
        
#if INFILE
    std::cin.rdbuf(cinbuf);   //reset to standard input again
#endif
#if OUTFILE
    std::cout.rdbuf(coutbuf); //reset to standard output again
#endif
    
    return 0;
}
