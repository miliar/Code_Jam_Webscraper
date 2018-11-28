#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin("abc.txt");
    ofstream fout("ex.txt",ios::app);
    int test;
    fin>>test;
    for(int i=0;i<test;i++)
    {
	char a;
    int b,c,temp;
    fin>>b;
    fin>>a;
    fin>>c;
    int count=0;
    int flag=0;
    temp=c;
    while(temp>1)
    {
    	if(temp%(2)==1)
    	{flag=1;
    	break;
    	}
    	
    	temp=temp/2;
    }
    
    while(b<c)
    {
    	b=b*2;
    	
    	count++;
    }
    if(flag==1)
    fout<<"Case #"<<i+1<<": "<<"impossible\n";
    else
    fout<<"Case #"<<i+1<<": "<<count<<"\n";
    	
    }
    
    return 0;
    
}



 
 
      
         
     
            
