#include <iostream>
using namespace std;

void GetInput();
int main()
{
	GetInput();
	return 0;
}

void GetInput()
{
	int tempCount = 0;
	bool solnFound=false;
	int count=0;
	int cases;
	char xORo[4][4];
	cin>>cases;
	for(int i=0;i<cases;i++)
	{
solnFound=false;
count=0;
tempCount=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>xORo[j][k];
				if(xORo[j][k]=='.')
				{
					count++;
				}
			}
		}
		//Evaluation logic here
		char temp;
		while(!solnFound && tempCount==0)
		{
			temp = xORo[0][0];
				if( (xORo[1][0]==temp || xORo[1][0]=='T') && (xORo[2][0]==temp || xORo[2][0]=='T') && (xORo[3][0]==temp || xORo[3][0]=='T') )
				{
					if(temp=='.')
						{count++;}
					else
					{
						cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
						solnFound=true;
						break;
					}
				}
				if( (xORo[1][1]==temp || xORo[1][1]=='T') && (xORo[2][2]==temp || xORo[2][2]=='T') && (xORo[3][3]==temp || xORo[3][3]=='T') )
				{
					if(temp=='.')
						{count++;}
					else{
						cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
						solnFound=true;
						break;}
				}
				if( (xORo[0][1]==temp || xORo[0][1]=='T') && (xORo[0][2]==temp || xORo[0][2]=='T') && (xORo[0][3]==temp || xORo[0][3]=='T') )
				{
					if(temp=='.')
						{count++;}
					else{
						cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
						solnFound=true;
						break;}
				}
			temp = xORo[1][0];
				if( (xORo[1][1]==temp || xORo[1][1]=='T') && (xORo[1][2]==temp || xORo[1][2]=='T') && (xORo[1][3]==temp || xORo[1][3]=='T') )
				{
					if(temp=='.')
						{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}
			temp = xORo[2][0];
				if( (xORo[2][1]==temp || xORo[2][1]=='T') && (xORo[2][2]==temp || xORo[2][2]=='T') && (xORo[2][3]==temp || xORo[2][3]=='T') )
				{
					if(temp=='.')
						{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}	
			temp = xORo[3][0];
				if( (xORo[1][0]==temp || xORo[1][0]=='T') && (xORo[2][0]==temp || xORo[2][0]=='T') && (xORo[0][0]==temp || xORo[0][0]=='T') )
				{
					if(temp=='.')
						{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}
				if( (xORo[2][1]==temp || xORo[2][1]=='T') && (xORo[1][2]==temp || xORo[1][2]=='T') && (xORo[0][3]==temp || xORo[0][3]=='T') )
				{
					if(temp=='.')
						{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}
				if( (xORo[3][1]==temp || xORo[3][1]=='T') && (xORo[3][2]==temp || xORo[3][2]=='T') && (xORo[3][3]==temp || xORo[3][3]=='T') )
				{
					if(temp=='.')
						{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}	
			temp = xORo[3][1];
				if( (xORo[0][1]==temp || xORo[0][1]=='T') && (xORo[1][1]==temp || xORo[1][1]=='T') && (xORo[2][1]==temp || xORo[2][1]=='T') )
				{
					if(temp=='.')
						{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}	
			temp = xORo[3][2];
				if( (xORo[0][2]==temp || xORo[0][2]=='T') && (xORo[1][2]==temp || xORo[1][2]=='T') && (xORo[2][2]==temp || xORo[2][2]=='T') )
				{
					if(temp=='.')
						{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}	

			temp = xORo[3][3];
				if( (xORo[3][2]==temp || xORo[3][2]=='T') && (xORo[3][1]==temp || xORo[3][1]=='T') && (xORo[3][0]==temp || xORo[3][0]=='T') )
				{
					if(temp=='.')
					{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}
				if( (xORo[0][3]==temp || xORo[0][3]=='T') && (xORo[1][3]==temp || xORo[1][3]=='T') && (xORo[2][3]==temp || xORo[2][3]=='T') )
				{
					if(temp=='.')
					{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}
				if( (xORo[1][1]==temp || xORo[1][1]=='T') && (xORo[2][2]==temp || xORo[2][2]=='T') && (xORo[0][0]==temp || xORo[0][0]=='T') )
				{
					if(temp=='.')
					{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}

			temp = xORo[2][3];
				if( (xORo[2][2]==temp || xORo[2][2]=='T') && (xORo[2][0]==temp || xORo[2][0]=='T') && (xORo[2][1]==temp || xORo[2][1]=='T') )
				{
					if(temp=='.')
					{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}

			temp = xORo[1][3];
				if( (xORo[1][2]==temp || xORo[1][2]=='T') && (xORo[1][1]==temp || xORo[1][1]=='T') && (xORo[1][0]==temp || xORo[1][0]=='T') )
				{
					if(temp=='.')
					{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}

			temp = xORo[0][3];
				if( (xORo[1][3]==temp || xORo[1][3]=='T') && (xORo[2][3]==temp || xORo[2][3]=='T') && (xORo[3][3]==temp || xORo[3][3]=='T') )
				{
					if(temp=='.')
					{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}	
				if( (xORo[1][2]==temp || xORo[1][2]=='T') && (xORo[2][1]==temp || xORo[2][1]=='T') && (xORo[3][0]==temp || xORo[3][0]=='T') )
				{
					if(temp=='.')
					{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}
				if( (xORo[0][1]==temp || xORo[0][1]=='T') && (xORo[0][2]==temp || xORo[0][2]=='T') && (xORo[0][0]==temp || xORo[0][0]=='T') )
				{
					if(temp=='.')
					{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}

			temp = xORo[0][2];
				if( (xORo[1][2]==temp || xORo[1][2]=='T') && (xORo[2][2]==temp || xORo[2][2]=='T') && (xORo[3][2]==temp || xORo[3][2]=='T') )
				{
					if(temp=='.')
					{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}	

			temp = xORo[0][1];
				if( (xORo[1][1]==temp || xORo[1][1]=='T') && (xORo[2][1]==temp || xORo[2][1]=='T') && (xORo[3][1]==temp || xORo[3][1]=='T') )
				{
					if(temp=='.')
					{count++;}else{
					cout<<"Case #"<<(i+1)<<": "<<temp<<" won"<<endl;
					solnFound=true;
					break;}
				}
		tempCount++;
		}

		if(solnFound)
		{
		//break;
		continue;
		}
		else
			if(count>0)
			{
				cout<<"Case #"<<(i+1)<<": Game has not completed"<<endl;
			}
			else
			{
				cout<<"Case #"<<(i+1)<<": Draw"<<endl;
			}
	
	}
}
