#include<iostream>
using namespace std;
void main()
{
	long T;
	long m = 1;
	cin>>T;
	while(T--)
	{
		long e = m;
		char arr[4][4];
			for(int i = 0; i<4; i++)
				for(int j = 0; j<4; j++)
					cin>>arr[i][j];
			int d =0;
	    for(int i = 0; i< 4; i++)//rows
		{
			int countx = 0;
			for(int j = 0; j<4; j++)
			{
					if( arr[i][j] == 'X' || arr[i][j] =='T')
					{
						countx++;
						if(countx == 4)
						{
							cout<<"Case #"<<m<<": "<<"X won"<<endl;
						    m++;
							d++;
						}
					}
			}
			
		}
		if(d==1)
			goto next;
		 for(int j = 0; j< 4; j++)//columns
		{
			int countx = 0;
			for(int i = 0; i<4; i++)
			{
					if( arr[i][j] == 'X' || arr[i][j] =='T')
					{
						countx++;
						if(countx == 4)
						{
							cout<<"Case #"<<m<<": "<<"X won"<<endl;
						    m++;
							d++;
						}
					}
			}
			
		}
		 if(d==1)
			 goto next;
		 int p = 0; // X diagnol
		  for(int i = 0; i< 4; i++)
			{
			
		
					if( arr[i][i] == 'X' || arr[i][i] =='T')
					{
						p++;
						if(p == 4)
						{
							cout<<"Case #"<<m<<": "<<"X won"<<endl;
						    m++;
							d++;
						}
					}
						
			}
		  if(d==1)
			goto next;

		  // opp diagnol
	    
					if( arr[0][3] == 'X' || arr[0][3] =='T')
					{
						if( arr[1][2] == 'X' || arr[1][2] =='T')
						{
							if( arr[2][1] == 'X' || arr[2][1] =='T')
							{
								if( arr[3][0] == 'X' || arr[3][0] =='T')
						
									{	
										cout<<"Case #"<<m<<": "<<"X won"<<endl;
										 m++;
										 
								}
							}
						}
					}
next:
					;
				
		// O WON
					int f = 0;
	     for(int i = 0; i< 4; i++)//rows
		{
			int countx = 0;
			for(int j = 0; j<4; j++)
			{
					if( arr[i][j] == 'O' || arr[i][j] =='T')
					{
						countx++;
						if(countx == 4)
						{
							cout<<"Case #"<<m<<": "<<"O won"<<endl;
						    m++;
							f++;
						}
					}
			}
			
		}
		 if(f==1)
			goto nex;

		 for(int j = 0; j< 4; j++)//columns
		{
			int countx = 0;
			for(int i = 0; i<4; i++)
			{
					if( arr[i][j] == 'O' || arr[i][j] =='T')
					{
						countx++;
						if(countx == 4)
						{
							cout<<"Case #"<<m<<": "<<"O won"<<endl;
						    m++;
							f++;
						}
					}
			}
			
		}
		 if(f==1)
			goto nex;

		 int q = 0; // X diagnol
		  for(int i = 0; i< 4; i++)
			{
			
		
					if( arr[i][i] == 'O' || arr[i][i] =='T')
					{
						q++;
						if(q == 4)
						{
							cout<<"Case #"<<m<<": "<<"O won"<<endl;
						    m++;
							f++;
						}
					}
						
			}
		  if(f==1)
			goto nex;

		  // opp diagnol
	    
					if( arr[0][3] == 'O' || arr[0][3] =='T')
					{
						if( arr[1][2] == 'O' || arr[1][2] =='T')
						{
							if( arr[2][1] == 'O' || arr[2][1] =='T')
							{
								if( arr[3][0] == 'O' || arr[3][0] =='T')
						
								{	
										cout<<"Case #"<<m<<": "<<"O won"<<endl;
										 m++;
								}
																
									 



							}

						}
					}
nex:
					;
					
					if(e==m)
					{
						int w = 0;
						
								for(int i = 0; i< 4; i++)//rows
									{
			
										for(int j = 0; j<4; j++)
										{
											if( arr[i][j] == '.')
												{
						
													cout<<"Case #"<<m<<": "<<"Game has not completed"<<""<<endl;
												    m++;
													w++;
						
												}
											if(w == 1)
											break;
											
										}
										if(w == 1)
											break;

			
									}
								if(w==0)
							{
								cout<<"Case #"<<m<<": "<<"Draw"<<endl;
										 m++;
							}

						}
							
							
						
	
		
	
		

	}

}