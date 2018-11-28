/*
 * (C) Copyright Martin Juhlin, 2013
 * martin.juhlin@gmal.com
 */

#include <textio.h>
#include <QMap>
#include <QVarLengthArray>

static bool testCase(TextInput * ti);

int main(int argc, char ** argv)
{
    TextInput * ti = TextInput::setupOrExit(argc, argv);
    TextOutput to;
    int cases = ti->readNumber();
    for (int c = 0; c < cases; c++) {
        bool res = testCase(ti);
        to.out(res ? "YES" : "NO");
        to.endl();
    }
    
    delete ti;
    return 0;
}

bool testCase(TextInput* ti)
{
    QList<int> dim = ti->readVector();
    int N = dim.at(0);
    int M = dim.at(1);

    QList<int> posX, posY;
    for (int i = 0; i < M; i++)
        posX.append(0);
    for (int i = 0; i < N; i++)
        posY.append(0);
    Q_ASSERT(posX.size() == M);
    Q_ASSERT(posY.size() == N);
    
    //QScopedPointer<int> cleanup(new int[N * M]);
    QList< QList< int > > matrix;
    for (int y = 0; y < N; y++) {
        QList<int> l = ti->readVector();
        Q_ASSERT(l.size() == M);
        matrix.append(l);
        for (int x = 0; x < M; x++) {
            int v = l.at(x);
            posY[y] = qMax<int>(posY[y], v);
            posX[x] = qMax<int>(posX[x], v);
            // qDebug("v=%d posX=%d posY=%d", v, posX[x], posY[y]);
        }
    }
    
    // qDebug("--");
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < M; x++) {
            int cell = matrix.at(y).at(x);
            int allow = qMin<int>(posX[x], posY[y]);
            if (cell < allow)
                return false;
            // qDebug("cell = %d, %d", cell, allow);
        }
    }
    return true;
}
