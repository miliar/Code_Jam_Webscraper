#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <map>

using namespace std;

int main()
{
    ifstream ifs("B-large.in");
    ofstream ofs;
    ofs.open("output1.out", fstream::app | fstream::out);
    int broj_testa;
    int kraj = 0;
    string line;
    if(ifs.is_open())
    {
        getline(ifs, line);
        stringstream bab;

        broj_testa = 1;
        string buf = "";
        while(ifs.good())
        {

            //INPUT
            getline(ifs, line);
            if(line.compare("")==0){break;}
            int m, n;
            vector<string> splitLine;
            stringstream ss1(line);

            while(ss1 >> buf)
            {
                splitLine.push_back(buf);
            }
            stringstream prvi(splitLine[0]);
            prvi>>n;
            stringstream drugi(splitLine[1]);
            drugi>>m;

            int polje[n][m];
            for(int i=0; i<n;i++)
            {
                getline(ifs, line);
                vector<int> vectorInt;
                int buffer;
                stringstream ssBuf(line);
                string bufferString;
                while(ssBuf >> bufferString)
                {
                    stringstream ssBuf1;
                    ssBuf1 << bufferString;
                    ssBuf1 >> buffer;
                    vectorInt.push_back(buffer);
                }
                for(int j=0; j<m;j++)
                {
                    polje[i][j] = vectorInt[j];
                }
                vectorInt.resize(0);
            }
            int height = 0;
            //TESTING
            bool no = false;
            for(int i =0; i<n;i++)
            {
                if(no){break;}
                for(int j = 0; j<m; j++)
                {
                    int height = polje[i][j];
                    bool slobodno = true;
                    for(int k = 0; k<n; k++)
                    {
                        if(polje[k][j] > height)
                        {
                            slobodno = false;
                        }
                    }
                    if(!(slobodno))
                    {
                        for(int l = 0; l < m;l++)
                        {
                            if(polje[i][l] > height)
                            {
                                no = true;
                                break;
                            }
                        }
                    }

                    if(no){break;}
                }
                if(no){break;}
            }
            //OUTPUT
            string result = "";
            if(no)
            {
                result = "NO";
            }
            else
            {
                result = "YES";
            }
            ofs<<"Case #"<<broj_testa<<": " << result<<endl;
            broj_testa++;
        }
    }
    ifs.close();
    ofs.close();
}

