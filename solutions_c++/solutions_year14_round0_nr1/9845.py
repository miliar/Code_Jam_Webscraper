
#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in_stream;
    ofstream out_stream;

    in_stream.open("A-small-attempt1.in");
    out_stream.open("outfile.dat");

    int  noOfTestCase, rowIndex;
    int  Row[4][4];
    int n=0;
    in_stream>>noOfTestCase;
    do{
        int  key[4], temp[4],keyCount[4];
        for( int i =0; i<4; i++)
            keyCount[i]=0;
        in_stream>>rowIndex;
        for( int i = 0; i < 4; i++)
        {
            for( int j = 0; j<4; j++)
            {
                in_stream>>Row[i][j];
            }
        }

        for( int i = 0; i <4; i++)
        {
            key[i]=Row[rowIndex-1][i];
        }

        in_stream>>rowIndex;
        for( int i = 0; i < 4; i++)
        {
            for( int j = 0; j<4; j++)
            {
                in_stream>>Row[i][j];
            }
        }
        for( int i = 0; i <4; i++)
        {
            temp[i]=Row[rowIndex-1][i];
        }

        for( int i = 0; i < 4; i++)
        {
            for( int j = 0; j < 4; j++)
            {
                if(temp[i]== key[j])
                    keyCount[j]++;
            }
        }
        int count = 0, index = -1;
        for( int i = 0; i < 4; i++)
        {
            if(keyCount[i]==1)
            {
                count++;
                index = i;
            }
        }
        n++;
        if(count == 1)
            out_stream<<"Case #"<<n<<": "<<key[index]<<endl;
        if(count > 1)
            out_stream<<"Case #"<<n<<": Bad magician!"<<endl;
        if (count == 0 )
            out_stream<<"Case #"<<n<<": Volunteer cheated!"<<endl;
        noOfTestCase--;
    }while(noOfTestCase >0);
    in_stream.close();
    out_stream.close();
    return 0;
}
