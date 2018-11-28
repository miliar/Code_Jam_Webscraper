#include <QtCore/QCoreApplication>
#include <QFile>
#include <QTextStream>
#include <QDebug>
#include <QStringList>
#include <QList>
#include <QtCore/qmath.h>
#include <math.h>
#include <iostream>

//I use Qt 5.2.0 that can be downloaded from http://www.qt.io/download-open-source/

QFile go_InFile("Input.in");
QFile go_OutFile("Output.txt");
QTextStream out(&go_OutFile);

int main(int argc, char *argv[])
{
 	QCoreApplication a(argc, argv);
 
	if (go_InFile.open(QIODevice::ReadOnly | QIODevice::Text) == false)
		return -1;

	if (go_OutFile.open(QIODevice::WriteOnly | QIODevice::Text) == false)
		return -1;

	QTextStream oTextStream(&go_InFile);

	QString sLine = oTextStream.readLine();
	int iNoOftestCases = sLine.toInt();

	for (int i = 1; i <= iNoOftestCases; ++i)
	{
		out << "Case #" << i << ": ";

		sLine = oTextStream.readLine();
		QStringList lstTmp = sLine.split(" ");
		int iSMax = lstTmp.at(0).toInt();
		QString sAudi = lstTmp.at(1);
		
		int iAns = 0;
		int iTotal = 0;

		for (int iS = 0; iS <= iSMax; ++iS)
		{
			int iNum = sAudi.at(iS).digitValue();

			if (iTotal < iS)
			{
				iAns = iAns + iS - iTotal;
				iTotal = iS;
			}

			iTotal = iTotal + iNum;

		}

		out  << iAns << "\n";
	}

	go_OutFile.close();
	go_InFile.close();

	qDebug() << "Completed";

	return a.exec();
}

