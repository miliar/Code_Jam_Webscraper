#include <QtCore>
#include <stdio.h>

QString computeCase(QTextStream &in)
{
    int X, R, C;
    in >> X;
    in >> R;
    in >> C;
    if (R > C)
    {
        int tmp = R;
        R = C;
        C = tmp;
    }
    if ((X > C) || (X >= 7) || ((R * C) % X != 0) || (((X + 1) >> 1) > R))
        return QString("RICHARD");
    switch (X)
    {
    case 4:
        if (R == 2)
            return QString("RICHARD");
        break;
    case 6:
        if (R == 3)
            return QString("RICHARD");
        break;
    }
    return QString("GABRIEL");
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
