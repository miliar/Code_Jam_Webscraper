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

	QString sRichard = "RICHARD";
	QString sGarbrial = "GABRIEL";

	for (int i = 1; i <= iNoOftestCases; ++i)
	{

		out << "Case #" << i << ": ";

		sLine = oTextStream.readLine();
		QStringList lstTmp = sLine.split(" ");

		int iX = lstTmp.at(0).toInt();
		int iR = lstTmp.at(1).toInt();
		int iC = lstTmp.at(2).toInt();

		int iArea = iR * iC;

		if (iArea < iX)
		{
			out << sRichard << "\n";
			continue;
		}
		
		if (iArea % iX != 0)
		{
			out << sRichard << "\n";
			continue;
		}

		if (iX <= 2)
		{
			out << sGarbrial << "\n";
			continue;
		}

		int iMinSize = qMin(iR, iC);
		if ( (iMinSize + 1) * (iMinSize + 1)  <= iX)
		{
			out << sRichard << "\n";
			continue;
		}

		if (qMax(iR, iC) < iX)
		{
			out << sRichard << "\n";
			continue;
		}

		if (iArea == 2 * iX && iX == 4)
		{
			out << sRichard << "\n";
			continue;
		}

		if (iArea == 3 && iX > 2)
		{
			out << sRichard << "\n";
			continue;
		}
		
		
		out << sGarbrial << "\n";
	}

	go_OutFile.close();
	go_InFile.close();

	qDebug() << "Completed";

	return a.exec();
}

