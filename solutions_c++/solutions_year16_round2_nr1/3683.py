#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main()
{
	ifstream fin;
	fin.open("A.txt");
	ofstream fout;
	fout.open("Aout.txt");
	int N;
	int letter[26];
	string result;
	fin >> N;
	string dummy;
	getline(fin,dummy);
	string HINT;
	for (int i=1;i<=N;i++)
	{
		bool complete = false;
	    for (int j=0;j<26;j++)
			letter[j]=0;
		fout << "Case #" << i << ": ";
		getline(fin,HINT);
		for (int j=0;j<HINT.length();j++)
			letter[HINT[j]-'A']++;		
			while(letter[13]>1 && letter[8]>0 && letter[4]>0)
			{result+="9";letter[13]-=2;letter[8]--;letter[4]--;}		
			while(letter[4]>0 && letter[8]>0 && letter[6]>0 && letter[7]>0 && letter[19]>0)
			{result+="8";letter[4]--;letter[8]--;letter[6]--;letter[7]--;letter[19]--;}		
			while(letter[18]>0 && letter[4]>1 && letter[21]>0 && letter[13]>0)
			{result+="7";letter[18]--;letter[4]-=2;letter[13]--;letter[21]--;}		
			while(letter[18]>0 && letter[8]>0 && letter[23]>0)
			{result+="6";letter[18]--;letter[8]--;letter[23]--;}
			while(letter[5]>0 && letter[8]>0 && letter[21]>0 && letter[4]>0)
			{result+="5";letter[5]--;letter[8]--;letter[21]--;letter[4]--;}
			while(letter[5]>0 && letter[14]>0 && letter[20]>0 && letter[17]>0)
			{result+="4";letter[5]--;letter[14]--;letter[20]--;letter[17]--;}	
			while(letter[19]>0 && letter[7]>0 && letter[17]>0 && letter[4]>1)
			{result+="3";letter[19]--;letter[7]--;letter[17]--;letter[4]-=2;}
			while(letter[19]>0 && letter[22]>0 && letter[14]>0)
			{result+="2";letter[19]--;letter[22]--;letter[14]--;}
			while(letter[13]>0 && letter[14]>0 && letter[4]>0)
			{result+="1";letter[13]--;letter[14]--;letter[4]--;}
			while(letter[25]>0 && letter[4]>0 && letter[17]>0 && letter[14]>0)
			{result+="0";letter[25]--;letter[4]--;letter[17]--;letter[14]--;}
        for (int j=0;j<26;j++)
			if (letter[j]!=0)
		{
		    result.clear();
		    for (int j=0;j<26;j++)
			letter[j]=0;
		    for (int j=0;j<HINT.length();j++)
			letter[HINT[j]-'A']++;		
		while(letter[25]>0 && letter[4]>0 && letter[17]>0 && letter[14]>0)
			{fout << "0";letter[25]--;letter[4]--;letter[17]--;letter[14]--;}
		while(letter[13]>0 && letter[14]>0 && letter[4]>0)
			{fout << "1";letter[13]--;letter[14]--;letter[4]--;}
		while(letter[19]>0 && letter[22]>0 && letter[14]>0)
			{fout << "2";letter[19]--;letter[22]--;letter[14]--;}
		while(letter[19]>0 && letter[7]>0 && letter[17]>0 && letter[4]>1)
			{fout << "3";letter[19]--;letter[7]--;letter[17]--;letter[4]-=2;}
		while(letter[5]>0 && letter[14]>0 && letter[20]>0 && letter[17]>0)
			{fout << "4";letter[5]--;letter[14]--;letter[20]--;letter[17]--;}
		while(letter[5]>0 && letter[8]>0 && letter[21]>0 && letter[4]>0)
			{fout << "5";letter[5]--;letter[8]--;letter[21]--;letter[4]--;}
		while(letter[18]>0 && letter[8]>0 && letter[23]>0)
			{fout << "6";letter[18]--;letter[8]--;letter[23]--;}
		while(letter[18]>0 && letter[4]>1 && letter[21]>0 && letter[13]>0)
			{fout << "7";letter[18]--;letter[4]-=2;letter[13]--;letter[21]--;}
		while(letter[4]>0 && letter[8]>0 && letter[6]>0 && letter[7]>0 && letter[19]>0)
			{fout << "8";letter[4]--;letter[8]--;letter[6]--;letter[7]--;letter[19]--;}
		while(letter[13]>1 && letter[8]>0 && letter[4]>0)
			{fout << "9";letter[13]-=2;letter[8]--;letter[4]--;}
			complete = true;
			break;
		}
		
		if (!complete)
        {for (int j=result.length();j>=1;j--)
			fout << result[j-1];}
		if(i!=N) fout << endl;
		result.clear();
	}
	fin.close();
	fout.close();
	return 0;
}


