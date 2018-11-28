#include <QFileInfo>
#include <QFile>
#include <QString>
#include "QStringList"
#include <iostream>
#include <QTextStream>
#include <QList>
#include "QVector"
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


int main() {
	QFile smallIn("D:/Working/Merging/GCJ/LawnMower/debug/B-large.in");
	if (!smallIn.open(QIODevice::ReadOnly | QIODevice::Text)) {
		return 1;
	}

	QFile smallOut("D:/Working/Merging/GCJ/LawnMower/debug/small-out2.txt");
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
		int n = inputStrList.at(currentLineNo).split(" ").at(0).toInt();
		int m = inputStrList.at(currentLineNo).split(" ").at(1).toInt();
		IntMatrix pattern;
		IntVector hMaxValVec, vMaxValVec;
		
		currentLineNo++;
		for (int rowNo = 0; rowNo < n; rowNo++ ) {
			IntVector newRow;
			pattern.push_back(newRow);
			QString rowStr = inputStrList.at(currentLineNo);
			currentLineNo++;
			QStringList colValStrList = rowStr.split(" ");
			if ( colValStrList.size() != m ) {
				out << "Error. colValStrList.size() != m";
				return 2;
			}
			for(int colNo = 0; colNo < m; colNo++) {
				int h = colValStrList.at(colNo).toInt();
				pattern[rowNo].push_back(h);
				if ( rowNo == 0 ) {
					vMaxValVec.push_back(h);
				} else if ( vMaxValVec.at(colNo) < h ) {
					vMaxValVec[colNo] = h;
				}
				if ( colNo == 0 ) {
					hMaxValVec.push_back(h);
				} else if ( hMaxValVec.at(rowNo) < h ) {
					hMaxValVec[rowNo] = h;
				}
			}
		}

		bool isFeasible = true;
		for (int rowNo = 0; rowNo < n; rowNo++ ) {
			for(int colNo = 0; colNo < m; colNo++) {
				if ( (pattern[rowNo][colNo] < vMaxValVec.at(colNo)) && (pattern[rowNo][colNo] < hMaxValVec.at(rowNo)) ) {
					isFeasible = false;
					break;
				}
			}
			if ( ! isFeasible ) break;
		}

		out << "Case #" << testCaseNo+1 << ": " << (isFeasible?"YES":"NO") << "\n";




	}


	return 0;
}