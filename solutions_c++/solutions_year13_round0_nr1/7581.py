#include <iostream>
#include <fstream>

using namespace std;

bool won(char m[4][4], char a);
bool find_dot(char m[4][4]);

ifstream in("A-large.in");

int main()
{
    ofstream out("A_answ.txt");
    int t;
    in>>t;
    for(int q=1;q<=t;q++)
    {
        char m[4][4];
        for(int i=0;i<4;i++)
        {
            for(int w=0;w<4;w++)
            {
                in>>m[i][w];
            }
        }
        if(won(m,'X'))
        {
            out<<"Case #"<<q<<": X won"<<endl;
        }
        else
        if(won(m,'O'))
        {
            out<<"Case #"<<q<<": O won"<<endl;
        }
        else
        if(find_dot(m))
        {
            out<<"Case #"<<q<<": Game has not completed"<<endl;
        }
        else
        {
            out<<"Case #"<<q<<": Draw"<<endl;
        }
    }
    return 0;
}

bool won(char m[4][4], char a)
{
    for(int i=0;i<4;i++)
    {   int c=0;
        for(int q=0;q<4;q++)
        {
            if(m[i][q]==a||m[i][q]=='T')
            {
                c++;
            }
        }
        if(c==4)
        {
            return true;
        }
        else
        {
            c=0;
        }
    }
    //------------
    for(int i=0;i<4;i++)
    {   int c=0;
        for(int q=0;q<4;q++)
        {
            if(m[q][i]==a||m[q][i]=='T')
            {
                c++;
            }
        }
        if(c==4)
        {
            return true;
        }
        else
        {
            c=0;
        }
    }
    //----------
        int c=0;
        for(int q=0;q<4;q++)
        {
            if(m[q][q]==a||m[q][q]=='T')
            {
                c++;
            }
        }
        if(c==4)
        {
            return true;
        }
        else
        {
            c=0;
        }
        //---------
        //0000000
        /*int s=3;
        for(int q=0;q<4;q++)
        {
            cout<<m[q][q+s]<<" ";
            //cout<<q<<" "<<s<<" "<<q+s<<"   ";
            s=s-2;
        }
        cout<<endl;*/
        //00000000
    //-------------------
        c=0;
        int s=3;
        for(int q=0;q<4;q++)
        {
            if(m[q][q+s]==a||m[q][q+s]=='T')
            {
                c++;
            }
            s=s-2;
        }
        if(c==4)
        {
            return true;
        }
        else
        {
            c=0;
        }
        //--------------
    return false;
}

bool find_dot(char m[4][4])
{
    for(int i=0;i<4;i++)
    {
        for(int k=0;k<4;k++)
        {
            if(m[i][k]=='.')
            {
                return true;
            }
        }
    }
    return false;
}
