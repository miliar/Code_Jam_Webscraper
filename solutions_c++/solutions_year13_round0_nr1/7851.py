#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<algorithm>

using namespace std;

bool checkRow(char *,int,char);
bool checkColumn(char *,int,char);
bool checkLeftDiagonal(char *,char);
bool checkRightDiagonal(char *,char);
	
int main()
	{
		int testCases;
		scanf("%d",&testCases);
			
		for(int k=0;k<testCases;k++)
			{	
		
				char board[16];
				bool dot=false;
				for (int i=0;i<4;i++)
					{
						for (int j=0;j<4;j++)
							{
								cin>>board[(i*4)+j];
								if( !dot && board[(i*4)+j]=='.')
									{
										dot=true;
									}
								
							}
								
					}
				
				bool Xoccurence,Yoccurence,gameOver=false,space;
				//Checking for Row
				for (int i=0;i<4;i++)
	
					{
						space=checkRow(board,i,'.');
						if(!space)
							{
								Xoccurence=checkRow(board,i,'X');
								Yoccurence=checkRow(board,i,'O');
										
								if( ( Xoccurence && !Yoccurence))
									{
										cout<<"Case #"<<k+1<<": "<<"X won"<<endl;
										gameOver=true;
										break;
									}
								if (  !Xoccurence && Yoccurence )
									{
										cout<<"Case #"<<k+1<<": "<<"O won"<<endl;
										gameOver=true;
										break;
									} 
							}
							
					}

				//Checking for Column
				if(gameOver==false)
					{
						for (int i=0;i<4;i++)
							{
								space=checkColumn(board,i,'.');
								//cout<<!space;
								if(!space)
									{
										Xoccurence=checkColumn(board,i,'X');
										Yoccurence=checkColumn(board,i,'O');
										space=checkRow(board,i,'.');
										if( ( Xoccurence && !Yoccurence))
											{
												cout<<"Case #"<<k+1<<": "<<"X won"<<endl;
												gameOver=true;
												break;
											}
										if (  !Xoccurence && Yoccurence )
											{
												cout<<"Case #"<<k+1<<": "<<"O won"<<endl;
												gameOver=true;
												break;
											} 
									}
							}
					}

				//Checking for Diagonals
				if(gameOver==false)
					{
						space=checkLeftDiagonal(board,'.');
						if(!space)
							{						
		
								Xoccurence=checkLeftDiagonal(board,'X');
								Yoccurence=checkLeftDiagonal(board,'O');

								if( ( Xoccurence && !Yoccurence))
									{
										cout<<"Case #"<<k+1<<": "<<"X won"<<endl;
										gameOver=true;
									
									}
								if (  !Xoccurence && Yoccurence )
									{
										cout<<"Case #"<<k+1<<": "<<"O won"<<endl;
										gameOver=true;
									
									} 
							}
					}
				if(gameOver==false)
					{
						space=checkRightDiagonal(board,'.');
						if(!space)
							{						

								Xoccurence=checkRightDiagonal(board,'X');
								Yoccurence=checkRightDiagonal(board,'O');

								if( ( Xoccurence && !Yoccurence))
									{
										cout<<"Case #"<<k+1<<": "<<"X won"<<endl;
										gameOver=true;
								
									}
								if (  !Xoccurence && Yoccurence )
									{
										cout<<"Case #"<<k+1<<": "<<"O won"<<endl;
										gameOver=true;
									
									} 
							}
					}
						
				if( !gameOver && !dot)
						cout<<"Case #"<<k+1<<": "<<"Draw"<<endl;
					
				if( !gameOver && dot)
					cout<<"Case #"<<k+1<<": "<<"Game has not completed"<<endl;
				

		
	
			}

		return 0;
	}

bool checkRow(char *board,int row,char move)
	{
		for(int j=0;j<4;j++)
			{
				if(board[(row*4)+j]==move)
					{
						return true;
					}
			}
	}

bool checkColumn(char *board,int column,char move)
	{
		for(int i=0;i<4;i++)
			{
				if(board[(i*4)+column]==move)
					{
						return true;
					}
			}
	}

bool checkLeftDiagonal(char *board,char move)
	{
		//Checking left diagonal
		for(int i=0;i<4;i++)
			{
				if(board[(i*4)+i]==move)
					{
						return true;
					}
			}
	}

bool checkRightDiagonal(char *board,char move)
	{
		if( board[(0*4)+3]== move || board[(1*4)+2] == move || board[(2*4)+1]==move || board[(3*4)+0]==move)
			return true;
	}

			
