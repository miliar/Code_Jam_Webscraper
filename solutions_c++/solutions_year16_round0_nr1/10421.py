#include <iostream>
#include <fstream>

using namespace std;
int myfunc(int aa)
{
   int m[10];
   
   for(int i=0;i<10;++i)
   m[i]=0;
   
   int aa1=aa;
   
   if(aa==0)
    return -1;
   
   for(;;)
   {
      if(aa1==0)
       break;
       
       m[aa1%10]=1;
       
       aa1/=10;   
   }
		
   aa1=aa;
   		
   for(int ii=2;ii<100;++ii)	
   {
         
       aa1=aa*(ii-1);  
       int f=1;
       for(int i=0;i<10;++i)
        {
    //       cout<<m[i]<<" ";
		   	
		   if(m[i]==0)
		     f=0;
		}
			
		if(f==1)
		 return aa1;		 
				              
      // cout<<endl;


	   aa1=aa*ii;  
        
       //cout<<aa1<<endl; 

for(;;)
   {
      if(aa1==0)
       break;
       
       m[aa1%10]=1;
       
       aa1/=10;   
   }

   }
		
	
}


int main()
{
	
    ifstream myfile;
	ofstream myfile1;
	
	myfile.open("C:\\Users\\Fatema Arobee Rima\\Documents\\A-large.in");
	myfile1.open("C:\\Users\\Fatema Arobee Rima\\Documents\\out.txt");
/*
    if(!myfile)
    cout<<"Error"<<endl;
    else
    cout<<"okz"<<endl;
*/
    int n=3;
    
    myfile >> n;
    
    cout<<"N="<<n<<endl;
    
    int i=0;
    int a;
    
	while (i<n)
    {
    	++i;
    	myfile >> a;
    //    cout<<a<<endl;
        
        
       int r = myfunc(a);
       
        if(r<0)
        myfile1 <<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        //cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        else
        myfile1 <<"Case #"<<i<<": "<<r<<endl;
        
    }

    myfile.close();
    myfile1.close();
    getchar();

	return 0;
}
