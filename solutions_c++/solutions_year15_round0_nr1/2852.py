#include <QVector>
#include <QTextStream>

int main(int argc, char *argv[])
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();
    for (int i = 0; i < T; ++i)
    {
        int Max;
        ins >> Max;
        //qDebug("max: %d", Max);
        long nCur = 0;
        long nNeeded = 0;
        ins.skipWhiteSpace();
        for (int curLvl = 0; curLvl <= Max; ++curLvl)
        {
            char ch;
            ins >> ch;
            int nAtCur = (ch - '0');
            //qDebug("next: %d", nAtCur);
            if (nCur >= curLvl)
            {
                nCur += nAtCur;
            }
            else
            {
                long req = curLvl - nCur;
                nNeeded += req;
                nCur += (req + nAtCur);
            }
        }
        ins.readLine();

        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(QString::number(nNeeded)) << endl;
    }

    return 0;
}
