#include <QCoreApplication>
#include <QFile>
#include <QStringList>
#include <QTextStream>
#include <QDebug>
#include <QtGlobal>
#include <QDateTime>
#include <QList>
#include <QMap>
#include <QPair>

bool is_debug = false;

QMap<int, int> F;
QList<int> Fl;
int FL;
int FF;
int getNext(int c) {
    if (is_debug) qDebug() << "getNext" << c << FL << Fl;
        ++FL;
        Fl.append(c);

    int nc = F[c];
    if (Fl.indexOf(nc) == -1) {
        getNext(nc);
    } else if (F[nc] == FF) {
        ++FL;
    } else {
        --FL;
    }
 //Fl.append();
}

QString getAnswer(QString s) {
    if (is_debug) {
        qDebug() << "start getAnswer" << s;
    }

    QMap<QChar, int> cm;
    QChar c;
    for(int i = 0; i < s.length(); ++i) {
        c = s.at(i);
        if (cm.contains(c)) {
            ++cm[c];
        } else {
            cm[c] = 1;
        }
    }

    QMap<int, int> nm;

    for(int i = 0; i < 10; ++i) {
        nm[i] = 0;
    }

    while(cm['Z'] > 0) {
        --cm['Z'];
        --cm['E'];
        --cm['R'];
        --cm['O'];
        ++nm[0];
    }

    while(cm['W'] > 0) {
        --cm['T'];
        --cm['W'];
        --cm['O'];
        ++nm[2];
    }

    while(cm['U'] > 0) {
        --cm['F'];
        --cm['O'];
        --cm['U'];
        --cm['R'];
        ++nm[4];
    }

    while(cm['X'] > 0) {
        --cm['S'];
        --cm['I'];
        --cm['X'];
        ++nm[6];
    }

    while(cm['G'] > 0) {
        --cm['E'];
        --cm['I'];
        --cm['G'];
        --cm['H'];
        --cm['T'];
        ++nm[8];
    }

    while(cm['O'] > 0) {
        --cm['O'];
        --cm['N'];
        --cm['E'];
        ++nm[1];
    }

    while(cm['T'] > 0) {
        --cm['T'];
        --cm['H'];
        --cm['R'];
        --cm['E'];
        --cm['E'];
        ++nm[3];
    }

    while(cm['F'] > 0) {
        --cm['F'];
        --cm['I'];
        --cm['V'];
        --cm['E'];
        ++nm[5];
    }

    while(cm['S'] > 0) {
        --cm['S'];
        --cm['E'];
        --cm['V'];
        --cm['E'];
        --cm['N'];
        ++nm[7];
    }

    while(cm['I'] > 0) {
        --cm['N'];
        --cm['I'];
        --cm['N'];
        --cm['E'];
        ++nm[9];
    }

    QString res;
    for(int i = 0; i < 10; ++i) {
        while(nm[i] > 0) {
            res.append(QString::number(i));
            --nm[i];
        }
    }

    return res;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QStringList params = QCoreApplication::arguments();
    if (params.count() < 3) {
        return 1;
    }

    qDebug() << params;
    qDebug() << params.at(1);
    QFile file_in(params.at(1));
    if (!file_in.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return 2;
    }

    QTextStream in(&file_in);

    QFile file_out(params.at(2));
    if (!file_out.open(QIODevice::WriteOnly)) {
        return 3;
    }

    is_debug = true;//params.count() > 3 && params.at(3).compare("debug") == 0;

    QTextStream out(&file_out);
    QString line;
    int Idx = -1;
    int CaseNum = 0;
    QString answer;

    QDateTime start;
    QDateTime finish;
    QStringList sl;
    int line_type = 0;
    int N = 0;
    int LnCnt = 0;
    int i;

    while (!in.atEnd()) {
        line = in.readLine();
        if (++Idx == 0) {
            if (is_debug) qDebug() << "Input case count " << line;
            continue;
        }
        if (is_debug) {
            qDebug() << "Current index " << Idx << N << line_type << LnCnt << line;
        }
        start = QDateTime::currentDateTime();

            answer = "Case #" + QString::number(++CaseNum) + ": " + getAnswer(line);
            out << answer;
            endl(out);

        finish = QDateTime::currentDateTime();
        if (is_debug) {
            //qDebug() << "LineProcessed" << finish.toTime_t() - start.toTime_t();
        }

    }//*/
    return 0;
    //return a.exec();
}
