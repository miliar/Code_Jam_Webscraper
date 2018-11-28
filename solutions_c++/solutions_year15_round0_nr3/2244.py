//
//  c.cpp
//  CodeJam15
//
//  Created by Ahmed Mohammed on 4/11/15.
//  Copyright (c) 2015 Better. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>


using namespace std;

// 1 -> 1
// i -> 2
// j -> 3
// k -> 4
// -x -> -(x)


int mul(int x, int y)
{
    static int prods[5][5] =
    {
        {0, 0, 0, 0, 0},
        {0, 1, 2, 3, 4},       // 1
        {0, 2, -1, 4, -3},     // i
        {0, 3, -4, -1, 2},     // j
        {0, 4, 3, -2,-1}       // k
    };
    
    bool inv = false;
    if (x < 0) { x = -x; inv = !inv;}
    if (y < 0) { y = -y; inv = !inv;}
    
    return inv ? -prods[x][y] : prods[x][y];
}




int main(int argc, const char * argv[])
{
    if (argc < 3) { printf("Usage: %s <input file> <output file>\n", argv[0]); exit(1);}
    
    ifstream fin(argv[1], ios::in|ios::ate);
    if (!fin.is_open()) { printf("Unable to open input file\n"); exit(1);}
    fin.seekg(0);
    
    ofstream fout(argv[2], ios::out|ios::ate);
    if (!fout.is_open()) { printf("Unable to open output file\n"); exit(1);}
    fout.seekp(0);
    
    fout.precision(7);
    fout.setf(ios::fixed);
    
    
    // solve cases
    uint64_t testcase_count;
    fin >> testcase_count;
    for (uint64_t tcase = 0; tcase < testcase_count; tcase++)
    {
        int64_t l, x;
        fin >> l >> x;
        int s[l];
        for (int i = 0; i < l; i++) { char ch; fin >> ch; s[i] = (ch - 'i') + 2;}
        
        bool sol = false;
        
        int fp[l];
        fp[0] = s[0]; for (int i = 1; i < l; i++) fp[i] = mul(fp[i-1], s[i]);
        int pp = fp[l-1];
        
        bool impossible = false;
        if (pp == 1) impossible = true;
        else if (pp == -1) { if (!(x & 1)) impossible = true;}
        else if ((x + 2) & 3) impossible = true;
        
        if (!impossible)
        {
            int bp[l];
            bp[l-1] = s[l-1]; for (int64_t i = l-2; 0 <= i; i--) bp[i] = mul(s[i], bp[i+1]);
            
            uint64_t iidx = UINT64_MAX, kidx = UINT64_MAX;
            
            if (pp == -1)
            {
                // i
                {
                    int mi = -1;
                    for (int i = 0; i < l; i++) if (fp[i] == 2) { mi = i; break;}
                    if (mi == -1)
                    {
                        for (int i = 0; i < l; i++) if (fp[i] == -2) { mi = i; break;}
                        if (mi != -1) mi += l;
                    }
                    
                    if (mi != -1) iidx = mi;
                }
                
                // k
                {
                    int mk = -1;
                    for (int i = (int)l-1; 0 <= i; i--) if (bp[i] == 4) { mk = (int)l-i-1; break;}
                    if (mk == -1)
                    {
                        for (int i = (int)l-1; 0 <= i; i--) if (bp[i] == -4) { mk = (int)l-i-1; break;}
                        if (mk != -1) mk += l;
                    }
                    
                    if (mk != -1) kidx = mk;
                }
            }
            else
            {       // pp = i, j, k
                // i
                {
                    int mi = -1;
                    int k;
                    int pg = 0;
                    
                    if (mi == -1) { k = 2; for (int i = 0; i < l; i++) if (fp[i] == k) { mi = i + pg; break;}}
                    
                    pg += (int)l;
                    if (mi == -1) { k = mul(-pp, 2); for (int i = 0; i < l; i++) if (fp[i] == k) { mi = i + pg; break;}}
                    
                    pg += (int)l;
                    if (mi == -1) { k = -2; for (int i = 0; i < l; i++) if (fp[i] == k) { mi = i + pg; break;}}
                    
                    pg += (int)l;
                    if (mi == -1) { k = mul(pp, 2); for (int i = 0; i < l; i++) if (fp[i] == k) { mi = i + pg; break;}}
                    
                    if (mi != -1) iidx = mi;
                }
                
                // k
                {
                    int mk = -1;
                    int k;
                    int pg = 0;
                    
                    if (mk == -1) { k = 4; for (int i = (int)l-1; 0 <= i; i--) if (bp[i] == k) { mk = (int)l-i-1 + pg; break;}}
                    
                    pg += (int)l;
                    if (mk == -1) { k = mul(4, -pp); for (int i = (int)l-1; 0 <= i; i--) if (bp[i] == k) { mk = (int)l-i-1 + pg; break;}}
                    
                    pg += (int)l;
                    if (mk == -1) { k = -4; for (int i = (int)l-1; 0 <= i; i--) if (bp[i] == k) { mk = (int)l-i-1 + pg; break;}}
                    
                    pg += (int)l;
                    if (mk == -1) { k = mul(4, pp); for (int i = (int)l-1; 0 <= i; i--) if (bp[i] == k) { mk = (int)l-i-1 + pg; break;}}
                    
                    if (mk != -1) kidx = mk;
                }
            }
            
            sol = ((iidx != UINT64_MAX) && (kidx != UINT64_MAX) && ((iidx + kidx + 2) < (l * x)));
        }
        
        fout << "Case #" << (tcase + 1) << ": " << (sol ? "YES" : "NO") << endl;
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}

