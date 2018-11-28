#include<iostream>
#include<fstream>
using namespace std;
main()
{
    ifstream input("A-large.in");
    ofstream out("output.txt");
    
    long long N,c=0;
    input>>N;
    
  
    while(input>>N){
    long long array [10]={5,0,0,0,0,0,0,0,0,0};
   long long flag=0;
    long long counter=0;
    long long prod=1,result,res,maxi=1;
    if(N==0){
    	c++;
				out<<"Case #"<<c<<":"<<" INSOMNIA"<<endl;
    	continue;
	}
    	while(1){
      
         counter=0;
        result=N*prod;
        
        
        
       
            maxi=result;
        
        
        
        
        
        while(result!=0)
        {
            res=result%10;
            array[res]=res;
            
            result=result/10;
            
        }
        
        
        for(int i=0;i<10;i++)  // chick point
        {if(array[i]==i)
            {counter++;}
        }
            if(counter==10)
	            { c++;
					out<<"Case #"<<c<<": "<< maxi<<endl;
				break;
			}
        
        
        
        
        
        
        prod++;
}
    
    
    
    }
    
    
}


