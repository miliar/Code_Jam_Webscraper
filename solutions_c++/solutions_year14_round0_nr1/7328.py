#include <iostream>
#include <fstream>

using namespace std;

int  case1[4]={0}, case2[4]={0};

ifstream f1 ("1.in");
ofstream f2 ("1.out");

void compare(int &match, int &noMatches)
{
    match=0;
    noMatches=0;
    for(int i=0; i<=3; i++)
        for(int j=0; j<=3; j++)
        {
            if(case1[i]==case2[j])
            {
                match=case2[j];
                case2[j]=NULL;
                noMatches++;
            }
        }
}

int main()
{
    int noOfTests, line, garbage, noMatches, match;
    f1 >> noOfTests;

    for(int i=1; i<=noOfTests; i++)
    {
        f1>>line;
        for(int j=1; j<=16; j++)
        {
            if(j>(line-1)*4&&j<=line*4)
                f1>>case1[j%4];
            else

            f1>>garbage;
        }
        f1>>line;
        for(int j=1; j<=16; j++)
        {
            if(j>(line-1)*4&&j<=line*4)
                f1>>case2[j%4];
            else

            f1>>garbage;
        }

        compare(match, noMatches);

        f2<<"Case #"<<i<<": ";

        if(noMatches==0)
            f2<<"Volunteer cheated!";
        else if (noMatches==1)
            f2<<match;
        else f2<<"Bad magician!";
        f2<<"\n";


    }


    //cout << "Hello world!" << endl;
    return 0;
}
