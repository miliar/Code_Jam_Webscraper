#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    fstream f1, f2;
    f1.open("B-large.in", ios::in);
    f2.open("output.txt", ios::out | ios::binary);
    int iter;
    f1>>iter;
    f1.get();
    for (int x=0; x<iter; x++)
    {
        int l=0, b=0;
        f1>>l;
        f1.get();
        f1>>b;
        f1.get();
        int m[l][b];

        string s = "Case #";
        if (x<9)
            s+=(x+49);
        else if (x<99)
        {
            int z = x, y;
            z = x+1;
            y = z%10;
            z = z/10;
            s+=(z+48);
            s+=(y+48);
        }
        else
            s+="100";

        for (int i=0; i<l; i++)
        {
            for (int j=0; j<b; j++)
            {
                f1>>m[i][j];
                f1.get();
            }
        }

        int dup[l][b];

        for (int i=0; i<l; i++)
        {
            for (int j=0; j<b; j++)
            {
                dup[i][j] = 9999;
            }
        }

        int c=0;
        for (int i=0; i<l; i++)
        {
            for (int j=0; j<b; j++)
            {
                if (m[i][j]!=dup[i][j])
                {
                    c=0;
                    for (int x=0; x<b; x++)
                    {
                        if (m[i][j]>=m[i][x])
                            c++;
                    }
                    if (c==b)
                    {
                        for (int y=0; y<b; y++)
                        {
                            if (m[i][y]>=m[i][j])
                                dup[i][y] = m[i][j];
                        }
                    }

                    c=0;
                    for (int x=0; x<l; x++)
                    {
                        if (m[i][j]>=m[x][j])
                            c++;
                    }
                    if (c==l)
                    {
                        for (int y=0; y<l; y++)
                        {
                            if (m[y][j]>=m[i][j])
                                dup[y][j] = m[i][j];
                        }
                    }
                }
            }
        }

        c=0;

        for (int i=0; i<l; i++)
        {
            for (int j=0; j<b; j++)
            {
                if (m[i][j]!=dup[i][j])
                    c++;
            }
        }
        if (c==0)
            s+=": YES";
        else
            s+=": NO";
        f2<<s;
        f2<<endl;
    }
    f1.close();
    f2.close();
    return 0;
}
