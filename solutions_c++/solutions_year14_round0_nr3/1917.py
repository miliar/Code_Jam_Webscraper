#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include "windows.h"

using namespace std;

void UpdateMap(vector<int> &map, int x, int y, int R, int C)
{
    int mines = 0;
    if(x!=0)
    {
        if(map[(x-1)+(y)*C] > 0)
            mines ++;

        if(y!=0)
            if(map[(x-1)+(y-1)*C] > 0)
                mines ++;

        if(y!=R-1)
            if(map[(x-1)+(y+1)*C] > 0)
                mines ++;
    }

    if(x!=C-1)
    {
        if(map[(x+1)+(y)*C] > 0)
            mines ++;

        if(y!=0)
            if(map[(x+1)+(y-1)*C] > 0)
                mines ++;

        if(y!=R-1)
            if(map[(x+1)+(y+1)*C] > 0)
                mines ++;
    }

    if(y!=0)
    {
        if(map[(x)+(y-1)*C] > 0)
            mines ++;
    }

    if(y!=R-1)
    {
        if(map[(x)+(y+1)*C] > 0)
            mines ++;
    }

    if(mines == 0)
        map[(x)+(y)*C] = -100;
    else
        map[(x)+(y)*C] = -mines;
}

int TestMap(vector<int> &map, int minesCount, int x, int y, int R, int C)
{
    int s = 0;

    if(x < 0 || y < 0)
        return 0;

    if(x >= C || y >= R)
        return 0;

    int qqq = map[(x)+(y)*C];

    if(map[(x)+(y)*C] < 0)
        return 0;

    UpdateMap(map,x,y,R,C);
    s++;

    if(map[(x)+(y)*C] == -100)
    {
        s += TestMap(map, minesCount, x-1, y, R, C);
        s += TestMap(map, minesCount, x-1, y-1, R, C);
        s += TestMap(map, minesCount, x-1, y+1, R, C);

        s += TestMap(map, minesCount, x+1, y, R, C);
        s += TestMap(map, minesCount, x+1, y-1, R, C);
        s += TestMap(map, minesCount, x+1, y+1, R, C);

        s += TestMap(map, minesCount, x, y-1, R, C);
        s += TestMap(map, minesCount, x, y+1, R, C);    
    }

    return s;
}


bool FindSolution(int mineNumber, int minesCount, int lastPosition, vector<int> &map, vector<int> &res, int R, int C)
{
    if(mineNumber == minesCount+2)
    {
        vector<int> map2 = map;

        int x = lastPosition % C;
        int y = lastPosition / C;

        int openedCels = TestMap(map2, minesCount, x, y, R, C);
        if(openedCels == R*C - minesCount)
        {
            res = map;
            return true;
        }

        return false;
    }

    if(R*C - (lastPosition + 1) < minesCount+1-mineNumber+1)
        return false;

    for(int i=lastPosition+1; i<map.size(); i++)
    {
        int xOld = lastPosition % C;
        int yOld = lastPosition / C;

        int x = i % C;
        int y = i / C;

        vector<int> map2 = map;

        map2[i] = mineNumber;

        if(FindSolution(mineNumber+1,minesCount,i,map2, res, R, C))
            return true;
    }

    return false;
}

void CreateTemplate3(int minesCount, vector<int> &map, int R, int C)
{
    int mine = 0;
    int i,j;

    for( i = 0; i<R-3; i++)
        for(j=0; j<C; j++)
            map[i*C+j] = ++mine;

    for(j=0; j<C-3; j++)
        map[i*C+j] = ++mine;

    i=R-2;
    j=0;

    while(mine < minesCount)
    {
        map[i*C+j] = ++mine;
        if(i != R-1)
            i++;
        else
        {
            i = R-2;
            j++;
        }
    }
}

void CreateTemplate2(int minesCount, vector<int> &map, int R, int C)
{
    int mine = 0;
    int i,j;

    for( i = 0; i<R-2; i++)
        for(j=0; j<C; j++)
            map[i*C+j] = ++mine;

    i=R-2;
    j=0;

    while(mine < minesCount)
    {
        map[i*C+j] = ++mine;
        if(i != R-1)
            i++;
        else
        {
            i = R-2;
            j++;
        }
    }
}

bool CheckTemplate(int minesCount, vector<int> &res, int R, int C)
{
    int fullRows = minesCount / C;

    vector<int> map(R*C);

    if(C <= 3)
        return false;

    if(minesCount == R*C - 1)
        return false;

    if(fullRows >= R - 2)
    {
        CreateTemplate3(minesCount, map, R, C);

        for(int i=0; i<map.size(); i++)
        {
            if(map[i] == 0)
            {
                int x = i % C;
                int y = i / C;

                vector<int> map2 = map;
                map2[i]=minesCount+1;

                int openedCels = TestMap(map2, minesCount, x, y, R, C);
                if(openedCels == R*C - minesCount)
                {
                    map[i]=minesCount+1;
                    res = map;
                    return true;
                }
            }
            
        }

        for(int i=0; i<map.size(); i++)
            map[i] = 0;

        CreateTemplate2(minesCount, map, R, C);

        for(int i=0; i<map.size(); i++)
        {
            if(map[i] == 0)
            {
                int x = i % C;
                int y = i / C;

                vector<int> map2 = map;
                map2[i]=minesCount+1;

                int openedCels = TestMap(map2, minesCount, x, y, R, C);
                if(openedCels == R*C - minesCount)
                {
                    map[i]=minesCount+1;
                    res = map;
                    return true;
                }
            }

        }

        return false;
    }

}
 

void main()
{
    int T = 0;

    ifstream in("C-small-attempt2.in");
    ofstream out("C-small-attempt2.out");

    in >> T;

    for(int i=0; i<T; ++i)
    {
        int R, C, M, F;
        bool isOneClick;
        in >> R >> C>> M;

        F = R*C-M;

        vector<int> map(R*C), r(R*C);
        int start = GetTickCount();

        isOneClick = FindSolution(1,M,-1,map,r, R, C);
        
        //if(R ==1 || C == 1)
        //{
        //    isOneClick = FindSolution(1,M,-1,map,r, R, C);
        //}
        //else
        //    if(R == 2 || C == 2)
        //    {
        //        if( (M%2 == 0 && F!=2) || F==1 )
        //            isOneClick = FindSolution(1,M,-1,map,r, R, C);
        //        else
        //            isOneClick = false;
        //    }
        //    else
        //        if(F == 2 || F == 3 || F == 5 || F == 7)
        //            isOneClick = false;
        //        else
        //        {
        //            //isOneClick = CheckTemplate(M,r,R,C);
        //            isOneClick=false;
        //            if(isOneClick == false)
        //                isOneClick = FindSolution(1,M,-1,map,r, R, C);
        //        }
        //    
        int finish = GetTickCount();

        out << "Case #" << i+1 << ": " << endl;
        cout << "Case #" << i+1 << ": " << finish-start << endl;

        if(isOneClick == false)
        {
            out << "Impossible";
            cout << "Impossible"<<endl;
        }
        else
        {
            vector<int>::iterator p = r.begin();

            for(int j=0; j<R; j++)
            {
                for(int k=0; k<C; k++)
                {
                    if(*p == 0)
                        out << ".";
                    else 
                        if(*p == M+1)
                            out << "c";
                        else 
                            out << "*";
                    p++;
                }
                if(j!=R-1)
                    out << endl;
            }
        }

        out << endl;
    }

}