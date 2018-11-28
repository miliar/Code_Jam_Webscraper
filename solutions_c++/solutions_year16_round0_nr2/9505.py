#ifndef PROBELMB_H
#define PROBELMB_H

#include <QObject>
#include <QFile>
#include <QTextStream>

class ProbelmB : public QObject
{
    Q_OBJECT
public:
    explicit ProbelmB(QString url, QString filein, QString fileout, QObject *parent = 0);
    QString CalculateB();

signals:

public slots:

private:
    QFile* fileIn;
    QFile* fileOut;

};

#endif // PROBELMB_H
