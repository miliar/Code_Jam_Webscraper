
#include "stdafx.h"
#include <vector>
#include <string>

using std::vector;
using std::string;

#pragma warning(disable : 4996)

// returns exp of the word
string Exp(string word)
{
	string ret = "";
	char act = word[0];
	ret+= word[0];
	for(int i=1;i<word.length();i++)
		if(word[i]!=act)
		{
			ret+=word[i];
			act=word[i];
		}
	return ret;
}

// return true if word fits the expression
bool CheckWord(string word, string exp) // word to check, expression
{
	if(Exp(word) == exp) return true;
	return false;
}

vector<int> CountExp(string word)
{
	vector<int> exp = vector<int>();
	char act = word[0];
	int act_count = 1;
	for(int i=1;i<word.length();i++)
		if(word[i]!=act)
		{
			exp.push_back(act_count);
			act_count=1;
			act=word[i];
		}
		else act_count++;
	exp.push_back(act_count);
	return exp;
}

int CountMoves(string word, string word_dest)
{
	int count = 0;
	vector<int> exp1 = CountExp(word);
	vector<int> exp2 = CountExp(word_dest);

	for(int i=0;i<exp1.size();i++)
	{
		int act_count = exp1[i]-exp2[i];
		if(act_count<0) act_count*=-1;
		count+=act_count;
	}
	return count;
}

int CountMovesList(vector<string> list, int index)
{
	string word = list[index];
	int count=0;
	for(int i=0;i<list.size();i++)
	{
		if(i==index) continue;
		count+=CountMoves(list[i],list[index]);
	}
	return count;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int case_num,moves,words;
	vector<string> word_list = vector<string>();
	FILE* in = fopen("data.in","r");
	FILE* out = fopen("data.out","w");

	fscanf(in,"%d",&case_num);
	for(int i=0; i<case_num;i++)
	{
		word_list.clear();
		moves=-1;
		fscanf(in,"%d",&words);
		for(int s=0;s<words;s++)
		{
			char buff[101];
			fscanf(in,"%s",&buff);
			word_list.push_back(buff);
		}
		moves=0;
		for(int s=1;s<words;s++)
		{
			if(word_list[s]!=word_list[0])
			{
				moves=-1; // words are not identical yet
				break;
			}
		}
		if(moves==0) 
		{
			fprintf(out,"Case #%d: 0\n",i+1);
			continue;
		}
		
		moves=0;
		for(int s=1;s<words;s++)
		{
			if(CheckWord(word_list[s],Exp(word_list[0]))==false)
			{
				moves=-1; // words are not identical yet
				break;
			}
		}
		if(moves==-1) 
		{
			fprintf(out,"Case #%d: Fegla Won\n",i+1);
			continue;
		}
		
		// it is possible to find solution
		moves=CountMovesList(word_list,0);
		for(int s=1;s<words;s++)
		{
			int act_moves = CountMovesList(word_list,s);
			if(act_moves<moves) moves=act_moves;
		}
		
		word_list.push_back(Exp(word_list[0]));
		int act_moves = CountMovesList(word_list,word_list.size()-1);
		if(act_moves<moves) moves=act_moves;
		fprintf(out,"Case #%d: %d\n",i+1,moves);
	}

	fclose(in);
	fclose(out);
	return 0;
}

