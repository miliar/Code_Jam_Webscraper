#include <QTextStream>
#include <QFile>
#include <QStringList>
#include <QGenericMatrix>
#include <QVector>
#include <QString>

#include <QDebug>

#include <cmath>
#include <algorithm>

void testElf(double PQ, int depth, int* firstFound);

int main(int argc, char** argv)
{
  QFile inFile("../input/input.txt");
  if(!inFile.open(QIODevice::ReadOnly)) {
    qDebug() <<  "ReadError:" << inFile.errorString();
    return -1;
  }
  QTextStream in(&inFile);
  QFile outFile("../input/output.txt");
  if(!outFile.open(QIODevice::WriteOnly)) {
    qDebug() <<  "WriteError:" << outFile.errorString();
    return -1;
  }
  QTextStream out(&outFile);
  out.setRealNumberNotation(QTextStream::FixedNotation);
  out.setRealNumberPrecision(7);
  int numberOfCases = in.readLine().toInt();
  qDebug() << "Cases:" << numberOfCases;
  for (int c = 1; c <= numberOfCases; ++c)
  {
    QStringList parameters = in.readLine().split("/");
    int P = parameters[0].toInt();
    int Q = parameters[1].toInt();
    qDebug() << P << Q;
    double PQ = (double)P/(double)Q;
    int firstFound = -1;
    testElf(PQ, 1, &firstFound);
    if (firstFound == -1)
    {
      out << "Case #" << c << ": impossible" << endl;
    }
    else
    {
      out << "Case #" << c << ": " << firstFound << endl;
    }
  }
  inFile.close();
  outFile.close();
  return 0;
}

void testElf(double PQ, int depth, int* firstFound)
{
  if (depth > 40)
  {
    *firstFound = -1;
    return;
  }
  if (PQ >= (1.0/std::pow(2,depth)))
  {
    int numbers = PQ/(1.0/std::pow(2,depth));
    PQ = PQ - numbers * (1.0/std::pow(2,depth));
    if (*firstFound == -1)
    {
      *firstFound = depth;
    }
  }
  if (PQ == 0)
  {
    qDebug() << *firstFound;
    return;
  }
  else
  {
    testElf(PQ, depth + 1, firstFound);
  }
}