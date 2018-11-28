#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
int match (vector<int> list , int a1 , int a2)
{
    int out=0 , countr = 0;
    for (int i=0; i<4 ; i++)
    {
        for(int j=0 ; j<4 ;j++)
        {
            if( list[a1+i] == list[a2+j])
            {
                out = a1+i;
                countr++;
            }
        }
    }
    if(countr > 1)
    {
        return -1; // bad magician
    }
    else if(countr == 1)
    {
        return out;
    }
    else
    {
        return -2; // cheating
    }
}
int main () {

    vector<int> list;
    ifstream in_stream;
    ofstream out_stream;
    string line;
    int j=1;
    int first , second , row1 , row2;
    in_stream.open("input.in");
    out_stream.open("output.in");

    while( in_stream >> line)
    {
        list.push_back(atoi(line.c_str()));
    }

    in_stream.close();

    for (int i=0 ; i < list[0] ; i++)
    {
        first = j;
        row1 = first + 4*(list[first] - 1) + 1;

        second = first + 4*4 + 1;
        row2 = second + 4 * ( list[second] -1 ) + 1;

        int x = match(list , row1 , row2);

        switch(x)
        {
            case -2:
                out_stream << "Case #"<<(i+1)<<": "<<"Volunteer cheated!\n";
            break;
            case -1:
                out_stream << "Case #"<<(i+1)<<": "<<"Bad magician!\n";
            break;
            default:
                out_stream << "Case #"<<(i+1)<<": "<<list[x]<<"\n";
            break;
        }

        j = second + 4*4 + 1;

    }

return 0;
}
