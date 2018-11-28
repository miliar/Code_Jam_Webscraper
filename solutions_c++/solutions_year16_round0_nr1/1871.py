#include <QFile>
#include <QTextStream>
#include <QVector>

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam2016/Qualification/A/A-large.in");
QFile outFile("C:/CodeJam2016/Qualification/A/output.txt");


int main(int argc, char *argv[])
{
    inFile.open(QFile::ReadOnly);
    outFile.open(QFile::WriteOnly);
    QTextStream inData(&inFile);
    QTextStream outData(&outFile);

    int T;
    inData >> T;
    QVector<bool> allMet(10, 1);

    for(int t=0; t<T; t++)
    {
        QVector<bool> metDigit(10, 0);
        int N, S;
        inData >> N;

        if(N==0)
        {
            outData << QString("Case #%1: %2\r\n").arg(t+1).arg("INSOMNIA");
            continue;
        }
        S = N;

        for(int i=0; i<100; i++)  //she is not going to count more than 50 numbers anyways
        {
            int D = S;
            while(D>0)
            {
                metDigit[D%10] = 1;
                D /= 10;
            }

            if(metDigit==allMet)  break;
            S += N;
        }

        outData << QString("Case #%1: %2\r\n").arg(t+1).arg(S);
    }
}
