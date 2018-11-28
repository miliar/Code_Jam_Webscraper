#include <fstream>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int flips=0;
void check(string k);
void flip(int k);
int flag = 0; 
void flipups();
string pans, pan;


int main(int argc, char** argv)
{
    ifstream infile;
    infile.open("B-small-attempt8.in");
    
    ofstream outfile;
    outfile.open("output_pan.txt");
    
  for (int i=1;i<=100;i++)
  {
  	  getline(infile,pan);
     
        
        int j = pan.length();
        
        for(int s=0; s<j ; s++)
        {
        	pans[s] = pan[s];
		}
        
        check(pans);
        
        
    if(flag==1)
    {
   
    
            
       for(int m=j-1 ; m>=0 ; m--)
       {
           if(pans[m]=='-')
           {
		   	  if(pans[0]=='+')
		   	  {
                 flipups();
            
       		  }
       		  
           flip(m);
           }
          
       }
                
                   
    
    }
    
    outfile<<"Case #"<< i << ":" <<" " << flips << "\n" ;
    
    
    flips = 0;
    flag = 0;
    j=0;
    pan = pans = "";
}

infile.close();
outfile.close();
return 0;

}

void check(string k)
{
    for (int i=0; i<=k.length(); i++)
    {
        if (k[i] != '+')
        {flag = 1;}
        break;
    }
}

void flip(int k)
{
    char rev[k+1];
   
    int q = 0;
   
    flips = flips + 1;
    
    for(int t = k; t>=0 ;t--)
    {
        if(pans[t] == '+' )
        {
        	rev[q] = '-';
		}
		
		else
		{
			rev[q] = '+'; 
		}
        
        q++;
    }
    
    for(int i=0; i<=k;i++)
    {
		pans [i] = rev [i];
	}
	
    
    
    
    
}


void flipups()
{
    
    int h=0;
    while(pans[h] == '+')
    {
    	h++;
	}
     flip(h-1);
   
    }
