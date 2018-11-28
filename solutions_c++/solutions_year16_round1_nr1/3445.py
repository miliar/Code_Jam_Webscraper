#include <QFile>
#include <QTextStream>
#include <QVector>

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam2016/Round1/A/A-large.in");
QFile outFile("C:/CodeJam2016/Round1/A/output.txt");


int main(int argc, char *argv[])
{
    inFile.open(QFile::ReadOnly);
    outFile.open(QFile::WriteOnly);
    QTextStream inData(&inFile);
    QTextStream outData(&outFile);

    int T;
    inData >> T;
    char c;
    inData >> c; //\n
    //inData >> c; //\r

    for(int t=0; t<T; t++)
    {
        QString str, outStr;
        while(!inData.atEnd())
        {
            inData >> c;
            if((c=='\n')||(c=='\r'))
            {
                //inData >> c; //\r
                break;
            }
            str = str + c;
        }

        outStr = str[0];
        for(int i=1; i<str.length(); i++)
        {
            if(str[i] >= outStr[0]) outStr = str[i] + outStr;
            else outStr.append(str[i]);
        }

        outData << QString("Case #%1: %2\r\n").arg(t+1).arg(outStr);
    }
}
