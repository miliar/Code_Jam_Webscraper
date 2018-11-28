#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstdlib>
#include <set>
#include <map>
#include <fstream>
#include <bitset>

#define PI 3.14159265359

using namespace std;

int main()
{
    freopen("p1.in", "r", stdin);
    freopen("p1.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int kras=1; kras<=tc; kras++)
    {
        int r, c;
        scanf("%d %d", &r, &c);
        vector< vector<char> > field(r, vector<char>(c));
        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                scanf(" %c", &field[i][j]);
            }
        }

        int ans=0;
        bool possible = true;
        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                char current = field[i][j];
                if(current == '.')
                {
                    continue;
                }
                bool andere_pijl_gezien = false;
                if(current == '^')
                {
                    for(int k=i-1; k>=0; k--)
                    {
                        if(field[k][j] != '.')
                        {
                            andere_pijl_gezien = true;
                            break;
                        }
                    }
                }
                if(current == '>')
                {
                    for(int k=j+1; k<c; k++)
                    {
                        if(field[i][k] != '.')
                        {
                            andere_pijl_gezien = true;
                            break;
                        }
                    }
                }
                if(current == 'v')
                {
                    for(int k=i+1; k<r; k++)
                    {
                        if(field[k][j] != '.')
                        {
                            andere_pijl_gezien = true;
                            break;
                        }
                    }
                }
                if(current == '<')
                {
                    for(int k=j-1; k>=0; k--)
                    {
                        if(field[i][k] != '.')
                        {
                            andere_pijl_gezien = true;
                            break;
                        }
                    }
                }

                if(andere_pijl_gezien)
                {
                    continue;
                }
                ans++;
                bool ergens_een_pijl = false;

                    for(int k=i-1; k>=0; k--)
                    {
                        if(field[k][j] != '.')
                        {
                            ergens_een_pijl = true;
                            break;
                        }
                    }
                    for(int k=j+1; k<c; k++)
                    {
                        if(field[i][k] != '.')
                        {
                            ergens_een_pijl = true;
                            break;
                        }
                    }
                    for(int k=i+1; k<r; k++)
                    {
                        if(field[k][j] != '.')
                        {
                            ergens_een_pijl = true;
                            break;
                        }
                    }
                    for(int k=j-1; k>=0; k--)
                    {
                        if(field[i][k] != '.')
                        {
                            ergens_een_pijl = true;
                            break;
                        }
                    }
                if(!ergens_een_pijl)
                {
                    possible = false;
                    break;
                }

            }
            if(!possible)
            {
                break;
            }
        }
        printf("Case #%d: ", kras);
        if(!possible)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("%d\n", ans);
        }
    }

    return 0;
}
