#include<string>
#include<utility>
#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int count;
    cin >> count;
    int index = 1;
    fstream f;
    f.open("d:\\output",ios::out);
    while(index <= count)
    {
        string line[4];
        bool flag = false;
        for(int i = 0; i < 4; i++)
            cin >> line[i];
        pair<int, int> pos(-1,-1);
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
            {
                if(line[i][j] == 'T')
                {
                    pos.first = i;
                    pos.second = j;
                }
            }

        for(int i = 0; i < 4; ++i)
        {
            if(line[0][i] == line[1][i] && line[0][i] == line[2][i] && line[0][i] == line[3][i] &&line[0][i] != '.')
            {
                f << "Case #" << index << ": " << line[0][i] << " won" << endl;
                flag = true;
                break;
            }
           if(!flag && line[i][0] == line[i][1] && line[i][0] == line[i][2] && line[i][3] == line[i][0] && line[i][0] != '.')
            {
                f << "Case #" << index << ": " << line[i][0] << " won" << endl;
                flag = true;
                break;
            }
        }
         if(!flag && line[0][0] == line[1][1]&& line[0][0] == line[2][2] && line[0][0] == line[3][3] && line[0][0] != '.')
        {
            f << "Case #" << index << ": " << line[0][0] << " won" << endl;
            flag = true;
        }
        if(!flag && line[0][3] == line[1][2]&& line[0][3] == line[2][1] && line[0][3] == line[3][0] && line[0][3] != '.')
        {
            f << "Case #" << index << ": " << line[0][3] << " won" << endl;
            flag = true;
        }
            //char tmp;
        if(!flag && pos.first != -1 && line[pos.first][(pos.second - 1 + 4) % 4] == line[pos.first][(pos.second - 2 + 4) % 4]
        &&line[pos.first][(pos.second - 1 + 4) % 4] == line[pos.first][(pos.second - 3 + 4) % 4]&& line[pos.first][(pos.second - 3 + 4) % 4] != '.')
        {
            //cout << line[pos.first][(pos.second - 1 + 4) % 4]  << endl;
            f << "Case #" << index << ": " << line[pos.first][(pos.second - 1 + 4) % 4] << " won" << endl;
            flag = true;
                //break;
        }
        if(!flag && pos.first != -1 && line[(pos.first - 1 + 4) % 4][pos.second] == line[(pos.first - 2 + 4) % 4][pos.second]
        &&line[(pos.first - 1 + 4) % 4][pos.second] == line[(pos.first - 3 + 4) % 4][pos.second]&& line[(pos.first -1 + 4) % 4][pos.second] != '.')
        {
            f << "Case #" << index << ": " << line[(pos.first -1 + 4) % 4][pos.second] << " won" << endl;
            flag = true;
                //break;
            }
        if(!flag && pos.first == pos.second && pos.first != -1)
        {
            if(line[(pos.first - 1 + 4) % 4][(pos.second - 1 + 4) % 4] == line[(pos.first - 2 + 4) % 4][(pos.second - 2 + 4) % 4]&&
                line[(pos.first - 1 + 4) % 4][(pos.second - 1 + 4) % 4] == line[(pos.first - 3 + 4) % 4][(pos.second - 3 + 4) % 4] && line[(pos.first - 3 + 4) % 4][(pos.second - 3 + 4) % 4] != '.')
            {
                f << "Case #" << index << ": " << line[(pos.first -1 + 4) % 4][(pos.second - 1 + 4) % 4] << " won" << endl;
                flag = true;
            }
            }
        if (!flag && pos.first + pos.second == 3)
        {
            if(line[(pos.first - 1 + 4) % 4][(pos.second + 1 + 4) % 4] == line[(pos.first - 2 + 4) % 4][(pos.second + 2 + 4) % 4]&&
                line[(pos.first - 1 + 4) % 4][(pos.second + 1 + 4) % 4] == line[(pos.first - 3 + 4) % 4][(pos.second + 3 + 4) % 4] && line[(pos.first - 3 + 4) % 4][(pos.second + 3 + 4) % 4] != '.')
            {
                f << "Case #" << index << ": " << line[(pos.first -1 + 4) % 4][(pos.second + 1 + 4) % 4] << " won" << endl;
                flag = true;
            }
        }
        if(!flag)
        {
            bool tmp = false;
            bool tmp1 = false;
            for(int i = 0; i < 4; i++)
            {
               for(int j = 0; j < 4; j++)
                {
                    if(line[i][j] == '.')
                    {
                       f << "Case #" << index << ": " << "Game has not completed" << endl;
                        tmp = true;
                        tmp1 = true;
                        break;
                    }
                }
                if(tmp1)
                    break;
            }

            if(!tmp)
                f << "Case #" << index << ": " << "Draw" << endl;
        }
        index++;
    }


    return 0;
}
