#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("a.in");
    ofstream out("a.out");

    int a;
    int b;
    int k;

    int cases;
    int currentCase = 1;
    int winCases = 0;
    if(in)
    {
        in >> cases;
        while(currentCase <= cases)
        {
            in >> a;
            in >> b;
            in >> k;

            int temp;
            for(int i=0;i<a;i++)
            {
                for(int j=0;j<b;j++)
                {
                    temp = i & j;
                    if(temp < k)
                    {
                        winCases++;
                    }
                }
            }
            out<<"Case #"<<currentCase<<": "<<winCases<<endl;
            currentCase++;
            winCases = 0;
        }
    }
}
