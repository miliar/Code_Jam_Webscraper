/**
* File:		Round00_ProbC.cpp
* Title:	Google Code Jam 2015 - Qualification Round - Problem C - Dijkstra
* Author:	R.Quatrefoil
* Date:		2015-04-11
* Purpose:	Split substrings
* Notes:	Created using Microsoft Visual Studio 2013
*
*			May have been way overthinking this.
*			You must have an i at beginning and k at end (possibly with 1 on either side)
*			Once you have that, you must have j in the middle (possibly with 1 on either side)
*			Only difference would be where the 1's distribute, which doesn't matter
*				(1s could be next to i or next to j, or they could be cut next to j or next to k)
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cctype>

using namespace std;

class Quaternion
{
private:
	int sign;		//is the current quaternion positive or negative (should only be -1 or +1)
	char value;		//the current value can be 1, i, j, k
public:
	Quaternion(char val = '1', int posOrNeg = 1);		//fcn proto, default constructor
	void setSign(int posOrNeg);		//fcn proto
	void setValue(char val);		//fcn proto
	int getSign();		//fcn proto
	char getValue();		//fcn proto
	bool isChar(char ch);		//fcn proto

	friend Quaternion operator*(Quaternion rObj, Quaternion lObj);		//fcn proto
};

void Quaternion::setSign(int posOrNeg)
//void setSign(int posOrNeg);		//fcn proto
{
	if (posOrNeg >= 0)
		sign = 1;
	else
		sign = -1;
}

void Quaternion::setValue(char val)
//void setValue(char val);		//fcn proto
{
	if (val >= 'i' && val <= 'k')
		value = val;
	else
		value = '1';
}

int Quaternion::getSign()
//int getSign();		//fcn proto
{
	return sign;
}

char Quaternion::getValue()
//char getValue();		//fcn proto
{
	return value;
}

bool Quaternion::isChar(char ch)
//bool isChar(char ch);		//fcn proto
{
	if (value == ch && sign == 1)
		return true;
	else
		return false;
}

Quaternion::Quaternion(char val, int posOrNeg)
//Quaternion(char val = '1', int posOrNeg = 1);		//fcn proto, default constructor
//default constructor
{
	tolower(val);		//force character to be lowercase

	if (val >= 'i' && val <= 'k')
		value = val;
	else
		value = '1';

	if (posOrNeg >= 0)
		sign = 1;
	else
		sign = -1;
}

Quaternion operator*(Quaternion lObj, Quaternion rObj)
//friend Quaternion operator*(Quaternion rObj, Quaternion lObj);		//fcn proto
{
	Quaternion newObj;		//the new quaternion object being created based on old quaternions multiplied

	//first figure out new value and new negative sign based only on values
	if (lObj.value == '1')
	{
		newObj.value = rObj.value;
		//newObj.sign will just be based on (lObj.sign * rObj.sign) at end
	}
	else if (rObj.value == '1')
	{
		newObj.value = lObj.value;
		//newObj.sign will just be based on (lObj.sign * rObj.sign) at end
	}
	else if (lObj.value == rObj.value)		// && lObj.value != 1 is not necessary since those checks came first
	{
		newObj.value = '1';
		//newObj.sign based on an extra negative beyond (lObj.sign * rObj.sign) at end
		newObj.sign = -1;
	}
	else if (lObj.value == 'i')
	{
		if (rObj.value == 'j')
		{
			newObj.value = 'k';
			//newObj.sign will just be based on (lObj.sign * rObj.sign) at end
		}
		else		//if (rObj.value == 'k')
		{
			newObj.value = 'j';
			//newObj.sign based on an extra negative beyond (lObj.sign * rObj.sign) at end
			newObj.sign = -1;
		}
	}
	else if (lObj.value == 'j')
	{
		if (rObj.value == 'i')
		{
			newObj.value = 'k';
			//newObj.sign based on an extra negative beyond (lObj.sign * rObj.sign) at end
			newObj.sign = -1;
		}
		else		//if (rObj.value == 'k')
		{
			newObj.value = 'i';
			//newObj.sign will just be based on (lObj.sign * rObj.sign) at end
		}
	}
	else if (lObj.value == 'k')
	{
		if (rObj.value == 'i')
		{
			newObj.value = 'j';
			//newObj.sign will just be based on (lObj.sign * rObj.sign) at end
		}
		else		//if (rObj.value == 'j')
		{
			newObj.value = 'i';
			//newObj.sign based on an extra negative beyond (lObj.sign * rObj.sign) at end
			newObj.sign = -1;
		}
	}

	//second figure out real negative sign based on calc and old negs
	newObj.sign *= lObj.sign * rObj.sign;

	return newObj;
}

bool isIJK(vector<Quaternion> &quat);		//fcn proto

int main()
{
	ifstream iFile("Round00_ProbC_Input.txt", ios::in);
	ofstream oFile;		//will only open if iFile opens correctly

	int testCasesTotal = 0;		//total number of test cases to evaluate (1 <= T <= 100)
	int initNumBaseChars = 0;		//initial number of characters in base string (1 <= L < = 10000)
	int initNumBaseRepeats = 0;		//number of times the base string repeats to make initial string (1 <= X <= 10000 for small) (1 <= X <= 10^12 for large)
	string initBaseString;		//initial base string at the start of a case before repeats (only i, j, or k)
	vector<Quaternion> initQuaternions;		//initial quaternions based on initString (1 <= L * X <= 10000 for small) (1 <= L * X <= 10^16 for large)
	bool isDijkstra = false;		//can Edsger Dijkstra's name be made from quaternion string
	string successFailure;		//output "YES" or "NO" if case worked or not

	if (iFile)
	{
		oFile.open("Round00_ProbC_Output.txt", ios::out | ios::trunc);

		iFile >> testCasesTotal;
		for (int currCase = 0; currCase < testCasesTotal; currCase++)		//evaluate all test cases
		{
			//initialize all values at the start of a case
			isDijkstra = false;		//re-init for each case
			initQuaternions.clear();				//re-init for each case

			iFile >> initNumBaseChars;
			iFile >> initNumBaseRepeats;
			iFile >> initBaseString;

			for (int y = 0; y < initNumBaseRepeats; y++)
			{
				for (int x = 0; x < initNumBaseChars; x++)
				{
					initQuaternions.push_back(Quaternion(initBaseString[x]));
				}
			}

			//calculate the possibilities recursively
			isDijkstra = isIJK(initQuaternions);

			//create message for output
			if (isDijkstra)
				successFailure = "YES";
			else
				successFailure = "NO";

			//output case to file
			oFile << "Case #" << (currCase + 1) << ": " << successFailure << endl;
		}

		iFile.close();
		oFile.close();
		cout << "Output successful!!" << endl;
	}
	else
	{
		cout << "Error opening input file!!" << endl;
	}

	cout << endl << endl << "Press Enter key to continue..." << endl;
	cin.get();
	return 0;
}//endfcn main

bool isIJK(vector<Quaternion> &quat)
//bool isIJK(vector<Quaternion> &quat);		//fcn proto
{
	Quaternion testQuat('1', 1);		//should be same as just Quaternion testQuat;
	int subIndexForw = 0;
	int subIndexRev = quat.size() - 1;
	bool iFound = false;
	bool jFound = false;
	bool kFound = false;

	//pull an i (plus maybe some 1s) off beginning
	while ((subIndexForw < (quat.size() - 2)) && !iFound)
	{
		testQuat = testQuat * quat[subIndexForw];		//order matters since not commutative (forw since coming from left)

		if (testQuat.isChar('i'))
			iFound = true;

		subIndexForw++;		//this will advance one beyond where end is found, which is desirable, so start of next
	}

	//reset testQuat
	testQuat.setValue('1');
	testQuat.setSign(1);

	if (iFound)
	{
		//pull a k (plus maybe some 1s) off end
		while ((subIndexRev > subIndexForw) && !kFound)
		{
			testQuat = quat[subIndexRev] * testQuat;		//order matters since not commutative (reversed since coming from right)

			if (testQuat.isChar('k'))
				kFound = true;

			subIndexRev--;		//this will advance one beyond where start is found, which is ok, index of end rather than past it
		}
	}

	//reset testQuat
	testQuat.setValue('1');
	testQuat.setSign(1);

	if (iFound && kFound)
	{
		//check if middle is a j (plus maybe some 1s)
		while (subIndexForw <= subIndexRev)
		{
			testQuat = testQuat * quat[subIndexForw];		//order matters since not commutative (forw since coming from left)

			subIndexForw++;
		}

		if (testQuat.isChar('j'))
			jFound = true;
	}

	return (iFound && jFound && kFound);
}