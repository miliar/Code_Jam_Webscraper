#include <QtCore>
#include <stdio.h>

QString computeCase(QTextStream &in)
{
    int Smax, current = 0, needed = 0;
    in >> Smax;
    QString audience;
    in >> audience;
    if (audience.length() != Smax + 1)
    {
        fprintf(stderr, "BUG(%s)\n", qPrintable(audience));
        return "";
    }
    for (int i = 0; i < audience.length(); ++i)
    {
        int turn = i - current;
        if (turn > 0)
        {
            needed += turn;
            current += turn;
        }
        current += QString(audience.at(i)).toInt();
    }
    return QString::number(needed);
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    if (argc < 2)
    {
        fprintf(stderr, "Error: Missing argument.\n");
        return 1;
    }
    QFile inputFile(argv[1]);
    if (!inputFile.open(QIODevice::ReadOnly))
    {
        fprintf(stderr, "Error: Could not open input file.\n");
        return 1;
    }
    QFile outputFile(QString(argv[1]) + ".out");
    if (!outputFile.open(QIODevice::WriteOnly))
    {
        fprintf(stderr, "Error: Could not open output file.\n");
        inputFile.close();
        return 1;
    }
    int T, i = 0;
    QTextStream input(&inputFile);
    input >> T;
    while (++i <= T)
    {
        QString result = computeCase(input);
        outputFile.write(QString("Case #%1: %2\n").arg(i).arg(result).toUtf8());
    }
    outputFile.close();
    inputFile.close();
    printf("Done.\n");
    return 0;
}
