#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <GoogleCodeJam.h>
GoogleCodeJam::GoogleCodeJam(const char* InputFile)
{
	m_FP = fopen(InputFile, "r");
	if (NULL == m_FP)
	{
		printf("File Failed to Open\n");
		exit(EXIT_FAILURE);
	}
	m_OutFP = fopen("output/results.txt", "w");
	if (NULL == m_OutFP)
	{
		printf("Output File Failed to Open\n");
		exit(EXIT_FAILURE);
	}
}

GoogleCodeJam::~GoogleCodeJam()
{
	fclose(m_FP);
	fclose(m_OutFP);

}

bool GoogleCodeJam::Print_Line()
{
	char Buffer[255];
	if (fgets(Buffer, 255, m_FP)== NULL){
		return false;
	}
	printf("%s", Buffer);
	return true;
}

uint32_t GoogleCodeJam::Get_Line_Int()
{
	char Buffer[255];
	uint32_t Ret;
	if (fgets(Buffer, 255, m_FP)== NULL){
		return false;
	}
	sscanf(Buffer, "%d", &Ret);
	return Ret;
}

uint32_t* GoogleCodeJam::Get_Line_Int_Array(uint32_t NumValues)
{
	uint32_t *Ret = new uint32_t[NumValues];
	
	for (uint32_t i = 0; i < NumValues; i++)
	{
		fscanf(m_FP,"%u ", &(Ret[i]));
	}
	return Ret;
}

uint32_t GoogleCodeJam::Get_Int()
{
	uint32_t Ret;
	fscanf(m_FP,"%u ", &(Ret));

	return Ret;
}

uint8_t* GoogleCodeJam::Get_Byte_Array(uint32_t NumValues)
{
	uint8_t *Ret = new uint8_t[NumValues];
	for (uint32_t i = 0; i < NumValues; i++)
	{
		fscanf(m_FP,"%c ", &(Ret[i]));
		Ret[i] += -48;
	}
	return Ret;
}


uint32_t* GoogleCodeJam::Output_Results(uint32_t Case, uint32_t* Values, uint32_t NumValues)
{
	fprintf(m_OutFP, "Case #%u:", Case);
	for (uint32_t i = 0; i < NumValues; i++)
	{
		fprintf(m_OutFP, " %u", Values[i]);
	}
	
	fprintf(m_OutFP, "\n", Values);


}