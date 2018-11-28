//
//  main.cpp
//  codejam_dijkstra
//
//  Created by Alexandru Andronache on 11/04/15.
//  Copyright (c) 2015 Alexandru Andronache. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

enum Chars
{
    ONE,
    LETTER_I,
    LETTER_J,
    LETTER_K
};

int T, L, X;
char *sir;

struct position
{
    position(int _x, int _l)
    {
        x = _x;
        l = _l;
    }
    bool addOne()
    {
        l++;
        if (l == L)
        {
            x++;
            l = 0;
        }
        if (x == X)
        {
            return false;
        }
        return true;
    }
    bool isBigger(position p)
    {
        if (x > p.x) return true;
        if (x < p.x) return false;
        if (x == p.x)
        {
            if (l > p.l) return true;
            if (l <= p.l) return false;
        }
        return false;
    }
    int x;
    int l;
};

struct character
{
    character(char c)
    {
        if (c == 'i') p = LETTER_I;
        if (c == 'j') p = LETTER_J;
        if (c == 'k') p = LETTER_K;
        isNegativ = false;
    }
    void multiply(character c)
    {
        bool changeSign = false;
        switch (c.p)
        {
            case LETTER_I:
                switch (p)
                {
                    case ONE:
                        p = LETTER_I;
                        break;
                    case LETTER_I:
                        p = ONE;
                        changeSign = true;
                        break;
                    case LETTER_J:
                        p = LETTER_K;
                        changeSign = true;
                        break;
                    case LETTER_K:
                        p = LETTER_J;
                        break;
                }
                break;
            case LETTER_J:
                switch (p)
                {
                    case ONE:
                        p = LETTER_J;
                        break;
                    case LETTER_I:
                        p = LETTER_K;
                        break;
                    case LETTER_J:
                        p = ONE;
                        changeSign = true;
                        break;
                    case LETTER_K:
                        p = LETTER_I;
                        changeSign = true;
                        break;
                }
                break;
            case LETTER_K:
                switch (p)
                {
                    case ONE:
                        p = LETTER_K;
                        break;
                    case LETTER_I:
                        p = LETTER_J;
                        changeSign = true;
                        break;
                    case LETTER_J:
                        p = LETTER_I;
                        break;
                    case LETTER_K:
                        p = ONE;
                        changeSign = true;
                        break;
                }
                break;
            case ONE: //todo
                switch (p)
                {
                    case ONE:
                        p = ONE;
                        break;
                    case LETTER_I:
                        p = LETTER_I;
                        break;
                    case LETTER_J:
                        p = LETTER_J;
                        break;
                    case LETTER_K:
                        p = LETTER_K;
                        break;
                }
                break;
        }
        if (changeSign)
        {
            isNegativ = !isNegativ;
        }
        if (c.isNegativ)
        {
            isNegativ = !isNegativ;
        }
    }
    bool isI()
    {
        return (p == LETTER_I && !isNegativ);
    }
    bool isK()
    {
        return (p == LETTER_K && !isNegativ);
    }
    Chars p;
    bool isNegativ;
};

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");



vector<position> pozI;
vector<position> pozK;
vector<position> posIback;

char getLetter(char *s, int x, int l)
{
    return s[l];
}

int main(int argc, const char * argv[])
{
    fscanf(f, "%d", &T);
    
    for (int t = 1; t <= T; ++t)
    {
        fscanf(f, "%d %d\n", &L, &X);
        sir = new char[L + 1];
        fgets(sir, L + 1, f);
        
        character p(sir[0]);
        if (p.isI())
        {
            pozI.push_back(position(0, 0));
        }
        
        for (int i = 0; i < X; ++i)
        {
            int startPos = 0;
            if (i == 0) startPos = 1;
            for (int j = startPos; j < L; ++j)
            {
                character t(getLetter(sir, i, j));
                p.multiply(t);
                if (p.isI())
                {
                    pozI.push_back(position(i, j));
                }
            }
        }
        
        character p2(sir[L - 1]);
        if (p2.isK())
        {
            pozK.push_back(position(X - 1, L - 1));
        }
        if (p2.isI())
        {
            posIback.push_back(position(X - 1, L - 1));
        }
        
        for (int i = X - 1; i >= 0; --i)
        {
            int startPos = L - 1;
            if (i == X - 1) startPos = L - 2;
            for (int j = startPos; j >= 0; --j)
            {
                character t(getLetter(sir, i, j));
                t.multiply(p2);
                p2 = t;
                if (p2.isK())
                {
                    pozK.push_back(position(i, j));
                }
                if (p2.isI())
                {
                    posIback.push_back(position(i, j));
                }
            }
        }
        
        bool final_result = false;
        for (int i = 0; i < pozI.size() && !final_result; ++i)
        {
            bool result = true;
            position p = pozI[i];
            if (!p.addOne())
            {
                result = false;
            }
            
            bool found = false;
            for (int j = pozK.size() - 1; j >= 0 && !found; --j)
            {
                if (pozK[j].isBigger(p))
                    found = true;
            }
            
            if (!found) result = false;
            
            if (result)
            {
                bool found = false;
                for (int k = 0; k < posIback.size() && !found; ++k)
                {
                    if (posIback[k].x == p.x && posIback[k].l == p.l)
                    {
                        found = true;
                    }
                }
                if (found)
                {
                    result = true;
                }
                else
                {
                    result = false;
                }
            }
            if (result)
            {
                final_result = true;
            }
        }
        
        if (final_result)
        {
            fprintf(g, "Case #%d: YES\n", t);
        }
        else
        {
            fprintf(g, "Case #%d: NO\n", t);
        }
        
        
        pozI.clear();
        pozK.clear();
        posIback.clear();
        delete sir;
    }
    
    return 0;
}
