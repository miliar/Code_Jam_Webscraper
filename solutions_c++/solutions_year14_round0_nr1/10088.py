#include "StdAfx.h"
#include "MagicTrick.h"

CMagicTrick::CMagicTrick(void)
{
m_iCaseNumber=1;
}

CMagicTrick::~CMagicTrick(void)
{

}
void CMagicTrick::Run()
{
	string input;
	m_oInput.ReadLine();
	while( (input=m_oInput.ReadLine()).length())
	{
		m_iSelected1=atoi(input.c_str())-1;
		input=m_oInput.ReadLine();
		sscanf(input.c_str(),"%d %d %d %d",&m_aMatrix[0][0],&m_aMatrix[0][1],&m_aMatrix[0][2],&m_aMatrix[0][3]);
		input=m_oInput.ReadLine();
		sscanf(input.c_str(),"%d %d %d %d",&m_aMatrix[1][0],&m_aMatrix[1][1],&m_aMatrix[1][2],&m_aMatrix[1][3]);
		input=m_oInput.ReadLine();
		sscanf(input.c_str(),"%d %d %d %d",&m_aMatrix[2][0],&m_aMatrix[2][1],&m_aMatrix[2][2],&m_aMatrix[2][3]);
		input=m_oInput.ReadLine();
		sscanf(input.c_str(),"%d %d %d %d",&m_aMatrix[3][0],&m_aMatrix[3][1],&m_aMatrix[3][2],&m_aMatrix[3][3]);
		
		input=m_oInput.ReadLine();
		m_iSelected2=atoi(input.c_str())-1+4;
		input=m_oInput.ReadLine();
		sscanf(input.c_str(),"%d %d %d %d",&m_aMatrix[4][0],&m_aMatrix[4][1],&m_aMatrix[4][2],&m_aMatrix[4][3]);
		input=m_oInput.ReadLine();
		sscanf(input.c_str(),"%d %d %d %d",&m_aMatrix[5][0],&m_aMatrix[5][1],&m_aMatrix[5][2],&m_aMatrix[5][3]);
		input=m_oInput.ReadLine();
		sscanf(input.c_str(),"%d %d %d %d",&m_aMatrix[6][0],&m_aMatrix[6][1],&m_aMatrix[6][2],&m_aMatrix[6][3]);
		input=m_oInput.ReadLine();
		sscanf(input.c_str(),"%d %d %d %d",&m_aMatrix[7][0],&m_aMatrix[7][1],&m_aMatrix[7][2],&m_aMatrix[7][3]);
		ProcessMessage();
	}

}

void CMagicTrick::ProcessMessage()
{
  int bMatched=0;
  int SelectedValue;
  char temp[256];
  for(int i=0;i<4;i++)
  {
	for(int j=0;j<4;j++)
	{
		if (m_aMatrix[m_iSelected1][i] == m_aMatrix[m_iSelected2][j])
		{
			if(bMatched)
			{
				//Bad magician!
				bMatched=2;
				break;
			}
			bMatched=1;
			SelectedValue=m_aMatrix[m_iSelected1][i];
		}
	}
  }
  switch(bMatched)
  {
  case 0: sprintf(temp,"Case #%d: Volunteer cheated!\n",m_iCaseNumber++);
		  m_oOutput.Writer(temp);
		  break;
  case 1: sprintf(temp,"Case #%d: %d\n",m_iCaseNumber++,SelectedValue);
		  m_oOutput.Writer(temp);
		  break;
  case 2: sprintf(temp,"Case #%d: Bad magician!\n",m_iCaseNumber++);
		  m_oOutput.Writer(temp);
		  break;
  }

}

