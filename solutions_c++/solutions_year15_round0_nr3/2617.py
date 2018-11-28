#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string>
#include <string.h>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <vector>
#include<algorithm>
#include <random>
#include<iomanip>


using namespace std;

char Matrix[5][5];
int sign[5][5];


int iton(char c)
{
	if (c=='1')
		return 1;
	if (c=='i')
		return 2;
	if (c=='j')
		return 3;
	if (c=='k')
		return 4;
}

int main()
{

	/*ifstream fin("input.txt");
	ofstream fout("output.txt");*/

	ifstream fin("C-small-attempt0.in");
	ofstream fout("output.out");

	Matrix[1][1]='1';
	Matrix[1][2]='i';
	Matrix[1][3]='j';
	Matrix[1][4]='k';
	Matrix[2][1]='i';
	Matrix[2][2]='1';
	Matrix[2][3]='k';
	Matrix[2][4]='j';
	Matrix[3][1]='j';
	Matrix[3][2]='k';
	Matrix[3][3]='1';
	Matrix[3][4]='i';
	Matrix[4][1]='k';
	Matrix[4][2]='j';
	Matrix[4][3]='i';
	Matrix[4][4]='1';

	sign[1][1]=1;
	sign[1][2]=1;
	sign[1][3]=1;
	sign[1][4]=1;
	sign[2][1]=1;
	sign[2][2]=-1;
	sign[2][3]=1;
	sign[2][4]=-1;
	sign[3][1]=1;
	sign[3][2]=-1;
	sign[3][3]=-1;
	sign[3][4]=1;
	sign[4][1]=1;
	sign[4][2]=1;
	sign[4][3]=-1;
	sign[4][4]=-1;
	


	int T;
	fin>>T;
	for (int cnt=1; cnt<=T; cnt++)
	{
		int L,X;
		fin>>L>>X;

		char *c= new char [L*X+1];
		string s;
		fin>>s;
		for (int i=0; i<X; i++)
			for (int j=0; j<s.length(); j++)
				c[j+L*i]=s[j];


		/*for (int i=0; i<L*X; i++)
			cout<<c[i];
		cout<<endl;*/

		vector<int> indexi;
		int temp_sign=1;
		char temp_result='1';
		for (int i=0; i<L*X; i++)
		{
			temp_sign=temp_sign*sign[iton(temp_result)][iton(c[i])];
			temp_result=Matrix[iton(temp_result)][iton(c[i])];
			//cout<<temp_result<<" "<<temp_sign<<endl;
			if (temp_sign==1 && temp_result=='i')
				indexi.push_back(i);
		}
		//cout<<"now is k"<<endl;

		vector<int> indexk;
		temp_sign=1;
		temp_result='1';
		for (int k=L*X-1; k>=0; k--)
		{
			temp_sign=temp_sign*sign[iton(c[k])][iton(temp_result)];
			temp_result=Matrix[iton(c[k])][iton(temp_result)];	
			//cout<<temp_result<<" "<<temp_sign<<endl;
			if (temp_sign==1 && temp_result=='k')
				indexk.push_back(k);
		}

		bool find=false;
		//cout<<"size="<<indexi.size()<<" "<<indexk.size()<<endl;
		//getchar();
		if (indexi.size()!=0 && indexk.size()!=0)
		{
			int temp_i=indexi.size()-1;
			for (int k=0; k<indexk.size(); k++)
			{
				if (temp_i >=0 && indexi[temp_i]>=indexk[k])
					temp_i--;
				if (temp_i>=0)
				{
					int temp_sign=1;
					char temp_result='1';
					for (int j=indexi[temp_i]+1; j<indexk[k]; j++)
					{
						temp_sign=temp_sign*sign[iton(temp_result)][iton(c[j])];
						temp_result=Matrix[iton(temp_result)][iton(c[j])];					
					}
					if (temp_sign==1 && temp_result=='j')
					{
						find=true;
						break;
					}
				}
			}
		}

		//cout<<find<<endl;
		if (find==false)
			fout<<"Case #"<<cnt<<": NO"<<endl;
		else
			fout<<"Case #"<<cnt<<": YES"<<endl;
	}




	



	system("pause");
}

