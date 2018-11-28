#include <iostream>
#include <string>
#include <algorithm>
#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <fstream>

using namespace std;

int main()
{

    ofstream fout ("C.out");
    ifstream fin ("C-small-attempt0.in");

    int number;

    fin >> number;

    int ranges[2];
    int now;
    int points=0;
    int square;
    double check;
    float jiwei;
    int weishu;
    bool pal=true;
    bool pals=true;

    for(int i=1;i<=number;i++)
    {
        for(int j=0;j<2;j++)
        {
            fin >> ranges[j];
        }
        for(int j=ranges[0];j<=ranges[1];j++)
        {
            pal=true;
            pals=true;
            now = j;
            jiwei = now;

            for(int k=1;;k++)
            {
                jiwei = jiwei/10;

                if(jiwei<1)
                {
                    weishu=k;
                    break;
                }
            }
            if(weishu>1)
            {
                for(int k=weishu/2;k<=1;k++)
                {
                    int nnow=now;
                    int a=nnow/pow(10,weishu-1);
                    int b=nnow%10;
                    if(a==b)
                    {
                        nnow-=(nnow%10)*(pow(10,weishu-1));
                        nnow=nnow/10;
                    }
                    else
                    {
                        pal=false;
                        break;
                    }

                }
            }

            if(pal)
            {
                square = sqrt(now);
                check = (double)now / (double)square;
                if(check==square)
                {
                    jiwei = square;

                    for(int k=1;;k++)
                    {
                        jiwei = jiwei/10;

                        if(jiwei<1)
                        {
                            weishu=k;
                            break;
                        }
                    }
                    if(weishu>1)
                    {
                        for(int k=weishu/2;k<=1;k++)
                        {
                            int nnow=square;
                            int a=nnow/pow(10,weishu-1);
                            int b=nnow%10;
                            if(a==b)
                            {
                                nnow-=(nnow%10)*(pow(10,weishu-1));
                                nnow=nnow/10;
                            }
                            else
                            {
                                pals=false;
                                break;
                            }

                        }
                    }
                }
                else
                    pals=false;

                if(pals)
                    points++;

            }

        }
        fout << "Case #" << i << ": " << points << endl;
        points = 0;

    }


    return 0;

}
