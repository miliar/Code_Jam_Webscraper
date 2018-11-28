#include <iostream>
#include <fstream>
std::ifstream cin("a.in");
std::ofstream cout("ulos.txt");
using std::endl;
int main()
{
    int N;
    cin>>N;
    for(int i=0;i<N;i++)
    {
        char lauta[4][4];
        for(int a=0;a<4;a++)
        {
            std::string s;
            cin>>s;
            for(int e=0; e<4;e++)
            {
                lauta[a][e]=s[e];
            }
        }
        char asd=lauta[0][0];
        bool oliko=true;
        if(asd!='.')
        {
            for(int i=1;i<4;i++)
            {
                if(lauta[i][i]!=asd&&lauta[i][i]!='T')
                {
                    oliko=false;
                }
            }
        }else{
            oliko=false;
        }

        if(oliko)
        {
            cout << "Case #" << i+1<< ": " << asd << " won"<<endl;
            continue;
        }
        if(!oliko)
        {
            char asd=lauta[3][0];
            bool oliko=true;
            if(asd!='.')
            {
                for(int i=1;i<4;i++)
                {
                    if(lauta[3-i][i]!=asd&&lauta[3-i][i]!='T')
                    {
                        oliko=false;
                    }
                }
            }else{
                oliko=false;
            }

            if(oliko)
            {
                cout << "Case #" << i+1<< ": " << asd << " won"<<endl;
                continue;
            }
        }
        if(!oliko)
        {
            for(int e=0;e<4;e++)
            {
                char asd=lauta[e][0];
                oliko=true;
                if(asd!='.')
                {
                    for(int a =1;a<4;a++)
                    {
                        if(lauta[e][a]!=asd&&lauta[e][a]!='T')
                            oliko=false;

                    }
                }else{
                    oliko=false;
                }
                if(oliko)
                {
                    cout << "Case #" << i+1<< ": " << asd << " won"<<endl;
                    break;
                }

                asd=lauta[0][e];
                oliko=true;
                if(asd!='.')
                {
                    for(int a =1;a<4;a++)
                    {
                        if(lauta[a][e]!=asd&&lauta[a][e]!='T')
                            oliko=false;

                    }
                }else{
                    oliko=false;
                }
                if(oliko)
                {
                    cout << "Case #" << i+1<< ": " << asd << " won"<<endl;
                    break;
                }
            }
        }
        if(!oliko)
        {
            for(int a=0;a<4;a++)
                for(int e =0; e<4;e++)
                    if(lauta[a][e]=='.')
                        oliko=true;
            if(oliko)
            {
                cout << "Case #" << i+1<< ": " <<"Game has not completed"<<endl;
            }else{
                cout << "Case #" << i+1<< ": " <<"Draw"<<endl;
            }
        }


    }
    return 0;
}
