#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream input("test.txt");
    ofstream output("output.txt");
    int T=0;
    input >> T;
    int mas[4][4];
    int masB[4][4];
    int a=0, b=0;
    int sk=0;
    int ats=0;
    for(int i=0; i<T; i++)
    {
        sk=0;
        ats=0;
        input >> a;
        a--;
        for(int y=0;y<4;y++){
            for(int z=0;z<4;z++){
                input >> mas[y][z];
            }
        }
        input >> b;
        b--;
        for(int y=0;y<4;y++){
            for(int z=0;z<4;z++){
                input >> masB[y][z];
            }
        }
        for(int y=0;y<4;y++){
            for(int z=0;z<4;z++){
                    if(mas[a][y]==masB[b][z])
                    {
                        sk++;
                        ats=masB[b][z];
                    }
            }
         }
        output << "Case #" << i+1 << ": ";
        if(sk==0) output << "Volunteer cheated!" << endl;
        else if(sk>1) output << "Bad magician!" << endl;
        else output << ats << endl;
    }
    return 0;
}
