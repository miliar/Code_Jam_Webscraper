#include <QTextStream>
#include <QFile>
#include <QStringList>
#include <QGenericMatrix>
#include <QVector>
#include <QString>

#include <QDebug>

#include <cmath>

int AND(int a, int b);

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
    QStringList parameters = in.readLine().split(" ");
    int A = parameters[0].toInt();
    int B = parameters[1].toInt();
    int K = parameters[2].toInt();
    int ways = 0;
    for (int i = 0; i < A; ++i)
    {
      for (int j = 0; j < B; ++j)
      {
	if (AND(i, j) < K)
	{
	  ways++;
	}
      }
    }
    out << "Case #" << c << ": " << ways << endl;
  }
  inFile.close();
  outFile.close();
  return 0;
}

int AND(int a, int b)
{
  return a & b;
}