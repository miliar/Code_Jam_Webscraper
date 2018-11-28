#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

void SplitLine(string line, vector<string> *result);
int Osmos(long A, int N, vector<long>& motes);
size_t BinInsPos(vector<long>& list, long val);

int main()
{
	ifstream fi;
	ofstream fo;
	string strTmp,strNo;
	char out[255];

	int i,j;
	int T,A,N;

	vector<string> tmpStrArr;
	vector<long> motes;


	fi.open ("A-small-attempt0.in");
	fo.open ("A-small-attempt0.out");

	// Get number of cases, N
	getline(fi,strTmp);
	T = atoi(strTmp.c_str());

	for (i = 0; i<T ; i++)
	{
		// Get A & N
		getline(fi,strTmp);
		SplitLine(strTmp, &tmpStrArr);
		A = atoi(tmpStrArr[0].c_str());
		N = atoi(tmpStrArr[1].c_str());

		// Parse N motes
		getline(fi,strTmp);
		SplitLine(strTmp, &tmpStrArr);
		motes.clear();
		for (j=0;j<tmpStrArr.size();j++)
		{
			motes.push_back(atol(tmpStrArr[j].c_str()));
		}

		// Evaluate test case & Write result to file
		sprintf_s(out,"Case #%d: %d\n",i+1,Osmos(A,N,motes));
		fo.write(out,strlen(out));
	}

	fi.close();
	fo.close();

	return 0;
}

void SplitLine(string line, vector<string> *result)
{
    string buf; // Have a buffer string
    stringstream ss(line); // Insert the string into a stream
	result->clear();
    while (ss >> buf)
        result->push_back(buf);
}

int Osmos(long A, int N, vector<long>& motes)
{
	int res = 0;
	int i, k_rmv;
	long tmp = 0;
	vector<long> AvaiMotes;

	// Parse N motes
	for (i=0;i<motes.size();i++)
	{
		if (A>motes[i])
		{
			A += motes[i];
			if (AvaiMotes.size()>0)
			{
				while(A>AvaiMotes[0])
				{
					A+=AvaiMotes[0];
					AvaiMotes.erase(AvaiMotes.begin());
					if (AvaiMotes.size()==0) break;
				}
			}
		}
		else
		{
			AvaiMotes.insert(AvaiMotes.begin()+BinInsPos(AvaiMotes, motes[i]), motes[i]);
		}
	}

	// Parse available motes
	while(AvaiMotes.size()>0)
	{
		k_rmv = AvaiMotes.size();
		if (k_rmv==1) return (res+1);
		if (pow(2,k_rmv-1)*(A-1)-1 > AvaiMotes[0])
		{
			while(A<=AvaiMotes[0])
			{
				A+=A-1;
				res+=1;
			}
			while(A>AvaiMotes[0])
			{
				A+=AvaiMotes[0];
				AvaiMotes.erase(AvaiMotes.begin());
				if (AvaiMotes.size()==0) return res;
			}
		}
		else
			return (res+k_rmv);
	}
	return res;
}

// Get position for binary insert a number into a sorted list
size_t BinInsPos(vector<long>& list, long val)
{
	size_t pos, start, end;	
	start = 0;
	end = list.size()-1;

	if (list.size()==0) return 0;
	
	while(1)
	{
		pos = start+(end-start)/2;	// Don't use (end+start)/2 to avoid integer overflow
		if (val<list[pos])
		{
			if (end==pos) break;
			end = pos;
		}
		else
		{
			start = pos++ + 1;
			if (start>end) break;
		}
	}
	return pos;
}
