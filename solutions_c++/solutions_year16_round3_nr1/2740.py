// Filename: 
// Description: 
// Author: Latiful Kabir < siplukabir@gmail.com >
// Created: 
// URL: latifkabir.github.io

/*
Problem:

*/

#include<iostream>
#include<fstream>
#include<list>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;


void Evacuate(int *nMembers, int nParties)
{
    int maxParty=max_element(nMembers,nMembers+nParties)-nMembers;
    cout << char(char(maxParty+1)+'@');
    nMembers[maxParty]=nMembers[maxParty]-1;
}


int Sum(int *nMembers, int nParties)
{
    int sum=0;
    for (int i = 0; i < nParties; i++) 
	sum+=nMembers[i];

    return sum;    
}



int main(int argc, char *argv[])
{

    ifstream inFile("input.txt");
    if(!inFile)
    {
	cout << "Input file not found !" <<endl;
	return -1;
    }
    long nCases;

    inFile>>nCases;
    int nParties;
    int *nMembers;

    for (int i = 0; i < nCases; i++) 
    {
	inFile>>nParties;
	nMembers=new int[nParties];
	for (int j=0; j < nParties; j++) 
	    inFile>>nMembers[j];
	cout<<"Case #"<<i+1<<": ";
	int sum=Sum(nMembers,nParties);
	while(sum)
	{
	    Evacuate(nMembers,nParties);
	    sum=Sum(nMembers,nParties);

	    for(int k=0; k < nParties; k++)
	    {
		if(nMembers[k]>sum/2)
		{
		    Evacuate(nMembers,nParties);
		    sum=Sum(nMembers,nParties);
		}
	    }

	    cout << " ";	    
	}
	cout << endl;

    }

    inFile.close();
    return 0;
}

