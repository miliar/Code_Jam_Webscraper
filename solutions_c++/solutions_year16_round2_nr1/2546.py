#include <QFile>
#include <QTextStream>
#include <QVector>

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam2016/Round1B/A/A-large.in");
QFile outFile("C:/CodeJam2016/Round1B/A/output.txt");

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
        QString str;
        inData >> str;
        QList<int> list;

        while(str.contains('Z'))
        {
            list.append(0);
            str.remove( str.indexOf('Z'),1 );  str.remove( str.indexOf('E'),1 );  str.remove( str.indexOf('R'),1 );  str.remove( str.indexOf('O'),1 );
        }

        while(str.contains('W'))
        {
            list.append(2);
            str.remove( str.indexOf('T'),1 );  str.remove( str.indexOf('W'),1 );  str.remove( str.indexOf('O'),1 );
        }

        while(str.contains('U'))
        {
            list.append(4);
            str.remove( str.indexOf('F'),1 );  str.remove( str.indexOf('O'),1 );  str.remove( str.indexOf('U'),1 );  str.remove( str.indexOf('R'),1 );
        }

        while(str.contains('X'))
        {
            list.append(6);
            str.remove( str.indexOf('S'),1 );  str.remove( str.indexOf('I'),1 );  str.remove( str.indexOf('X'),1 );
        }

        while(str.contains('G'))
        {
            list.append(8);
            str.remove( str.indexOf('E'),1 );  str.remove( str.indexOf('I'),1 );  str.remove( str.indexOf('G'),1 ); str.remove( str.indexOf('H'),1 ); str.remove( str.indexOf('T'),1 );
        }

        while(str.contains('O'))
        {
            list.append(1);
            str.remove( str.indexOf('O'),1 );  str.remove( str.indexOf('N'),1 );  str.remove( str.indexOf('E'),1 );
        }

        while(str.contains('T'))
        {
            list.append(3);
            str.remove( str.indexOf('T'),1 );  str.remove( str.indexOf('H'),1 );  str.remove( str.indexOf('R'),1 ); str.remove( str.indexOf('E'),1 ); str.remove( str.indexOf('E'),1 );
        }

        while(str.contains('F'))
        {
            list.append(5);
            str.remove( str.indexOf('F'),1 );  str.remove( str.indexOf('I'),1 );  str.remove( str.indexOf('V'),1 ); str.remove( str.indexOf('E'),1 );
        }

        while(str.contains('S'))
        {
            list.append(7);
            str.remove( str.indexOf('S'),1 );  str.remove( str.indexOf('E'),1 );  str.remove( str.indexOf('V'),1 ); str.remove( str.indexOf('E'),1 ); str.remove( str.indexOf('N'),1 );
        }

        while(str.contains('N'))
        {
            list.append(9);
            str.remove( str.indexOf('N'),1 );  str.remove( str.indexOf('I'),1 );  str.remove( str.indexOf('N'),1 ); str.remove( str.indexOf('E'),1 );
        }

        qSort(list.begin(), list.end());

        outData << QString("Case #%1: ").arg(t+1);
        for(int i=0; i<list.count(); i++)  outData << QString("%1").arg(list[i]);
        outData << "\r\n";
    }
}
