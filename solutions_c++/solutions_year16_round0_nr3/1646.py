#include <QFile>
#include <QTextStream>
#include <QVector>

//Artem Klimov's solution
//soved using Qt Framework

QFile inFile("C:/CodeJam2016/Qualification/C/C-large.in");
QFile outFile("C:/CodeJam2016/Qualification/C/output.txt");

void FindAndPrintAllValidA(QVector<bool> &A, int &numberOfAlreadyPrinted, int numberNeedToPrint, QTextStream &outData, int startIndex)
{
    for(int i=startIndex; i<(A.count()-1); i++)
    {
        if(numberOfAlreadyPrinted>=numberNeedToPrint) return;
        if( (A[i-1]==0) && (A[i]==0) && (A[i+1]==0) )   //let's see if we can put 1 at i place
        {
            //outData << QString("Solution %1: ").arg(numberOfAlreadyPrinted);
            A[i] = 1;
            //now we have one more valid combination, let's output A*11
            outData << "1";
            for(int j=0; j<(A.count()-1); j++)  outData << QString("%1").arg( (int) (A[j]||A[j+1]) );
            outData << "1 ";

            outData << "3 4 5 6 7 8 9 10 11\r\n";  //dividers

            numberOfAlreadyPrinted++;
            FindAndPrintAllValidA(A, numberOfAlreadyPrinted, numberNeedToPrint, outData, i+1);
            A[i] = 0; //return to what it was!
        }
    }
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
        int N, J;
        inData >> N;
        inData >> J;

        QVector<bool> A(N-1, 0);   //A*11 will give us the number
        A[0] = 1;
        A[N-2] = 1;

        outData << QString("Case #%1:\r\n").arg(t+1);
        int numberOfAlreadyPrinted = 0;
        FindAndPrintAllValidA(A, numberOfAlreadyPrinted, J, outData, 1);
    }
}
