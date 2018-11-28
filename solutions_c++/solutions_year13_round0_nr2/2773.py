//
//  main.cpp
//  GCJ_3
//
//  Created by Yutian Liu on 13-4-13.
//  Copyright (c) 2013年 Yutian Liu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <list>
using namespace std;

struct point
{
    int x;
    int y;
};

vector <point> sort(vector <vector <int>> farm, int N, int M, int &lessMin, int &min, int &max)
{
    int i,j;
    vector <point> res;
    lessMin = 1000, min = 1000, max = -1;
    for(i=0;i<N;i++)
    {
        for(j=0;j<M;j++)
        {
            if(farm[i][j] < min)
            {
                lessMin = min;
                min = farm[i][j];
            }
            if(farm[i][j] > max)
                max = farm[i][j];
        }
    }
    
    for(i=0;i<N;i++)
    {
        for(j=0;j<M;j++)
        {
            if(farm[i][j] == min)
            {
                point newP;
                newP.x = i;
                newP.y = j;
                res.push_back(newP);
            }
        }
    }
     
    return res;
}

bool check(vector <vector <int>> farm,  int N, int M, point P)
{
    return true;
}

bool try_hori(vector <vector <int>> farm,  int N, int M, point P,int lessMin)
{
    int i,j;
    i = P.x;
    j = P.y;
    int temp = farm[i][j];
    if(farm[i][0] != temp)
        return false;
    else if(farm[i][M-1] != temp)
        return false;
    else
    {
        for(j=0;j<M;j++)
            farm[i][j] = lessMin;//逐次递进,待修改
        return true;
    }
}

bool try_vert(vector <vector <int>> farm,  int N, int M, point P, int lessMin)
{
    int i,j;
    i = P.x;
    j = P.y;
    int temp = farm[i][j];
    if(farm[0][j] != temp)
        return false;
    else if(farm[N-1][j] != temp)
        return false;
    else
    {
        for(i=0;i<N;i++)
            farm[i][j] = lessMin;//逐次递进,待修改
        return true;
    }
}

bool try_point(vector <vector <int>> farm,  int N, int M)
{
    int min,lessMin,max;
    int i,j,m;
    vector <point> mins = sort(farm,N,M,lessMin,min,max);
    if(min == max || min == 100)
        return true;
    else
    {
        for(m=0;m<mins.size();m++)
        {
            vector <vector <int>> newFarm;
            for(i=0;i<N;i++)
            {
                vector <int> k1;
                for(j=0;j<M;j++)
                {
                    k1.push_back(farm[i][j]);
                }
                newFarm.push_back(k1);
            }
            if(try_hori(newFarm, N, M, mins[m],lessMin))
            {
                if(try_point(newFarm,N,M))
                    return true;
            }
            if(try_vert(newFarm, N, M, mins[m],lessMin))
            {
                if(try_point(newFarm,N,M))
                    return true;
            }
        }
        return false;
    }
}

