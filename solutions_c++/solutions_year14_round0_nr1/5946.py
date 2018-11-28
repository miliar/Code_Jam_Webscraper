// GJam_2014_1.cpp : définit le point d'entrée pour l'application console.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

fstream answer_file;

void solve( int row1, int arg1[16], int row2, int arg2[16] )
{
	// the possible values :
	vector<int> possib1;
	vector<int> possib2;

	for( int i=0; i< 4; i++ )
	{
		possib1.push_back( arg1[i+row1*4] );
		possib2.push_back( arg2[i+row2*4] );
	}

	// union of the two vectors
	std::sort (possib1.begin(), possib1.end());
    std::sort (possib2.begin(), possib2.end());

	std::vector<int> v(8);
    std::vector<int>::iterator it;

    it=std::set_intersection(possib1.begin(), possib1.end(), possib2.begin(), possib2.end(), v.begin());                              
    v.resize(it-v.begin());                    

	if( v.size() == 1 )
	{
		answer_file <<v[0]<<endl;
		cout<<v[0]<<endl;
	}
	else
	{
		if( v.size() > 1 )
		{
			answer_file <<"Bad magician!"<<endl;
			cout<<"Bad magician!"<<endl;
		}
		else
		{
			answer_file <<"Volunteer cheated!"<<endl;
			cout<<"Volunteer cheated!"<<endl;
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	answer_file.open( "answer.txt", std::ios_base::out );
	
	// read the input
	std::fstream myfile("input.txt", std::ios_base::in);

    int nb_input;
    myfile >> nb_input;

	for( int input = 0; input < nb_input; input++ )
	{
		int answer1 = 0;
		int arrang1[16];
		myfile >> answer1;
		answer1--; // [1;4]
		for( int i=0; i< 16; i++ )
		{
			myfile >> arrang1[i];
		}

		int answer2 = 0;
		int arrang2[16];
		myfile >> answer2;
		answer2--; // [1;4]
		for( int i=0; i< 16; i++ )
		{
			myfile >> arrang2[i];
		}

		answer_file <<"Case #"<<input+1<<": "; 
		cout<<"Case #"<<input+1<<": "; 
		solve( answer1, arrang1, answer2, arrang2 );
	}

	system("pause");
	return 0;
}

