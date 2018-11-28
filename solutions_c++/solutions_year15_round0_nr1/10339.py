// GCJ.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <iostream>





using namespace std;

char foo[1000][1000];
int iFreunde[1000];
int counter = 0;
int iT;

void einlesen()
	{
	fstream nei;
	char blubb[1000];
	string s;

	nei.open("A-small-attempt2.in", ios::in);
	
	getline(nei, s);
	iT=atoi(s.c_str());
	
	for(int i=0; i<iT;i++)
		{
		nei.getline(blubb, sizeof(blubb));
		for (int x=0; x<sizeof(blubb);x++)
			{
				foo[i][x]=blubb[x];

			}
		}

	nei.close();
	}

void ausgeben ()
	{

	string nausdamit;
	char buffer[1000];
	fstream naus;
	naus.open("out.txt", ios::out);
	for (int i=0; i<iT; i++)
	{	
		
		nausdamit=itoa(iFreunde[i], buffer, 10);
		naus<<"Case #"<<i+1<<": "<<nausdamit<<"\n";
	}
	}

void ladeFreundeEin(){
	int iMaxShy[1000];
	int iRest[100];
	char buffer[1000];
	int iLeute;
	int iFreund;
	string s;
	string foo2;
	size_t pos;
	
	for (int i=0; i<=iT; i++){
	iMaxShy[i]=foo[i][0] - '0';	
		
		if(iMaxShy[i]==0)
			{
				iFreunde[i]=0;
			}
		else{
			
			for(int a=0; a<100; a++){
				iRest[a]=0;
				}
			iLeute=0;
			iFreund=0;
			for (int x=2;x<=(iMaxShy[i]+2);x++)
				{
				iRest[x-2]=foo[i][x] - '0';
				iLeute=iRest[x-2]+iLeute;
				if ((x-1)>iLeute)
					{
						iFreund++;
						iLeute++;
					}
					
				}
				if (iLeute<iMaxShy[i])
					{
					iFreund = iMaxShy[i]-iLeute;
					}
			iFreunde[i]=iFreund;
			


			}
		}

	}

int main()
{
string blub;
einlesen();
ladeFreundeEin();
ausgeben();
system("pause");
return 0;
}






