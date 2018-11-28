#include<iostream>
#include<string>
using namespace std;
int array[4][4];
int check_array()
{
    //check rows:

    for(int i=0;i<4;i++)
    {
        bool statusX=true;
        bool statusO=true;
        for(int j=0;j<4;j++)
        {
            if(array[i][j]!=1&&array[i][j]!=3)
                statusX =false;
            if(array[i][j]!=2&&array[i][j]!=3)
                statusO =false;
        }
        if(statusX)
            return 1;
        if(statusO)
            return 2;
    }

    //Check Columns:

    for(int i=0;i<4;i++)
    {
        bool statusX=true;
        bool statusO=true;
        for(int j=0;j<4;j++)
        {
            if(array[j][i]!=1&&array[i][j]!=3)
                statusX =false;
            if(array[j][i]!=2&&array[i][j]!=3)
                statusO =false;
        }
        if(statusX)
            return 1;
        if(statusO)
            return 2;
    }

    //Checking diagonal -part 1

    bool statusX=true;
    bool statusO=true;
    for(int i=0;i<4;i++)
    {
        if(array[i][i]!=1&&array[i][i]!=3)
            statusX=false;
        if(array[i][i]!=2&&array[i][i]!=3)
            statusO=false;
    }
    if(statusX)
        return 1;
    if(statusO)
        return 2;

    //Checking diagonal -part 2

    statusX=true;
    statusO=true;
    for(int i=0;i<4;i++)
    {
        if(array[i][3-1]!=1&&array[i][3-i]!=3)
            statusX=false;
        if(array[i][3-i]!=2&&array[i][3-i]!=3)
            statusO=false;
    }
    if(statusX)
        return 1;
    if(statusO)
        return 2;



    //Checking for a draw game:

    bool statusDr=true;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(array[i][j]==0)
                statusDr=false;
        }
    }
    if(statusDr)
        return 3;

    return 4;

}
int main()
{
    int total,case_id;
    string input;
    case_id=1;
    cin>>total;
    char bl;
    while(case_id<=total)
    {
        //Reading the array
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>bl;
                if(bl=='X')
                {
                    array[i][j]=1;
                }
                if(bl=='O')
                {
                    array[i][j]=2;
                }
                if(bl=='T')
                {
                    array[i][j]=3;
                }
                if(bl=='.')
                {
                    array[i][j]=0;
                }

            }
        }
        //Display

        int result=check_array();
        cout<<"Case #"<<case_id<<": ";
        if(result==1)
            cout<<"X won";
        if(result==2)
            cout<<"O won";
        if(result==3)
            cout<<"Draw";
        if(result==4)
            cout<<"Game has not completed";
        cout<<"\n";
        case_id++;
    }
}











