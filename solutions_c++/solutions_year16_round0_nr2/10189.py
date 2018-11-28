#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
using namespace std;


int main()
{
	int S,count=0;
	int Q=1;
	int a=0;
	std::string str;
	
	ifstream fin;
	fin.open("B-large.in",ios::in);
	ofstream fout;
	fout.open("output.txt",ios::out);
	LABEL:while(std::getline(fin,str))
	{   
		
	    if(Q==1)
	    {
		istringstream buffer(str);
	    buffer>>S;Q=2;
	    goto LABEL;
	    }
	    a++;    
		char line[str.size()+1];
		strcpy(line,str.c_str()); 
	    
	    
	    for(int i=(sizeof(line)-2);i>=0;--i)	  
		{ 
		  if(line[i]!='+')
		    {   
		         for(int j=i;j>=0;--j)	
		          {
		          	if(line[j]!='+')
		             line[j]='+';
		            else if(line[j]!='-')
					    line[j]='-';        
		             
		          }  count++;
			}
			
		      
		}  	
    	 
	   
	  
	   
	    fout<<"Case #"<<a<<": "<<count<<"\n";
	     if(a==S)
	    {break;
	    }
		  count=0;
	}
	fin.close();
	fout.close();
}
