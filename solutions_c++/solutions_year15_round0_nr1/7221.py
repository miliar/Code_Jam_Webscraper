#include<stdio.h>
#include<conio.h>
#include<string.h>
#include <stdlib.h>
class Data
{
public:
	char* line;
	int m_maxShy;
	char* m_numShy;
	int* m_numShyArray;
	Data* m_next;
};
void Parse(Data* a_data)
{
	int length = strlen(a_data->m_numShy);
	a_data->m_numShyArray = new int[length];
	for(int i=0;i<length;i++)
	{
		char val = a_data->m_numShy[i];
		a_data->m_numShyArray[i] = atoi((const char*)&val);
	}
}
Data* InputParse()
{
	int m_testCases;
	scanf("%d", &m_testCases);
	if(m_testCases<=0)
		return 0;
	Data * head = new Data();
	Data* start = head;
	for(int i=0;i<m_testCases;i++)
	{
		if( i!=0)
		{
			start->m_next = new Data();
			start =start->m_next;
		}
		start->line = new char[2000];
		scanf("%d %s",&start->m_maxShy,start->line);
		start->m_numShy = new char[start->m_maxShy+1];
		strcpy(start->m_numShy,start->line);
		delete start->line;
		Parse(start);

	}
	
	 return head;
}
int Find(Data* a_data)
{
	int numFriends = 0;
	int currentNumAudience = 0;
	for(int i=0;i<=a_data->m_maxShy;i++)
	{
		if(i>currentNumAudience)
		{
			int diff = i - currentNumAudience;
			numFriends += diff;
			currentNumAudience += diff;
		}
		currentNumAudience+=a_data->m_numShyArray[i];
	}
	return numFriends;
}
void main()
{
	
	Data* data = InputParse();
	Data* start = data;
	if(data==0)
		return;
	int prob = 1;
	//FILE* resultFile = fopen("D:\\code jam\\file.txt\0","w");
	while(data != 0 )
	{
		printf("Case #%d: %d\n", prob, Find(data));
		prob++;
		data = data->m_next;
	}
	//fclose(resultFile);
	//getch();
}