#include<iostream>
#include<fstream>
using namespace std;

ifstream in("text.txt");
ofstream out("result.txt");
enum Outcomes {Xwon , Owon ,Draw ,Incomplete };
class Case
{
	char t[4][4]; //tic tac toe 
	 Outcomes r;
public:
	void set()
	{ 
		
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in>>t[i][j];
			}
		}
	}

	void check();
	void show();
};
void Case::check()
{
	int flagc=0;
	int dotCount=0;
	int flagr=0;		//flag of rows
	char ch;
	//first row checks
	for (int i = 0; i < 4; i++)
	{
		int j = 1;
		flagr=0;
		ch=t[i][0];
		if(ch=='.')
		{
			dotCount++;
			break;
		}
		else if(ch=='T')
		{
			ch=t[i][j++];
			flagr++;
		}
		for (; j < 4; j++)
		{
			if(t[i][j]=='.')
			{
				dotCount++;
				break;
			}
			
			else if( (t[i][j]==ch)||(t[i][j]=='T') )
			{
				flagr++;
			}
		}
		if(flagr==3)
		{
			if(ch=='O')	
				r=Owon;
			else if(ch=='X')
				r=Xwon;
			break;
		}
	}
	//////////////////column check
	if(flagr!=3)
	{
		int i = 1;
		
		for (int j = 0; j < 4; j++)
		{
			flagc=0;
			ch=t[0][j];
			if(ch=='.')
			{
				dotCount++;
				break;
			}
			else if(ch=='T')
			{
				flagc++;
				ch=t[i++][j];
			}

			for (	; i < 4; i++)
			{
				if(t[i][j]=='.')
				{
					dotCount++;
					break;
				}
				
				else if( (t[i][j]==ch) || (t[i][j]=='T'))
				{
					flagc++;
				}	
			}
		
			if(flagc==3)
			{
			if(ch=='O')
				r=Owon;
			else if(ch=='X')
				r=Xwon;
			break;
			}
		}
			if(flagc!=3)
			{
				///////////////flag diagonal
				int i = 0;
				int flagd=0;
				ch=t[i][i];
					if(ch=='.')
					{
						dotCount++;
						i=5;
					}
					else if(ch=='T')
					{
						i++;
						ch=t[i][i];
						flagd++;
					}
				for (++i; i < 4; i++)
				{
					if(t[i][i]=='.')
					{
						dotCount++;
						break;
					}
			
					else if( (t[i][i]==ch)||(t[i][i]=='T') )
					{
						flagd++;
					}
				}
				/////////////right diagonal
				if(flagd!=3)
				{
					 i = 3;
					 flagd=0;
					ch=t[3-i][i];
					if(ch=='.')
					{
						dotCount++;
						i=0;
					}
					else if(ch=='T')
					{
						i--;
						ch=t[3-i][i];
						flagd++;
					}
					for (--i; i >=0; i--)
					{
						if(t[3-i][i]=='.')
						{
							dotCount++;
							break;
						}
			
						else if( (t[3-i][i]==ch)||(t[3-i][i]=='T') )
						{
							flagd++;
						}
					}
				}

				if(flagd==3)
				{
					if(ch=='O')
						r=Owon;
					else if(ch=='X')
						r=Xwon;
					
				}
				else if(dotCount==0)
					r=Draw;
				else
					r=Incomplete;
					
				
			}
		}
	}
	


void Case :: show()
{
	
	switch(r){
		case Xwon: out<<"X won";	break;
		case Owon: out<<"O won";	break;
		case Incomplete: out<<"Game has not completed";	break;
		case Draw: out<<"Draw";	break;
	}

}
void main()
{
	Case cArr[10];
	int noc;
	in>>noc;
	for (int i = 0; i < noc; i++)
	{
		cArr[i].set();
		
	}
	for (int i = 0; i < noc; i++)
	{
		cArr[i].check();
	}
	for (int i = 0; i < noc; i++)
	{
		out<<endl<<"Case  #"<<i+1<<":  ";
		cArr[i].show();
	}
}