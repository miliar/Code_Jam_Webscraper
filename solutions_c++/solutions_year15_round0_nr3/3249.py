#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

vector<vector<pair<int, char> > > mx;

unordered_map<char, int> map;

void init()
{
    map['1'] = 0;
    map['i'] = 1;
    map['j'] = 2;
    map['k'] = 3;

    pair<int, char> p11(1, '1');
    pair<int, char> p1i(1, 'i');
    pair<int, char> p1j(1, 'j');
    pair<int, char> p1k(1, 'k');
    vector<pair<int, char> > row1 = { p11, p1i, p1j, p1k };
    
    pair<int, char> pi1(1, 'i');
    pair<int, char> pii(-1, '1');
    pair<int, char> pij(1, 'k');
    pair<int, char> pik(-1, 'j');
    vector<pair<int, char> > rowi = { pi1, pii, pij, pik };

    pair<int, char> pj1(1, 'j');
    pair<int, char> pji(-1, 'k');
    pair<int, char> pjj(-1, '1');
    pair<int, char> pjk(1, 'i');
    vector<pair<int, char> > rowj = { pj1, pji, pjj, pjk };

    pair<int, char> pk1(1, 'k');
    pair<int, char> pki(1, 'j');
    pair<int, char> pkj(-1, 'i');
    pair<int, char> pkk(-1, '1');
    vector<pair<int, char> > rowk = { pk1, pki, pkj, pkk };

    mx = { row1, rowi, rowj, rowk };
}

pair<int, char> getCombine(pair<int, char> &a, pair<int, char> &b)
{
    pair<int, char> ans = mx[map[a.second]][map[b.second]];
    ans.first *= a.first * b.first;
    return ans;
}

bool match(pair<int, char> &a, pair<int, char> &b, pair<int, char> &target)
{
    pair<int, char> ans = getCombine(a, b);
    if (ans.first == target.first && ans.second == target.second)
    {
        return true;
    }
    return false;
}

bool matchOne(pair<int, char> &a, pair<int, char> &b)
{
    pair<int, char> one(1, '1');
    return match(a, b, one);
}

void main()
{
    init();

    FILE *infile = fopen("C-small-attempt0.in", "r");
    FILE *outfile = fopen("C-small-attempt0.out", "w");

    int T;
    fscanf(infile, "%d", &T);
    
    for (int i = 0; i < T; ++i)
    {
        int L, X;
        fscanf(infile, "%d %d", &L, &X);
        if (L*X < 3)
        {
            char *line = (char *)malloc(sizeof(char)* L);
            fscanf(infile, "%s", line);
            //free(line);
            fprintf(outfile, "Case #%d: NO\n", i + 1);
            continue;
        }

        char *line = (char *)malloc(sizeof(char)* L);
        fscanf(infile, "%s", line);

        pair<int, char> curAns(1, '1');
        pair<int, char> curTarget(1, 'i');
        for (int k = 0; k < X; ++k)
        {
            for (int j = 0; j < L; ++j)
            {
                pair<int, char> curB(1, line[j]);
                if (true == match(curAns, curB, curTarget))
                {
                    curAns.first = 1;
                    curAns.second = '1';
                    curTarget.second += 1;
                }
                else if (true == matchOne(curAns, curB))
                {
                    curAns.first = 1;
                    curAns.second = '1';
                }
                else
                {
                    curAns = getCombine(curAns, curB);
                }
                if (j == L-1 && k == X-1)
                {
                    if (curTarget.second == 'l' && curAns.first == 1 && curAns.second == '1')
                        fprintf(outfile, "Case #%d: YES\n", i + 1);
                    else
                        fprintf(outfile, "Case #%d: NO\n", i + 1);
                }
            }
        }
        //free(line);
    }

    fclose(infile);
    fclose(outfile);
}
