// Google Code Jam 2015
// Qualifying Round
// A - Standing Ovation
//
// Adrian Dale
// 11/04/2015

#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

int T; // No of test cases

enum QValue
{
	Q_i = 0,
	Q_j,
	Q_k,
	Q_1,
	Q_ni,
	Q_nj,
	Q_nk,
	Q_n1
};

inline int QSign(QValue v)
{
	return (v == Q_i || v == Q_j || v == Q_k || v == Q_1) ? 1 : -1;
}

QValue QApplySign(QValue v, int Sign)
{
	if (Sign == -1)
	{
		switch (v)
		{
		case Q_i:
			return Q_ni;
		case Q_j:
			return Q_nj;
		case Q_k:
			return Q_nk;
		case Q_1:
			return Q_n1;

		case Q_ni:
			return Q_i;
		case Q_nj:
			return Q_j;
		case Q_nk:
			return Q_k;
		case Q_n1:
			return Q_1;
		}
	}
	return v;
}

QValue QAbs(QValue v)
{
	switch (v)
	{
	case Q_i:
	case Q_j:
	case Q_k:
	case Q_1:
		return v;
		
	case Q_ni:
		return Q_i;
	case Q_nj:
		return Q_j;
	case Q_nk:
		return Q_k;
	case Q_n1:
			return Q_1;
	}

	cout << "ERROR!" << endl;
	return Q_1;
}

QValue QMultiply(QValue lhs, QValue rhs)
{
	int lSign = QSign(lhs);
	int rSign = QSign(rhs);
	QValue lAbsQ = QAbs(lhs);
	QValue rAbsQ = QAbs(rhs);

	QValue resultV;
	int resultSign = 1;
	if (lAbsQ == Q_1)
	{
		resultV = rAbsQ;
	}
	else if (lAbsQ == Q_i)
	{
		if (rAbsQ == Q_1)
			resultV = Q_i;
		else if (rAbsQ == Q_i)
		{
			resultV = Q_1;
			resultSign = -1;
		}
		else if (rAbsQ == Q_j)
			resultV = Q_k;
		else if (rAbsQ == Q_k)
		{
			resultV = Q_j;
			resultSign = -1;
		}
		else
			cout << "ERROR!";
	}
	else if (lAbsQ == Q_j)
	{
		if (rAbsQ == Q_1)
			resultV = Q_j;
		else if (rAbsQ == Q_i)
		{
			resultV = Q_k;
			resultSign = -1;
		}
		else if (rAbsQ == Q_j)
		{
			resultV = Q_1;
			resultSign = -1;
		}
		else if (rAbsQ == Q_k)
		{
			resultV = Q_i;

		}
		else
			cout << "ERROR!";
	}
	else if (lAbsQ == Q_k)
	{
		if (rAbsQ == Q_1)
			resultV = Q_k;
		else if (rAbsQ == Q_i)
		{
			resultV = Q_j;
			
		}
		else if (rAbsQ == Q_j)
		{
			resultV = Q_i;
			resultSign = -1;
		}
		else if (rAbsQ == Q_k)
		{
			resultV = Q_1;
			resultSign = -1;
		}
		else
			cout << "ERROR!";
	}
	resultSign *= lSign * rSign;

	return QApplySign(resultV, resultSign);
}

QValue CharToQValue(char c)
{
	switch (c)
	{
	case 'i':
		return Q_i;
	case 'j':
		return Q_j;
	case 'k':
		return Q_k;
	}

	cout << "ERROR!";

	return Q_1;
}

char QValueToChar(QValue q)
{
	switch (q)
	{
	case Q_i:
		return 'i';
	case Q_j:
		return 'j';
	case Q_k:
		return 'k';
	case Q_1:
		return '1';
	case Q_ni:
		return 'I';
	case Q_nj:
		return 'J';
	case Q_nk:
		return 'K';
	case Q_n1:
		return 'L';
	}

	cout << "ERROR!";

	return Q_1;
}

map<QValue, vector<QValue> > gAccumStrings;
QValue gQValueList[] = { Q_i, Q_j, Q_k, Q_1, Q_ni, Q_nj, Q_nk, Q_n1 };

