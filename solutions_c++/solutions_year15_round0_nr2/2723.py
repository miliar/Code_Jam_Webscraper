#include <QVector>
#include <QMap>
#include <QTextStream>

void tryToFit(int curFit, int& specsUsed, int cntPan, int cntEat)
{
    if (curFit >= cntPan)
        return;

    specsUsed += (((cntPan + (curFit - 1)) / curFit) - 1) * cntEat;
}

int Solve(QMap<int,int>& cnts)
{
    int curOpt = cnts.lastKey();

    for (int curFit = curOpt; curFit > 1; --curFit)
    {
        int specsUsed = 0;
        for(QMap<int, int>::const_iterator i = cnts.begin(); i != cnts.end(); ++i)
        {
            tryToFit(curFit, specsUsed, i.key(), i.value());
        }

        if (curFit + specsUsed < curOpt)
        {
            curOpt = curFit + specsUsed;
        }
    }

    return curOpt;
}

int main(int argc, char *argv[])
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();
    for (int i = 0; i < T; ++i)
    {
        QMap<int,int> cnts;
        int D;
        ins >> D;
        //qDebug("max: %d", D);
        for (int j = 0; j < D; ++j)
        {
            int k;
            ins >> k;
            //qDebug("max: %d", k);
            cnts[k] += 1;
        }

        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(QString::number(Solve(cnts))) << endl;
    }

    return 0;
}
