#include <iostream>
#include <fstream>

using namespace std;

int simElements (int* tab1, int* tab2)
{
    int counter=0;
    for ( int i = 0 ; i < 4 ; i ++ )
        for ( int j = 0 ; j < 4 ; j ++ )
            if(tab1[i]==tab2[j])
                {
                    counter++;
                }
    return counter;
}

int simElement (int* tab1, int* tab2)
{
    int ans;
    for ( int i = 0 ; i < 4 ; i ++ )
        for ( int j = 0 ; j < 4 ; j ++ )
            if(tab1[i]==tab2[j])
                {
                    ans=tab1[i];
                }
    return ans;
}

int main()
{

    ofstream out("out.txt");
    ifstream in("in.txt");
    int tests=0;
    int disposition1[4][4];
    int line1=0;
    int possibilities1[4];
    int disposition2[4][4];
    int line2=0;
    int possibilities2[4];
    int ans;
    int a;
    in >> tests;

    for ( int i = 1 ; i <= tests ; i++ )
    {
        in >> line1;
        line1--;
        for ( int j = 0 ; j < 4 ; j++ )
            for ( int k = 0 ; k < 4 ; k++ )
            {
                in >> a;
                disposition1[j][k]=a;
            }
        for(int j = 0 ; j < 4 ; j ++)
            possibilities1[j]=disposition1[line1][j];

        in >> line2;
        line2--;
        for ( int j = 0 ; j < 4 ; j++ )
            for ( int k = 0 ; k < 4 ; k++ )
            {
                in >> a;
                disposition2[j][k]=a;
            }
        for(int j = 0 ; j < 4 ; j ++)
            possibilities2[j]=disposition2[line2][j];


        ans=simElements(possibilities1,possibilities2);
        out << "Case #" << i << ": ";
        if(ans==0)
            out << "Volunteer cheated!"<< endl;
        else if(ans==1)
            out << simElement(possibilities1,possibilities2) << endl;
        else
            out << "Bad magician!" << endl;
    }


    return 0;
}
