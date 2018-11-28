#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    //freopen("A-small-attempt0.out" , "w" , stdout);
    int t;
    bool kw;
    char map[5][5];
    scanf("%d" , &t);

    for (int tt = 1; tt <= t; ++tt)
    {
        kw = false;
        printf("Case #%d: ", tt);
        getchar();
        for (int i = 0; i < 4; ++i )
        {
            for (int j = 0; j < 4 ; ++j )
            {
                while(1)
                {
                    scanf("%c", &map[i][j]);
                    if (map[i][j] =='X' || map[i][j] =='O' || map[i][j] == 'T' || map[i][j] == '.')
                    {
                        break;
                    }
                }

                if (map[i][j] == '.')
                {
                    kw = true;
                }
            }
        }


        char tmp;
        bool getit = false;
        for (int i = 0; i < 4; ++i )
        {
            getit = true;
            tmp = map[i][0];
            for (int j = 1; j < 4 ; ++j )
            {
                if (tmp != 'X' && tmp != 'O' && tmp != 'T')
                {
                    getit = false;
                    break;
                }
                if (tmp == map[i][j] || map[i][j] == 'T' || tmp == 'T')
                {
                    if (tmp == 'T')
                        tmp = map[i][j];
                    continue;
                }
                else
                {
                    getit = false;
                    break;
                }
            }
            if (getit)
            {
                if (tmp != 'T')
                {
                    cout<<tmp<<" won"<<endl;
                    break;
                }
                else
                {
                    cout<<map[i][3]<<" won"<<endl;
                    break;
                }
            }

            getit = true;
            tmp = map[0][i];
            for (int j = 1; j < 4 ; ++j )
            {
                if (tmp != 'X' && tmp != 'O' && tmp != 'T')
                {
                    getit = false;
                    break;
                }
                if (tmp == map[j][i] || map[j][i] == 'T' || tmp == 'T')
                {
                    if (tmp == 'T')
                        tmp = map[j][i];
                    continue;
                }
                else
                {
                    getit = false;
                    break;
                }
            }
            if (getit)
            {
                if (tmp != 'T')
                {
                    cout<<tmp<<" won"<<endl;
                    break;
                }
                else
                {
                    cout<<map[3][i]<<" won"<<endl;
                    break;
                }
            }



        }


        if (getit == false)
        {
            getit = true;
            char tmp = map[0][0];
            for (int i = 1; i < 4; ++i )
            {
                if (tmp != 'X' && tmp != 'O' && tmp != 'T')
                {
                    getit = false;
                    break;
                }
                if (tmp == map[i][i] || map[i][i] == 'T' || tmp == 'T')
                {
                    if (tmp == 'T')
                       tmp = map[i][i];
                    continue;
                }
                else
                {
                    getit = false;
                    break;
                }

            }
            if (getit)
            {
                if (tmp != 'T')
                {
                    cout<<tmp<<" won"<<endl;

                }
                else
                {
                    cout<<map[3][3]<<" won"<<endl;
                }
            }
        }

        if (getit == false)
        {
            getit = true;
            char tmp = map[0][3];
            for (int i = 1; i < 4; ++i )
            {
                if (tmp != 'X' && tmp != 'O' && tmp != 'T')
                {
                    getit = false;
                    break;
                }
                if (tmp == map[i][3-i] || map[i][3-i] == 'T' || tmp == 'T')
                {
                    if (tmp == 'T')
                        tmp = map[i][3-1];
                    continue;
                }
                else
                {
                    getit = false;
                    break;
                }

            }
            if (getit)
            {
                if (tmp != 'T')
                {
                    cout<<tmp<<" won"<<endl;

                }
                else
                {
                    cout<<map[0][3]<<" won"<<endl;

                }
            }

        }

        if (getit == false && kw == true)
        {
            cout<<"Game has not completed"<<endl;
        }
        else if (getit == false)
        {
            cout<<"Draw"<<endl;
        }




    }

	return 0;
}
