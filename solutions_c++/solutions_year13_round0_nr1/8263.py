#include <iostream>
#include <windows.h>

using namespace std;

int main()
{
    int t,hor,ver,mir1,mir2,dot,pass;
    char lawn[4][4], one, two, three, four;

    cin >> t;

    for(int i=0; i<t; i++)
    {
        cin >> lawn[0];
        cin >> lawn[1];
        cin >> lawn[2];
        cin >> lawn[3];

        hor=ver=0;
        for(int j=0; j<4; j++)
        {
            hor=0;
            ver=0;
            for(int k=0; k<3; k++)
            {
                if( (lawn[j][k]==lawn[j][k+1]) || lawn[j][k]=='T' || lawn[j][k+1]=='T' )
                {
                    if(lawn[j][k]!='.')
                        hor++;
                    if( lawn[j][k]!='T' && lawn[j][k]!='.' )
                        one=lawn[j][k];
                }
                if( (lawn[k][j]==lawn[k+1][j]) || lawn[k][j]=='T' || lawn[k+1][j]=='T' )
                {
                    if(lawn[k][j]!='.')
                        ver++;
                    if( lawn[k][j]!='T' && lawn[k][j]!='.' )
                        two=lawn[k][j];
                }
            }
            if( lawn[j][3]!='T' && lawn[j][3]!='.' )
                one=lawn[j][3];
            if( lawn[3][j]!='T' && lawn[3][j]!='.' )
                two=lawn[3][j];
            pass=0;
            if(hor==3)
            {
                for(int k=0; k<4; k++)
                    if(lawn[j][k]==one)
                        pass++;
                if(pass>=3)
                    break;
                else
                    hor=0;
            }
            else if(ver==3)
            {
                for(int k=0; k<4; k++)
                    if(lawn[k][j]==two)
                        pass++;
                if(pass>=3)
                    break;
                else
                    ver=0;
            }
        }
        mir1=0;
        mir2=0;
        for(int j=0; j<3; j++)
        {
            if(lawn[j][j]==lawn[j+1][j+1] || lawn[j][j]=='T' || lawn[j+1][j+1]=='T')
            {
                if(lawn[j][j]!='.')
                    mir1++;
                if( lawn[j][j]!='T' && lawn[j][j]!='.' )
                    three=lawn[j][j];
            }
            if(lawn[j][3-j]==lawn[j+1][2-j] || lawn[j][3-j]=='T' || lawn[j+1][2-j]=='T')
            {
                if(lawn[j][3-j]!='.')
                    mir2++;
                if( lawn[j][3-j]!='T' && lawn[j][3-j]!='.' )
                    four=lawn[j][3-j];
            }
        }
        if( lawn[3][3]!='T' && lawn[3][3]!='.' )
            three=lawn[3][3];
        if( lawn[3][0]!='T' && lawn[3][0]!='.' )
            four=lawn[3][0];

        pass=0;
        if(mir1==3)
        {
            for(int k=0; k<4; k++)
                if(lawn[k][k]==three)
                    pass++;
            if(pass<3)
                mir1=0;
        }
        else if(mir2==3)
        {
            for(int k=0; k<4; k++)
                if(lawn[k][3-k]==four)
                    pass++;
            if(pass<3)
                mir2=0;
        }

        dot=0;
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
            {
                if(lawn[j][k]=='.')
                    dot=1;
                lawn[j][k]='\0';
            }

        if(hor==3)
        {
            if(one=='X')
                cout << "Case #" << i+1 << ": X won" << endl;
            else if(one=='O')
                cout << "Case #" << i+1 << ": O won" << endl;
        }
        else if(ver==3)
        {
            if(two=='X')
                cout << "Case #" << i+1 << ": X won" << endl;
            else if(two=='O')
                cout << "Case #" << i+1 << ": O won" << endl;
        }
        else if(mir1==3)
        {
            if(three=='X')
                cout << "Case #" << i+1 << ": X won" << endl;
            else if(three=='O')
                cout << "Case #" << i+1 << ": O won" << endl;
        }
        else if(mir2==3)
        {
            if(four=='X')
                cout << "Case #" << i+1 << ": X won" << endl;
            else if(four=='O')
                cout << "Case #" << i+1 << ": O won" << endl;
        }
        else if(!dot)
        {
            cout << "Case #" << i+1 << ": Draw" << endl;
        }
        else
        {
            cout << "Case #" << i+1 << ": Game has not completed" << endl;
        }
        one=two=three=four='\0';
    }

    return 0;
}
