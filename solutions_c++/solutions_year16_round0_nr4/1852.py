#include <QFile>
#include <QTextStream>
#include <QVector>

//Artem Klimov's solution
//soved using Qt Framework

QFile inFile("C:/CodeJam2016/Qualification/D/D-small-attempt0.in");
QFile outFile("C:/CodeJam2016/Qualification/D/output.txt");


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
        int K, C, S;
        inData >> K;
        inData >> C;
        inData >> S;

        outData << QString("Case #%1: ").arg(t+1);
        if( (C==1) || (K==1) )
        {
            if(S<K)  outData << "IMPOSSIBLE";
            else
                for(int i=1; i<=K; i++)  outData << QString("%1 ").arg(i);  //open all
        }
        else
        {
            if(S<(K-1))  outData << "IMPOSSIBLE";
            else
                for(int i=2; i<=K; i++)  outData << QString("%1 ").arg(i);  //open all except 1st
        }

        outData << "\r\n";
    }
}
