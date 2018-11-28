#include <string>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;

struct Line {
        int _lowerBound;
        int _i;
        bool _horiz;
        
        Line(): _lowerBound(){}

};


bool playLine(list<Line>::iterator itL,list<Line>::iterator itLEnd,vector <vector <int> > &iGame, vector<vector <bool> > &iSolved,int iSolvedCount, int N, int M)
{
    if(iSolvedCount == N*M)
    {
        return true;
    }
    if (itL == itLEnd)
    {
        return false;
    }

    // play the line
    
    int  playedCases[100];
    int playedCases_Localcount=0;

    auto &l = *itL;
    auto itL2 = itL;
    ++itL2;

    if(l._horiz)
    {
        unsigned int n=l._i;
        for(unsigned int m=0;m < M;++m)
        {
            if(iGame[n][m] == l._lowerBound && !iSolved[n][m])
            {
                iSolved[n][m]=true;
                playedCases[playedCases_Localcount]=m;
                ++playedCases_Localcount;
            }
        }
    }
    else
    {
        unsigned int m=l._i;
        for(unsigned int n=0;n < N;++n)
        {
            if(iGame[n][m] == l._lowerBound && !iSolved[n][m])
            {
                iSolved[n][m]=true;
                playedCases[playedCases_Localcount]=n;
                ++playedCases_Localcount;
            }
        }
    }

    if(playLine(itL2, itLEnd, iGame, iSolved,iSolvedCount + playedCases_Localcount, N, M))
    {
        return true;
    }

    if(playedCases_Localcount != 0)
    {

        if(l._horiz)
        {
            unsigned int n=l._i;
            for (int i=0;i< playedCases_Localcount;++i)
            {
                iSolved[n][i] = false;
            }

        }
        else
        {
            unsigned int m=l._i;
            for (int i=0;i< playedCases_Localcount;++i)
            {
                iSolved[i][m] = false;
            }
        }

        return playLine(itL2, itLEnd, iGame, iSolved,iSolvedCount, N, M);
    }

    return false;

}



int main()
{
    unsigned int pb_total;
    cin >> pb_total;
   
    for (unsigned int pb_idx = 1;pb_idx <= pb_total;++pb_idx)
    {
        cerr << "Case #" << pb_idx << endl;
        unsigned int N,M;
        cin >> N >> M;

        vector<vector<int> > squares;
        vector<vector<bool> > solved_squares;
        for (unsigned int n = 0; n < N;++n)
        {
            squares.push_back(vector<int> ());
            auto &squares_n = squares.back();
            solved_squares.push_back(vector<bool>());
            for (unsigned int m = 0; m < M;++m)
            {
                squares_n.push_back(int());
                auto & square_nm = squares_n.back();
                cin >> square_nm;

                solved_squares.back().push_back(false);
            }

        }

        list<Line> lines;
        // instantiate the lines
        //horizontal:
        for (unsigned int n = 0; n < N;++n)
        {
            lines.push_back(Line());
            auto &l = lines.back();
            l._horiz=true;
            l._i=n;

            for (unsigned int m=0; m< M; ++m)
            {
                if(squares[n][m]>l._lowerBound)
                {
                    l._lowerBound=squares[n][m];
                }
            }
        }
        // vertical:
        for (unsigned int m = 0; m < M;++m)
        {
            lines.push_back(Line());
            auto &l = lines.back();
            l._horiz = false;
            l._i=m;

            for (unsigned int n=0; n< N; ++n)
            {
                if(squares[n][m]>l._lowerBound)
                {
                    l._lowerBound=squares[n][m];
                }
            }
        }

        cout << "Case #" << pb_idx << ": "; 
        if (playLine(lines.begin(),lines.end(), squares,solved_squares, 0, N, M))
        { 
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
}
