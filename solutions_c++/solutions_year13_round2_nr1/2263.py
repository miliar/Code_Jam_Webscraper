#include <QFileInfo>
#include <QFile>
#include <QString>
#include "QStringList"
#include <iostream>
#include <QTextStream>
#include <QList>
#include <QMap>
#include <QSet>
#include "QVector"
#include <cmath>
#include <QtAlgorithms>
#include <qmath.h>
using namespace std;
typedef long long LongInt;

int minOperations = INT_MAX;
int A;
int N;

void findMin(QList<LongInt> moteList, int currentA, int currentMin) {
	while(! moteList.isEmpty() && moteList.first() < currentA ) {
		currentA += moteList.first();
		moteList.pop_front();
	}

	if ( ! moteList.isEmpty() ) {
		if ( currentA > 1 )
		findMin(moteList, 2*currentA-1, currentMin+1);
		moteList.pop_back();
		findMin(moteList, currentA, currentMin+1);
	} else {
		if ( currentMin < minOperations ) {
			minOperations = currentMin;
		}
	}
}

int main() {
	QFile smallIn("D:/murthy/1B/inout/A-small-attempt0.in");
	if (!smallIn.open(QIODevice::ReadOnly | QIODevice::Text)) {
		return 1;
	}

	QFile smallOut("D:/murthy/1B/inout/A-small-out.txt");
	if ( ! smallOut.open(QIODevice::WriteOnly | QIODevice::Text)) {
		return 1;
	}

	QTextStream in(&smallIn);
	QTextStream out(&smallOut);
	QStringList inputStrList;
	while (!in.atEnd()) {
		QString line = in.readLine();
		inputStrList.push_back(line);
	}

	int currentLineNo = 0;
	int t = inputStrList.at(currentLineNo).toInt();
	currentLineNo++;

	for(int testCaseNo = 0; testCaseNo < t; testCaseNo++) {
		minOperations = INT_MAX;
		QString rowStr = inputStrList.at(currentLineNo++);
		QStringList strList = rowStr.split(" ");
		A = strList.at(0).toInt();
		N = strList.at(1).toInt();
		QString row2 = inputStrList.at(currentLineNo++);
		QStringList moteList = row2.split(" ");
		QList<LongInt> moteSet; 
		foreach(QString mote, moteList) {
			moteSet.push_back(mote.toInt());
		}
		qSort(moteSet);

		findMin(moteSet, A, 0);

		if ( 1 ) {
			out << "Case #" << testCaseNo+1  << ": " << minOperations << "\n";
		}
	}

	return 0;
}

