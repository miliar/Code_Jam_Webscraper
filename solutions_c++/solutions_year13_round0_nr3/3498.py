#include <QFileInfo>
#include <QFile>
#include <QString>
#include "QStringList"
#include <iostream>
#include <QTextStream>
#include <QList>
#include "QVector"
#include "QMap"
#include "QSet"
#include "qmath.h"
using namespace std;


struct Node {
	Node(int h) {
		height = h;
		verticalObstacle = false;
		horizontalObstacle = false;
	}
	int height;
	bool verticalObstacle;
	bool horizontalObstacle;
};

typedef QList<QList<int> > IntMatrix;
typedef QList<int> IntVector;

typedef QMap<int, int> IntIntMap;
typedef QSet<int> IntSet;

IntVector openChests(int& noOfChests, IntVector availableKeys, IntIntMap& keyTypeToChestMap, IntIntMap& chestToKeyTypeMap, IntIntMap& chestToAvailableKeysMap, IntVector unopenedChestList, IntVector openedChestVector ) {
	if ( openedChestVector.size() == noOfChests ) return openedChestVector;
	//Quick feasibility check
	IntIntMap keyToRequirementMap, keyToPotentialAvailabilityMap;
	foreach(int chestNo, unopenedChestList  ) {
		keyToRequirementMap[chestToKeyTypeMap.value(chestNo)]++;
		IntVector unlockedKeys = chestToAvailableKeysMap.values(chestNo);
		foreach(int keyType, unlockedKeys) {
			keyToPotentialAvailabilityMap[keyType]++;
		}
	}
	foreach(int keyType, availableKeys) {
		keyToPotentialAvailabilityMap[keyType]++;
	}
	IntIntMap::iterator iter = keyToRequirementMap.begin();
	for(; iter != keyToRequirementMap.end(); iter++) {
		if ( iter.value() > keyToPotentialAvailabilityMap.value(iter.key()) ) {
			return openedChestVector;
		}
	}
	foreach (int chestNo , unopenedChestList) {
		int keyType = chestToKeyTypeMap.value(chestNo);
		IntVector currentAvailableKeys = availableKeys;
		if ( currentAvailableKeys.removeOne(keyType) ) {
			IntVector newKeyVector = chestToAvailableKeysMap.values(chestNo);
			currentAvailableKeys.append(newKeyVector);
			if ( currentAvailableKeys.isEmpty() ) continue;
			IntVector currentUOCV = unopenedChestList;
			currentUOCV.removeOne(chestNo);
			IntVector currentOCV = openedChestVector;
			currentOCV.push_back(chestNo);
			IntVector oCV = openChests(noOfChests, currentAvailableKeys, keyTypeToChestMap, chestToKeyTypeMap, chestToAvailableKeysMap, currentUOCV, currentOCV);
			if ( oCV.size() == noOfChests ) return oCV;
		}
	}
	return openedChestVector;
}

bool isPalyndrome(long int num) {
	QString str = QString::number(num);
	int size = str.size();
	for(int i = 0; i < size/2; i++ ) {
		if ( str.at(i) != str.at(size-i-1)) {
			return false;
		}
	}
	return true;
}

int main() {
	QFile smallIn("D:/Working/Merging/GCJ/LawnMower/debug/small-in.txt");
	if (!smallIn.open(QIODevice::ReadOnly | QIODevice::Text)) {
		return 1;
	}

	QFile smallOut("D:/Working/Merging/GCJ/LawnMower/debug/C-small-out.txt");
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
	int t = inputStrList.at(currentLineNo++).toInt();

	for(int testCaseNo = 0; testCaseNo < t; testCaseNo++) {
		QStringList knStrList = inputStrList.at(currentLineNo++).split(" ");
		int A = knStrList.at(0).toInt();
		int B = knStrList.at(1).toInt();
		/*int K = knStrList.at(0).toInt();
		int N = knStrList.at(1).toInt();

		QStringList startKeyStrList = inputStrList.at(currentLineNo++).split(" ");
		IntVector keyList, unOpenedChestList;
		for(int i = 0; i < startKeyStrList.size(); i++ ) {
			keyList.push_back(startKeyStrList.at(i).toInt());
		}
		IntIntMap keyTypeToChestMap, chestToKeyTypeMap, chestToAvailableKeyTypeMap;
		for (int i = 0; i < N; i++ ) {
			QStringList keyTypeAndKeysStrList = inputStrList.at(currentLineNo++).split(" ");
			keyTypeToChestMap.insertMulti(keyTypeAndKeysStrList.first().toInt(), i+1);
			chestToKeyTypeMap.insert(i+1, keyTypeAndKeysStrList.first().toInt());
			int noOfKeysInside = keyTypeAndKeysStrList.at(1).toInt();
			for(int j = 0; j < noOfKeysInside; j++) {
				chestToAvailableKeyTypeMap.insertMulti(i+1, keyTypeAndKeysStrList.at(2+j).toInt());
			}
			unOpenedChestList.push_back(i+1);
		}
		IntSet openedChestSet;
		IntVector openedChestVector;
		IntVector oCV = openChests(N, keyList, keyTypeToChestMap, chestToKeyTypeMap, chestToAvailableKeyTypeMap, unOpenedChestList,  openedChestVector);

		if ( oCV.size() == N ) {
			QStringList orderedChestList;
			for(int i = 0; i < oCV.size(); i++ ) {
				orderedChestList.push_back(QString::number(oCV.at(i)));
			}
			out << "Case #" << testCaseNo+1 << ": " << orderedChestList.join(" ") << "\n";
		} else {
			out << "Case #" << testCaseNo+1 << ": IMPOSSIBLE\n" ;
		}*/
		int a = (int) qSqrt((qreal)A);
		int b = (int) qSqrt((qreal)B);
		int count = 0;
		for (int i = a; i <= b; i++ ) {
			if ( isPalyndrome(i) ) {
				int sqr = i*i;
				if ( (sqr > B) || (sqr < A) ) continue;
				if (isPalyndrome(sqr)) {
					count++;
				}
			}
		}
		out << "Case #" << testCaseNo+1 << ": " << count << "\n";
	}


	return 0;
}

