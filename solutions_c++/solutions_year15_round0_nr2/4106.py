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
		int iD = sLine.toInt();

		sLine = oTextStream.readLine();
		QStringList lstTmp = sLine.split(" ");

		QMap<int, char> mapPlates1;
		QMap<int, char> mapPlates2;

		for (int j = 0; j < iD; ++j)
		{
			mapPlates1.insertMulti(lstTmp.at(j).toInt(), 0);
			mapPlates2.insertMulti(lstTmp.at(j).toInt(), 0);
		}

		int iMinValue = INT_MAX;

		int iProcessedCount = 0;

		while (true)
		{
			const int iMax = mapPlates1.lastKey();

			iMinValue = qMin(iMinValue, iProcessedCount + mapPlates1.lastKey());

			iProcessedCount = iProcessedCount + mapPlates1.count(iMax);

			if (iMax <= 3)
			{
				break;
			}




			QMap<int, char>::Iterator ite = mapPlates1.lowerBound(iMax);
			QMap<int, char>::Iterator iteEnd = mapPlates1.end();

			QList<int> tmpValues;

			while (ite != iteEnd)
			{
				int iValue = ite.key();
				ite = mapPlates1.erase(ite);

				int iValue1 = iValue / 2;
				int iValue2 = iValue - iValue1;

				tmpValues << iValue1;
				tmpValues << iValue2;


			}

			for	(int k = 0; k < tmpValues.size(); k++)
			{
				mapPlates1.insertMulti(tmpValues.at(k), 0);
			}
		}


			////////////////////////////////////////////////////////////////////
			iProcessedCount = 0;

			while (true)
			{
				const int iMax = mapPlates2.lastKey();

				iMinValue = qMin(iMinValue, iProcessedCount + mapPlates2.lastKey());

				iProcessedCount = iProcessedCount + mapPlates2.count(iMax);

				if (iMax <= 3)
				{
					break;
				}




				QMap<int, char>::Iterator ite = mapPlates2.lowerBound(iMax);
				QMap<int, char>::Iterator iteEnd = mapPlates2.end();

				QList<int> tmpValues;

				while (ite != iteEnd)
				{
					int iValue = ite.key();
					ite = mapPlates2.erase(ite);

					int iValue1 = iValue / 2;

					if (iValue == 9)
						--iValue1;

					int iValue2 = iValue - iValue1;

					

					tmpValues << iValue1;
					tmpValues << iValue2;


				}

				for	(int k = 0; k < tmpValues.size(); k++)
				{
					mapPlates2.insertMulti(tmpValues.at(k), 0);
				}

		}

		out << iMinValue << "\n";
	}

	go_OutFile.close();
	go_InFile.close();

	qDebug() << "Completed";

	return a.exec();
}

