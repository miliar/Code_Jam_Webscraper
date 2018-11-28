#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)
using namespace std;

char checkrows(char ttt[4][4])
{
    int row, col, xsc, osc;
    char cell, status='I';
    bool incom=false;

    FOR(row, 4)
    {
        xsc=0; osc=0;
        FOR(col,4)
        {
            cell=ttt[row][col];
            switch(cell)
            {
            case 'X': xsc++;
                    break;
            case 'O': osc++;
                    break;
            case 'T':   xsc++;
                        osc++;
                    break;
      //      case '.':   incom=true;
            }
        }

        if(xsc==4)
            {status='X';
            break;}
        else if(osc==4)
            {status='O';
            break;}
    }
//
//    if(status=='I' && incom==false)
//        status='D';

    return status;

}

char checkcols(char ttt[4][4])
{
    int row, col, xsc, osc;
    char cell, status='I';
    bool incom=false;

    FOR(col, 4)
    {
        xsc=0; osc=0;
        FOR(row,4)
        {
            cell=ttt[row][col];
            //cout<<cell;
            switch(cell)
            {
            case 'X': xsc++;
                    break;
            case 'O': osc++;
                    break;
            case 'T':   xsc++;
                        osc++;
                    break;
           // case '.':   incom=true;
            }
        }

        if(xsc==4)
            {status='X';
            break;}
        else if(osc==4)
            {status='O';
            break;}
    }

//    if(status=='I' && incom==false)
//        status='D';

    return status;

}

char checkdiag(char ttt[4][4])
{
    int row, col, xsc, osc;
    char cell, status='I';
    bool incom=false;
    xsc=0; osc=0;
    FOR(col, 4)
    {

            cell=ttt[col][col];
            //cout<<cell;
            switch(cell)
            {
            case 'X': xsc++;
                    break;
            case 'O': osc++;
                    break;
            case 'T':   xsc++;
                        osc++;
                    break;
           // case '.':   incom=true;
            }
        //}


    }

        if(xsc==4)
            status='X';
        else if(osc==4)
            status='O';


//    if(status=='I' && incom==false)
//        status='D';

    if(status =='X' || status=='O')
        return status;

    status='I';
    incom=false;
     xsc=0; osc=0;
       FOR(col, 4)
    {

            cell=ttt[col][3-col];
            switch(cell)
            {
            case 'X': xsc++;
                    break;
            case 'O': osc++;
                    break;
            case 'T':   xsc++;
                        osc++;
                    break;
          //  case '.':   incom=true;
            }

    }

   if(xsc==4)
            status='X';
        else if(osc==4)
            {status='O';cout<"chk";}
//
//    if(status=='I' && incom==false)
//        status='D';

    return status;

}


int main()
{
    int sm=0;
    char *filin, *filot;
    if(sm)
    {
        filin="A-small-attempt0.in";
        filot="A-small-result.txt";
    }
    else
    {
        filin="A-large.in";
        filot="A-large-result.txt";

    }

    ifstream inf;
    ofstream otp;

    inf.open(filin);
    otp.open(filot);

    char ttt[4][4];
    int row, col;
    string line;
    int test, it_test;
    getline(inf, line);
    stringstream sline(line);
    sline>>test;
    bool incomp;
    char res_row, res_col, res_diag;
    string result;

   FOR1(it_test, test)
    {
        incomp=false;
        res_row='I'; res_col='I'; res_diag='I';
        result="";


        //input phase
        FOR(row,4)
        {getline(inf, line);
        FOR(col,4)
        {
            ttt[row][col]=(char)line[col];
            if(ttt[row][col]=='.' && incomp==false)
                incomp=true;
        }
        }

        //checking phase
//        FOR(row,4)
//        {
//        FOR(col,4)
//        {
//            cout<<ttt[row][col]<<" ";
//        }
//        cout<<endl;
//        }
        res_row=checkrows(ttt);
        res_col=checkcols(ttt);
        res_diag=checkdiag(ttt);

        if(res_row=='I' && res_col=='I' && res_diag=='I')
        {
            if(incomp==false)
                result="Draw";
            else
                result="Game has not completed";
        }

        else if(res_row=='X' || res_col=='X' || res_diag=='X')
            result="X won";
        else
            result="O won";

        otp<<"Case #"<<it_test<<": "<<result<<endl;
        getline(inf, line);
    }




    return 0;
}
