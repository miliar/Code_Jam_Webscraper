// StandingOvation.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>

using namespace std;

const int SMAX = 1000;
const int TMAX = 100;

struct SInputData
{
	int ShyMax;
	char ShyLevel [SMAX + 1];
};

struct SOutputData
{
	int Output;
};


class CIOManager
{
public:
	CIOManager(void);
	~CIOManager(void);

	void ParseInputs();
	void WriteOutputs();
	void ProcessData();
	void StoreOutput(int index);

protected:
	int m_nTestCases;
	SInputData m_inputs[TMAX];
	SOutputData m_outputs[TMAX];
};

int _tmain(int argc, _TCHAR* argv[])
{
	CIOManager ioManager;
	ioManager.ParseInputs();
	ioManager.ProcessData();
	ioManager.WriteOutputs();
	return 0;
}



CIOManager::CIOManager(void)
{
}

CIOManager::~CIOManager(void)
{
}

void CIOManager::ParseInputs()
{
	ifstream input("E:\\CJ\\A-large.in");
	if(!input.bad())
	{
		input>>m_nTestCases;
		if(m_nTestCases > TMAX)
		{
			m_nTestCases = 100;
		}
		for(int i =0; i < m_nTestCases; i++)
		{
			input>>m_inputs[i].ShyMax;
			input>>m_inputs[i].ShyLevel;
		}
		input.close();
	}
}

void CIOManager::WriteOutputs()
{
	ofstream input("E:\\CJ\\Output.txt");
	if(!input.bad())
	{
		for(int i =0; i < m_nTestCases; i++)
		{
			if(i == 0)
			{
				input<<"Case #"<<(i + 1)<<": "<<m_outputs[i].Output;
			}
			else
			{
				input<<"\rCase #"<<(i + 1)<<": "<<m_outputs[i].Output;
			}
		}
		input.close();
	}
}

void CIOManager::ProcessData()
{
	for(int i = 0; i < m_nTestCases; i++)
	{
		StoreOutput(i);
	}
}

void CIOManager::StoreOutput(int index)
{
	char szShyLevel[1024];
	strcpy(szShyLevel, m_inputs[index].ShyLevel);

	int output = 0;
	int numPeoples = 0;
	
	for(int shyLevel = 0; shyLevel <= m_inputs[index].ShyMax; shyLevel++)
	{
		if(numPeoples < shyLevel)
		{
			int diff = shyLevel - numPeoples;
			if(diff > output)
			{
				output = diff;
			}
		}
		numPeoples += szShyLevel[shyLevel] - '0';
	}
	m_outputs[index].Output = output;
}