#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class hey
{
	int f,l;
	int nos;
	int** arr;
	int test[8];
	int count = 0;
	int count2=0;
public:
	

	
void get_data(void)
{
	int input;

	ifstream myfile; 

//	a_file<<"This text will now be inside of example.txt";
	
	int firstt=0;
	int nos,i,j;
	int a,b,m;
	int check;
	int p,q,r;
	int prev;
	myfile.open ("prices3.in");
	ofstream a_file ( "example.txt" );
	
	if (myfile.is_open())
	{
			while(myfile.eof() == false)
			{
				if(firstt==0)
				{		
					//	cout << "first \n";
						myfile>>input;
						f = input;
						l = 10*f;
						nos = 34 * a;
						arr = new int*[l];
						for(int i = 0; i < l; ++i)
						    arr[i] = new int[4];	
						firstt++;
				}
				else
				{
				//	cout << "f is " << f << "\n";
					prev=0;
					for(r=0;r<f;r++)
					{
						for(p=0;p<10;p++)
						{
						//	cout << "\np is " << p << "\n";
							if(p==0 || p==5)
							{
								myfile >> input;
								check=input;
								if(p==5)
									check=check+5;
							//	cout<< "read " << input;
								continue;
							}
							if(p==check)
							{
								for(i=0;i<4;i++)
									{
										myfile >> input;
									test[count]=input;
							//		cout<< "test[" << count << "] == " << test[count] << "\n";
									incr_count();
									}
									continue;
							}
							for(q=0;q<4;q++)
							{
								myfile >> input;
							//	cout << input ;
							}
						}	
						count2++;
						a_file << "case #" << count2 << ": ";
						m = check_equality() ;
						if(m>=0 && m<=16)
							a_file << m << "\n";
						else if(m==17)
							a_file << "Bad Magician!\n";	
						else if(m==18)
							a_file << "Volunteer cheated!\n";
					}
				}
			}
		myfile.close();
		a_file.close();
	}
	else
		cout << "Error opening file\n";
}

void incr_count()
{
	count++;
	count=count%8;
}

int check_equality()
{
	int i,j,eq=0;
	for(i=0;i<4;i++)
		{
			for(j=4;j<8;j++)
				{
					if(test[i]==test[j])
					{
						eq++;
					}
				}			
		}
	if(eq==1)
	{
		for(i=0;i<4;i++)
		{
			for(j=4;j<8;j++)
				{
					if(test[i]==test[j])
						return test[i];	
				}			
		}
	}
	else if(eq>1)
		return 17;
	else if(eq==0)
		return 18;	
				
}


} prog1;

int main()
{
	prog1.get_data();
}