void SolveTestCase_HARD(int L, int X, string dijkstring)
{
	cout << "Solving for  " << L << ", " << X << ", " << dijkstring << endl;

	gAccumStrings.clear();

	
	
	for (QValue startQv : gQValueList)
	{
		vector<QValue> accumString;
		QValue accum = startQv;
		for (auto dijk : dijkstring)
		{	
			QValue qv = CharToQValue(dijk);

			accum = QMultiply(accum, qv);
			accumString.push_back(accum);
		}
		gAccumStrings[startQv] = accumString;
	}
	
}

// Basic version
void SolveTestCase_TOO_SLOW(int L, int X, string dijkstring)
{
	//cout << "Solving for  " << L << ", " << X << ", " << dijkstring << endl;

	vector<QValue> testString;
	for (int i = 0; i < X; ++i)
	{
		for (auto dijk : dijkstring)
		{
			QValue qv = CharToQValue(dijk);
			testString.push_back(qv);
		}
	}

	QValue accum = Q_1;
	bool found = false;
	for (int i = 0; i < testString.size()-2; ++i)
	{	
		QValue qv = testString[i];

		accum = QMultiply(accum, qv);
		
		if (accum == Q_i)
		{
			// Found a possible starting point - now try all possible j's
			QValue accumj = Q_1;
			for (int j = i + 1; j < testString.size() - 1; ++j)
			{
				QValue qvj = testString[j];
				accumj = QMultiply(accumj, qvj);
				if (accumj == Q_j)
				{
					// Found a possible j, too - now see if remainder ends with k
					QValue accumk = Q_1;
					for (int k = j + 1; k < testString.size(); ++k)
					{
						QValue qvk = testString[k];
						accumk = QMultiply(accumk, qvk);
					}
					if (accumk == Q_k)
					{
						found = true;
						cout << "YES";
						return;
					}
				}
			}
		}
		
	}
	cout << "NO";
}

// Basic version
void SolveTestCase(int L, int X, string dijkstring)
{
	//cout << "Solving for  " << L << ", " << X << ", " << dijkstring << endl;

	vector<QValue> testString;
	for (int i = 0; i < X; ++i)
	{
		for (auto dijk : dijkstring)
		{
			QValue qv = CharToQValue(dijk);
			testString.push_back(qv);
		}
	}

	set<int> invalidK;

	QValue accum = Q_1;
	bool found = false;
	for (int i = 0; i < testString.size() - 2; ++i)
	{
		QValue qv = testString[i];

		accum = QMultiply(accum, qv);

		if (accum == Q_i)
		{
			// Found a possible starting point - now try all possible j's
			QValue accumj = Q_1;
			for (int j = i + 1; j < testString.size() - 1; ++j)
			{
				QValue qvj = testString[j];
				accumj = QMultiply(accumj, qvj);
				if (accumj == Q_j)
				{
					// Found a possible j, too - now see if remainder ends with k
					if (invalidK.find(j + 1) == invalidK.end())
					{
						QValue accumk = Q_1;
						for (int k = j + 1; k < testString.size(); ++k)
						{
							QValue qvk = testString[k];
							accumk = QMultiply(accumk, qvk);
						}
						if (accumk == Q_k)
						{
							found = true;
							cout << "YES";
							return;
						}
						else
						{
							invalidK.insert(j + 1);
						}
					}
				}
			}
		}

	}
	cout << "NO";
}

void ReadTestCases()
{
	string line;

	getline(cin, line);
	istringstream parser(line);
	parser >> T;

	int TestNo = 1;
	while (TestNo <= T)
	{
		getline(cin, line);
		parser.str(line);
		parser.clear();
		int L;
		int X;
		parser >> L >> X;
		string dijkstring;
		getline(cin, dijkstring);
		
		cout << "Case #" << TestNo << ": ";
		SolveTestCase(L, X, dijkstring);
		cout << endl;

		++TestNo;
	}
}

int main()
{
	ReadTestCases();
	//SolveTestCase(1, 1, "jij");
	return 0;
}
