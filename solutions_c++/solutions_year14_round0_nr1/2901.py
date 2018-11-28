#ifndef UTILE_H
#define UTILE_H

#include <QObject>

#include <QFile>

class Utile : public QObject
{
    Q_OBJECT
public:
    explicit Utile(QObject *parent = 0);


    QList<QStringList> getValuesFromFile(QString fileName);
    bool saveLslValuesToFile(QString fileName, QList<QStringList>listValues);
    bool saveSlValuesToFile(QString fileName, QStringList listValues);
    void setSeparateur(int);

    void writeRslt(QStringList sl);

signals:
    
public slots:
    
private :
    QString m_separateur;


};

#endif // UTILE_H
