#include "filereader.h"

FileReader::FileReader()
{
}

QList<QString> FileReader::ReadFile(QString fileName)
{
    QList<QString> lstString;
    QFile file(fileName);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return lstString;

    QTextStream in(&file);
    while (!in.atEnd()) {
        lstString.append(in.readLine());
    }
    return lstString;
}