//////////////////
/*
bool tryRow(vector <vector <int>> &farm,  int N, int M, int row, int min, int setNew)
{
    bool same = false;
    int i;
    if(farm[row][0] == min && farm[row][M-1] == min)
        same = true;
    if(same)
    {
        for(i=0;i<M;i++)
        {
            farm[row][i] = setNew;
        }
        return true;
    }
    else
        return false;
}

bool tryCol(vector <vector <int>> &farm,  int N, int M, int col, int min, int setNew)
{
    bool same = false;
    int i;
    if(farm[0][col] == min && farm[N-1][col] == min)
        same = true;
    if(same)
    {
        for(i=0;i<N;i++)
        {
            farm[i][col] = setNew;
        }
        return true;
    }
    else
        return false;
}

bool recur(vector <vector <int>> farm,  int N, int M)
{
    int min,lessMin,max;
    int i,j,m;
    vector <point> mins = sort(farm,N,M,lessMin,min,max);
    if(min == max || min == 100)
        return true;
    else
    {
        list <int> rows,cols;
        for(m=0;m<mins.size();m++)
        {
            rows.push_back(mins[m].x);
            cols.push_back(mins[m].y);
        }
        rows.sort();
        cols.sort();
        int last = -1;
        while(!rows.empty())
        {
            if(last != rows.front())
            {
                vector <vector <int>> newFarm;
                for(i=0;i<N;i++)
                {
                    vector <int> k1;
                    for(j=0;j<M;j++)
                    {
                        k1.push_back(farm[i][j]);
                    }
                    newFarm.push_back(k1);
                }
                last = rows.front();
                if(tryRow(newFarm,N,M,last,min,min+1))
                {
                    if(recur(newFarm,N,M))
                        return true;
                }
            }
            rows.pop_front();
        }
        last = -1;
        while(!cols.empty())
        {
            if(last != cols.front())
            {
                vector <vector <int>> newFarm;
                for(i=0;i<N;i++)
                {
                    vector <int> k1;
                    for(j=0;j<M;j++)
                    {
                        k1.push_back(farm[i][j]);
                    }
                    newFarm.push_back(k1);
                }
                last = cols.front();
                if(tryCol(newFarm,N,M,last,min,min+1))
                {
                    if(recur(newFarm,N,M))
                        return true;
                }
            }
            cols.pop_front();
        }
        return false;
    }
}


bool tryCol(vector <vector <int>> &farm, vector <vector <int>> final, int N, int M, int col, int setNew)
{
    int i;
    for(i=0;i<N;i++)
    {
        if(setNew < final[i][col])
        {
            return false;
        }
        else
            farm[i][col] = setNew;
    }
    return true;
}

bool tryRow(vector <vector <int>> &farm, vector <vector <int>> final, int N, int M, int row, int setNew)
{
    int i;
    for(i=0;i<M;i++)
    {
        if(setNew < final[row][i])
        {
            return false;
        }
        else
            farm[row][i] = setNew;
    }
    return true;
}

bool recur(vector <vector <int>> farm, vector <vector <int>> final, int N, int M)
{
    int i,j;
    for(i=0;i<N;i++)
    {
        vector <vector <int>> newFarm;
        for(i=0;i<N;i++)
        {
            vector <int> k1;
            for(j=0;j<M;j++)
            {
                k1.push_back(farm[i][j]);
            }
            newFarm.push_back(k1);
        }
        
        tryRow(newFarm, final, N, M, I, <#int setNew#>)

    }
    for(j=0;j<M;j++)
    {
        
    }

}
*/


bool checkPoint(vector <vector <int>> farm, int N, int M, point P)
{
    int i;
    bool flag = true;
    for(i=0;i<N;i++)
    {
        if(farm[i][P.y] > farm[P.x][P.y])
        {
            flag = false;
            break;
        }
    }
    if(flag)
        return true;
    for(i=0;i<M;i++)
    {
        if(farm[P.x][i] > farm[P.x][P.y])
        {
            return false;
        }
    }
    return true;
}

bool recur(vector <vector <int>> farm,  int N, int M)
{
    int min,lessMin,max;
    int i;
    vector <point> mins = sort(farm,N,M,lessMin,min,max);
    cout << mins.size() <<endl;
    for(i=0;i<mins.size();i++)
    {
        
        if(!checkPoint(farm, N, M, mins[i]))
            return false;
    }
    return true;
    
}

int main(int argc, const char * argv[])
{
    int N,M,numOfSample;
    int i;
    vector <vector <int>> farm;
    ifstream infile;
    infile.open("input.txt",ios::in);
    ofstream outfile;
    outfile.open("output.txt",ios::out);
    infile >> numOfSample;
    
    for(i=0;i<numOfSample;i++)
    {
        infile >> N >> M;
        int m,n;
        for(n=0;n<N;n++)
        {
            vector <int> k1;
            for(m=0;m<M;m++)
            {
                int t;
                infile >> t;
                k1.push_back(t);
            }
            farm.push_back(k1);
        }
        bool res = recur(farm, N, M);
        farm.clear();
        outfile << "Case #" << i+1 <<": ";
        if(res)
            outfile << "YES" << endl;
        else
            outfile << "NO" << endl;
    }
    infile.close();
    outfile.close();
    return 0;
}

