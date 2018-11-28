#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <iomanip> 
using namespace std;

#define SELECTED 200
#define MINE 100


unsigned char m[7][7];
unsigned char m2[7][7];

int rt, ct, mt;

void print()
{
    for(int r = 1; r <= rt; r++)
    {
        for(int c = 1; c <= ct; c++)
        {
            cout << (char)(m[r][c] >= MINE ? (m[r][c] == SELECTED ? 'c' : '*') : '.');
        }
        cout << endl;
    }
}



int bfs(int r,int c)
{
    if(r == 0 || c == 0 || r == rt + 1 || c == ct + 1)
        return 0;
    if(m[r][c] == 0)
    {
        m[r][c] = 25;
        return 1 + bfs(r - 1, c) + bfs(r + 1, c) 
            + bfs(r, c + 1) + bfs(r, c - 1)
                + bfs(r - 1, c + 1) + bfs(r + 1, c - 1) 
              + bfs(r + 1, c + 1) + bfs(r - 1, c - 1); 
    }
    else
        return 0;
}

int main(){
    int total_cases;
    cin >> total_cases;
    for(int cur_case = 1; cur_case <= total_cases ; cur_case++ )
    {
        cin >> rt >> ct >> mt;
        cout << "Case #" << cur_case << ":\n";
        
        for(int i = 0; i < (1 << rt *ct ); i++)
        {
            int mcount = 0;
            for(int r = 1; r <= rt; r++)
                for(int c = 1; c <= ct; c++)
            {
                m[r][c] = !!(i & (1 << ((r - 1) * ct + (c - 1))));
                mcount += m[r][c];
                m[r][c] = m[r][c] == 1 ? 100 : 0;
            }
            if(mcount != mt)
                continue;
            
            for(int r = 1; r <= rt; r++)
                for(int c = 1; c <= ct; c++)
                {
                    if(m[r][c] < MINE)
                        continue;
                    m[r][c + 1] ++;
                    m[r][c - 1] ++;
                    m[r + 1][c] ++;
                    m[r - 1][c] ++;
                    m[r + 1][c + 1] ++;
                    m[r - 1][c - 1] ++;
                    m[r + 1][c - 1] ++;
                    m[r - 1][c + 1] ++;
                }
                //print();
                int zero_count = 0;
                
            if(mt == rt * ct - 1)
            {
                for(int r = 1; r <= rt; r++)
                    for(int c = 1; c <= ct; c++)
                    {
                        if(m[r][c] < MINE)
                            m[r][c] = SELECTED;
                    }
                    goto succ_print; 
            }
            // connect set
            for(int r = 1; r <= rt; r++)
                for(int c = 1; c <= ct; c++)
                {
                    if(m[r][c] == 0)
                        zero_count++;
                }
                
                //cout << zero_count << "S1\n";
            if(zero_count == 0 && mt < rt * ct - 1) 
                goto failed_try; 
            
            for(int r = 1; r <= rt; r++)
                for(int c = 1; c <= ct; c++)
                {
                    if(m[r][c] == 0 && bfs(r,c) < zero_count)
                        goto failed_try;
                }    
                // cout << "S2\n";
                      
            // cover 
            memset(m2, 0, sizeof(m2));
            for(int r = 1; r <= rt; r++)
                for(int c = 1; c <= ct; c++)
                {
                    if(m[r][c] == 25)
                    {
                        m2[r][c + 1] = 50;
                        m2[r][c - 1] = 50;
                        m2[r + 1][c] = 50;
                        m2[r - 1][c] = 50;
                        m2[r + 1][c + 1] = 50;
                        m2[r - 1][c - 1] = 50;
                        m2[r + 1][c - 1] = 50;
                        m2[r - 1][c + 1] = 50;
                    }
                }
                //cout << "S3\n";
            for(int r = 1; r <= rt; r++)
                for(int c = 1; c <= ct; c++)
                {
                    if(m[r][c] < 20  && m[r][c] > 0 && m2[r][c] != 50)
                    {
                        //cout << r << "^^^" << c << "!!!" << (int)m[r][c] << "\n";
                        goto failed_try;
                        
                    }
                }
               // cout << "S4\n";
                
            for(int r = 1; r <= rt; r++)
                for(int c = 1; c <= ct; c++)
                {
                    if(m[r][c] == 25)
                    {
                        m[r][c] = SELECTED;
                        goto succ_print;
                    }
                }     
               //  cout << "S5\n";
                
            succ_print:
            print();
            goto succ; 
            
            failed_try:
            
            
            // TEST 
            
            continue;
        }
        cout << "Impossible\n";
        succ:
        continue;
    }
    return 0;
}
