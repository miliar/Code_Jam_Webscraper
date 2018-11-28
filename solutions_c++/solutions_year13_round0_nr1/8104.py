#include <iostream>

using namespace std;
bool verificavencedor(string s, int &cont,int z);

int main()
{
    int t,z=0,cont=0;
    bool b;
    string s="";
    char mat[4][4];
    cin >> t;
    while(z<t)
    {

        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                cin >> mat[i][j];
            }
        }




        cont=0;
        for(int i=0; i<4; i++)
        {
            s="";
            for(int j=0; j<4; j++)
            {
                s+=mat[i][j];
            }
            if(verificavencedor(s,cont,z)) break;
            else if(i==3)
            {
                for(int i=0; i<4; i++)
                {
                    s="";
                    for(int j=0; j<4; j++)
                    {
                        s+=mat[j][i];
                    }
                    if(verificavencedor(s,cont,z)) break;
                    else if (cont>=4)
                    {
                        s="";
                        s+=mat[0][0];
                        s+=mat[1][1];
                        s+=mat[2][2];
                        s+=mat[3][3];
                        if(verificavencedor(s,cont,z)) break;
                        s="";
                        s+=mat[0][3];
                        s+=mat[1][2];
                        s+=mat[2][1];
                        s+=mat[3][0];
                        if(verificavencedor(s,cont,z)) break;

                        cout << "Case #" << z+1 << ": Game has not completed\n";
                        break;
                    }
                    else if(cont<4)
                    {
                        s="";
                        s+=mat[0][0];
                        s+=mat[1][1];
                        s+=mat[2][2];
                        s+=mat[3][3];
                        if(verificavencedor(s,cont,z)) break;
                        s="";
                        s+=mat[0][3];
                        s+=mat[1][2];
                        s+=mat[2][1];
                        s+=mat[3][0];
                        if(verificavencedor(s,cont,z)) break;

                        cout << "Case #" << z+1 << ": Draw\n";
                        break;
                    }

                }




            }
        }
        z++;
        cin.ignore();
    }
    return 0;
}

bool verificavencedor(string s, int &cont,int z)
{

    if(s=="XXXT" || s=="TXXX" || s=="XXXX")
    {
        cout << "Case #" << z+1 << ": X won\n";
        return true;
    }
    else if (s=="OOOT" || s=="TOOO" || s=="OOOO")
    {
        cout << "Case #" << z+1 << ": O won\n";
        return true;
    }
    else if(s.find('.')!=-1)
    {
        cont++;
        return false;
    }
    else return false;


}
