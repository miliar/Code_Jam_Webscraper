#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(int argc, char* argv[])
{
	fstream burmeister;
	
	if(argc!=2)
	{
		cout<<"Usage: ./executable filename"<<endl;			//Format is ./'executable' filename
	}
	else
	{
		burmeister.open(argv[1], ios::in);

		char temp;
		char tempstring[100];				//Current longest method/attrib name is 100. Perhaps use String instead?
		int no_methods = 0;				
		int no_attribs = 0;
		int **access;					//The Access Matrix.
		int **mergeaccess;				//Matrix to detect partition.
		
		burmeister>>temp;
		burmeister>>no_methods;
		burmeister>>no_attribs;
		
		access = new int *[no_methods];
		mergeaccess = new int *[no_methods];
		for(int i=0; i<no_methods; i++)			//Init the Access Matrix.
		{
			access[i] = new int[no_attribs];
			mergeaccess[i] = new int[no_attribs];
		}
		
		for(int i=0; i<no_methods+no_attribs+2; i++)	//Skip through the method/attrib names.
		{
			burmeister.getline(tempstring, 100);
			//cout<<tempstring<<endl;
		}
		
		for(int i=0; i<no_methods; i++)			//Read the Access Matrix.
		{
			for(int j=0; j<no_attribs; j++)
			{
				burmeister>>temp;
				if( temp == 'X')
				{
					access[i][j] = 1;
					mergeaccess[i][j] = 1;
				}
				else
				{
					access[i][j] = 0;
					mergeaccess[i][j] = 0;
				}
				//cout<<access[i][j];
			}
			//cout<<endl;
		}
		
		/*Find if a Supremum exists and count the number          */
		/*Also count the number of attribs accessed by each method*/
		
		int supremum =0;
		int *method_access_count;
		method_access_count = new int[no_methods];
		
		for(int i=0; i<no_methods; i++)
		{
			int unaccessed_attrib = 0;	
			method_access_count[i] = 0;
			
			for(int j=0; j<no_attribs; j++)
			{
				if(access[i][j] == 0)
				{
					unaccessed_attrib = 1;
				}
				else
				{
					method_access_count[i]++;
				}
			}
			if(unaccessed_attrib == 0)
			{
				supremum++;
			}
			//cout<<i<<" "<<method_access_count[i]<<endl;
		}
		
		//cout<<supremum<<endl;

		/*Find if an Infimum exists and count the number        */
		/*Also count the number of methods accessing each attrib*/
		
		int infimum = 0;
		int *attrib_access_count;
		attrib_access_count = new int[no_attribs];
		
		for(int i=0; i<no_attribs; i++)
		{
			int unaccessed_attrib = 0;
			attrib_access_count[i] = 0;
			
			for(int j=0; j<no_methods; j++)
			{
				if(access[j][i] == 0)
				{
					unaccessed_attrib = 1;
				}
				else
				{
					attrib_access_count[i]++;
				}
			}
			if(unaccessed_attrib == 0)
			{
				infimum++;
			}
			//cout<<i<<" "<<attrib_access_count[i]<<endl;
		}
		//cout<<infimum<<endl;
		
		/*Find width, if any*/
		
		int method_width = 0;
		
		for(int i=0; i<no_methods; i++)
		{
			for(int j=0; j<no_methods; j++)
			{				
				if(i!=j && method_access_count[i]==method_access_count[j])
				{
					for(int k=0; k<no_attribs; k++)
					{
						if(access[i][k]!=access[j][k])
						{
							method_width++;
							break;
						}
					}
				}
			}
		}
		
		int attrib_width = 0;
		
		for(int i=0; i<no_attribs; i++)
		{
			for(int j=0; j<no_attribs; j++)
			{				
				if(i!=j && attrib_access_count[i]==attrib_access_count[j])
				{
					for(int k=0; k<no_methods; k++)
					{
						if(access[k][i]!=access[k][j])
						{
							attrib_width++;
							break;
						}
					}
				}
			}
		}
		
		//cout<<method_width<<" "<<attrib_width<<endl;
		
		/*Detecting Partition*/
		
		/*Method:- Take the bottom most access list on the access matrix, and merge with the first list containing a common attrib.
		  Do this until there is only one list, or a list has no common attributes with any others.*/
		
		int partition = 0;
		  
		for(int i=no_methods-1; i>=1; i--)
		{
			int merged = 0;
			for(int j=0; j<i; j++)
			{
				for(int k=0; k<no_attribs; k++)
				{
					if((mergeaccess[i][k] == 1) && (mergeaccess[j][k] == 1))
					{
						for(int l=0; l<no_attribs; l++)
						{
							if(mergeaccess[i][l] == 1)
							{
								mergeaccess[j][l] = 1;
							}
						}
						merged = 1;				//Merge Successfull, i.e. there is some method which has a link to this.
						break;
					}
				}
				if(merged == 1)
				{
					break;
				}
			}
			if( merged == 0)						// There are no methods having links to this. Hence it is partitioned.
			{
				partition = 1;
				break;
			}
		}

		/*Display the result*/
		
		if(supremum && infimum)
		{
			if((supremum == no_methods) && (infimum == no_attribs))
			{
				cout<<"Dot"<<endl;
			}
			else if(method_width || attrib_width)
			{
				cout<<"Diamond"<<endl;
			}
			else
			{
				cout<<"Chain"<<endl;
			}
		}
		else if(supremum)
		{
			cout<<"Umbrella"<<endl;
		}
		else if(infimum)
		{
			cout<<"Inverted Umbrella"<<endl;
		}
		else if(!partition)
		{
			cout<<"Mountain Range"<<endl;
		}
		else
		{
			cout<<"Partitioned"<<endl;
		}
					
	}
	
	return 0;
}
	
	
