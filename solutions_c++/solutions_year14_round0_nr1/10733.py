#include<iostream>
#include<fstream>
using namespace std;

bool Unique( int matrix[][4],int number,int till )
{
	for ( int i = 0; i< till ;i++ )
	{
		for ( int  j= 0; j < 4 ; j ++ )
		{
			if ( matrix[i][j] == number )
			{
				return false;
			}
		}
	}

	return true;
}
int magicianCheck( int matrix1[][4],int matrix2[][4],int answer1,int answer2 , int caseno)
{
	fstream fin,fout;
	fout.open("output.txt",ios::out|ios::app);
	int test1[4];
	int test2[4];
	int counter = 0;
		for ( int j = 0; j < 4 ; j++ )
		{
			test1[j] = matrix1[answer1-1][j];
			//cout<<test1[j];
		}
			//cout<<endl;
		for ( int j = 0; j < 4 ; j++ )
		{
			test2[j] = matrix2[answer2-1][j];
			//cout<<test2[j];
		}
		int value = 0;

		for ( int i = 0; i< 4; i++ )
		{
			for ( int j = 0; j < 4 ; j++ )
			{ 
				if ( test1[i] == test2[j] )
				{
					value = test1[i];
					counter++;
				}

			}
		}
		if ( counter == 1 )
		{
			fout<<"Case #"<<caseno<<": "<<value<<endl;
		}
		if ( counter > 1 )
		{
			fout<<"Case #"<<caseno<<": "<<"Bad magician!"<<endl;
		}
		if ( counter == 0 )
		{
			fout<<"Case #"<<caseno<<": "<<"Volunteer cheated!"<<endl;
		}
return 0;
		

}

int main()
{
	int testcases,answer1,answer2;
	int counterr = 0;
	int value =0 ;
	int matrix1[4][4],matrix2[4][4];
	fstream fin,fout;
	fin.open("A-small-attempt0.in",ios::in);
	fout.open("output.txt",ios::out);
	int currentT = 1;

	if ( !fin )
	{
		cout<<" file not found"<<endl;
	}
	else
	{
		fin>>testcases;

		//cout<<testcases<<endl;
		if ( testcases >=1 && testcases <= 100 )
		{
		 while( currentT <= testcases )
		 {
		 
			fin>>answer1;
			if ( answer1 >=1 && answer1<=4 )
			{
				for ( int i = 0; i< 4; i++ )
				{
					for ( int j = 0; j<4 ; j++ )
					{
						fin>> value;
						if ( value >=1 && value <=16 )
						{
							if (Unique( matrix1,value ,i))
							{
								matrix1[i][j] = value;
							}
							else
							{
								cout<<"not a unique value"<<endl;
							}
							
						}
					}
				}
							fin>>answer2;
							if ( answer2 >=1 && answer2<=4 )
							{
                                for ( int i = 0; i< 4; i++ )
								{
									for ( int j = 0; j<4 ; j++ )
									{
										fin>> value;
										if ( value >=1 && value <=16 )
										{
											if (Unique( matrix2,value,i ))
											{
												matrix2[i][j] = value;
											}
											else
											{
												cout<<"not a unique value"<<endl;
											}
	
										}
									}
								}
							}

    counterr = magicianCheck( matrix1, matrix2,answer1,answer2,currentT );
			}
			currentT++;
		 }



	
		}
		
	}


   	 




	fin.close();
	fout.close();

	return 0;
}