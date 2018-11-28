#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream ifile("input.txt");
	ofstream ofile("output.txt");
	int T;
	char A[4][4];
	char ch;
	char num,num1,num2;
	int win=0;
	bool bv, bg, bd1,bd2 , won, tochka;
	ifile>>T;
	for(int l=1;l<=T;l++)
	{
		tochka = false;
		for(int i=0; i<4;i++)
		{
			for(int k=0; k<4; k++)
			{
				ifile>>ch;
				/*switch(ch)
				{
				case 'X': A[i][k]=1; break;
				case 'O': A[i][k]=2; break;
				case '.': A[i][k]=0; tochka=true; break;
				case 'T': A[i][k]=3; break;
				}*/
				if(ch=='.')
					tochka=true;
				A[i][k]=ch;
				//cout<<ch;
			}
			//cout<<"\n";
		}
		//cout<<"\n";
	/*	for(int i=0; i<4; i++){
			for(int k=0; k<4; k++)
			{cout<<A[i][k]<<' ';
			}
			cout<<"\n";
		}
		cout<<"\n";
	*/	
		if(A[0][0]!='T')
			num1=A[0][0];
		else
			num1=A[1][1];
		if(A[3][0]!='T')
			num2=A[3][0];
		else
			num2=A[2][1];
		if(num1!='.')
			bd1=true;
		else
			bd1=false;
		if(num2!='.')
			bd2=true;
		else
			bd2=false;
		won=false;
		for(int i=0; i<4; i++)
		{
			if(bd1)
			{
					if(A[i][i]!=num1&&A[i][i]!='T')
					{bd1=false;}
			}
			if(bd2)
			{
				if(A[3-i][i]!=num2&&A[3-i][i]!='T')
					{bd2=false;}

			}
				bv=true;
				bg=true;
			if(A[i][i]!='T')
			{	
				
				
				num=A[i][i];
				if(num!='.'){
				for(int k=0; k<4; k++)
				{
					if(bv)
					{
						if(A[i][k]!=num && A[i][k]!='T')
						{bv=false;}
					}
					if(bg)
					{
						if(A[k][i]!=num && A[k][i]!='T')
						{bg=false;}
					}
				}
				if(bv || bg)
				{won=true;bd1=false;bd2=false;
				break;}
				}
				else
				{
					bv=false;
					bg=false;
				}
			}
			else //A[i][i]=='T'
			{
				if(A[i][0]!='T')
				{
					if(A[i][0]!='.')
						num=A[i][0];
					else
						bv=false;
				}
				else
				{
					if(A[i][1]!='.')
						num=A[i][1];
					else
						bv=false;
				}
				if(bv)
				for(int k=0; k<4; k++)
					if(A[i][k]!=num && A[i][k]!='T')
					{bv=false;
					break;
					}
					
				if(!bv)
				{
				
				if(A[0][i]!='T')
				{
					if(A[0][i]!='.')
						num=A[0][i];
					else
						bg=false;
				}
				else
				{
					if(A[1][i]!='.')
						num=A[1][i];
					else
						bg=false;
				}
				if(bg)
				for(int k=0; k<4; k++)
					if(A[k][i]!=num && A[k][i]!='T')
					{bg=false;
					break;
					}
					
				
				
				}

				if(bv || bg)
				{won=true;bd1=false;bd2=false;
				break;}
				


			}
			if(won)
				break;
		}
		if(bv || bg)
			ofile<<"Case #"<<l<<": "<<num<<" won"<<"\n";
		else if(bd1)
			ofile<<"Case #"<<l<<": "<<num1<<" won"<<"\n";
		else if(bd2)
			ofile<<"Case #"<<l<<": "<<num2<<" won"<<"\n";
		else if(tochka)
			ofile<<"Case #"<<l<<": "<<"Game has not completed"<<"\n";
		else
			ofile<<"Case #"<<l<<": "<<"Draw"<<"\n";
	//	cout<<"\n";


	}
}