#include <QFile>
#include <QTextStream>
#include <QSet>

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam/Qualification/D/D-small-attempt3.in");
QFile outFile("C:/CodeJam/Qualification/D/output.txt");


bool RichardWins(int X, int R, int C)
{
    if( X>qMax(R,C) ) return 1;
    if( (X/2)>qMin(R,C) ) return 1;  //square
    if( (R*C)%X )  return 1;
    if( X>6 )  return 1;

    //some table values
    if((X>=3) && ((R==1)||(C==1))) return 1;
    if((X>=4) && ((R==2)||(C==2))) return 1;

    return 0;
}

int main(int argc, char *argv[])
{
    inFile.open(QFile::ReadOnly);
    outFile.open(QFile::WriteOnly);
    QTextStream inData(&inFile);
    QTextStream outData(&outFile);

    int T;
    inData >> T;

    for(int t=0; t<T; t++)
    {
        int X,R,C;
        inData >> X;
        inData >> R;
        inData >> C;

        if(RichardWins(X,R,C))  outData << QString("Case #%1: RICHARD\r\n").arg(t+1);
        else                    outData << QString("Case #%1: GABRIEL\r\n").arg(t+1);
    }
}



