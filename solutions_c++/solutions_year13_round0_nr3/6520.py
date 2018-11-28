#include <iostream>
#include <vector>
#include <map>
#include <hash_set>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <hash_map>

using namespace std;
/*
int codejamsomecode()
{
	ofstream myfile ("output.txt");
	ifstream myfil ("A-large-practice.in");

if(myfile.is_open() && myfil.is_open()){
	int N=0;				//num of testcases
while(myfil.good()){

	
	myfil >> N;

	for(int i=0; i<N; i++)
	{
		int C=0;
		int l=0;			//num of items
		int *P;
		myfil >> C;
		myfil >> l;
		P= new int[l];
		for(int j=0; j<l; j++)
		{
			myfil >> P[j];
			if(j!=0){
				for(int k=j-1; k>=0; k--){
					int add=0;
					add= P[j]+P[k];
					if(add==C){
						myfile << "Case #"<<i+1<<": "<<k+1<<" "<<j+1<<endl;
					}
				}
			}
		}
	}

	myfil.close();
	myfile.close();
}
}
return 0;
}

int second()
{
	ofstream myfile ("output1.txt");
	ifstream myfil ("question.txt");

	if(myfile.is_open() && myfil.is_open()){

		int T=0;										//num of testcases
		while(myfil.good()){
			
			myfil >> T;

			for(int a=0; a<T; a++)
			{
				string line;
				myfil >> line;

				//cout << line <<endl;
				int length=line.length();
				
				map<string,int> m;
				m["hello"]=23;
				if(m.find("hello")==m.begin)
					cout << "hello";

				for(int a=0; a<length; a++)
				{	
					
					
				}
			}
		}
	}
	system("pause");
	return 0;
}



int tictaktomek()
{
	
	ifstream myfil ("A-large.in");
	ofstream myfile ("output.txt");

	if(myfile.is_open() && myfil.is_open()){

		int T=0;										//num of testcases
		//while(myfile.good()){
			
			int i,j=0;
			myfil >> T;

			for(int test=0; test<T; test++)
			{
				char arr[4][4];
				int diag=0,diag1=0;
				int ver[4]={0,0,0,0};
				int draw=1;
				int incom=0;
				int lines=0;
				string line[4];
				
				myfile << "Case #"<<test+1<<": ";

				for(lines=0; lines<4; lines++)
					myfil >> line[lines];

				for( i=0; i<4; i++)
				{
					int hor=0;				
				//cout << line <<endl;
					for( j=0; j<4; j++)
					{
						hor=hor+line[i][j];						//horizontal

						arr[i][j]=line[i][j];
						//cout << arr[i][j];


					}
					for(int k=0; k<4; k++)
						ver[k]=ver[k]+arr[i][k];

						if(ver[i]==321 || ver[i]==316 ){
						myfile << "O won" <<endl;
						draw=0;
						break;
						}

						if(ver[i]==352 || ver[i]==348 )
						{
							myfile << "X won" <<endl;
							draw=0;
							break;
						}
					

					diag1=diag1+arr[i][3-i];
					diag=diag+arr[i][i];

					if(hor==321 || hor==316){
						myfile << "O won" <<endl;
						draw=0;
						break;
					}
					if(hor==352 || hor==348)
					{
						myfile << "X won" <<endl;
						draw=0;
						break;
					}
					//cout <<endl;
				}
				

				if(diag==321 || diag==316 || diag1==321 || diag1==316){
					myfile << "O won" <<endl;
					continue;
				}
				if(diag==352 || diag==348 || diag1==352 || diag1==348)
				{
					myfile << "X won" <<endl;
					continue;
				}

				for(int a=0;a<4; a++)
				{
					
					if(ver[a]<316)
						incom=1;
				}
				
				if(draw==1 && incom==0)
					myfile << "Draw" << endl;
				else if(draw==1 && incom==1)
					myfile << "Game has not completed" <<endl;
			}	
		//}
	}
	system("pause");
	return 0;
}
*/

void main()
{
	ifstream myfil ("C-small-attempt0.in");
	ofstream myfile ("output1.txt");

	if(myfile.is_open() && myfil.is_open()){

		int T=0;										//num of testcases
		//while(myfile.good()){
			
		int i,j=0;
		myfil >> T;
		
		for(int test=0; test<T; test++)
		{
			int A=0,B=0,y=0;
			myfil >> A;
			myfil >> B;

			for(int count=A; count <=B; count++)
			{
				if(count==1 || count==4 || count==9 || count==121 || count==484)
					y++;

			}
			myfile << "Case #"<<test+1<<": "<<y<<endl;
		}
	}
}