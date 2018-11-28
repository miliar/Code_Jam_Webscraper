#include <iostream>
using namespace std;


int main() {
	int T=0,N=0;
	int Num = 0;
	int oldNum = 0,count =0;
	int a[10]={0},flag=0;
	int x=0;
	
	cin>>T;
	for(int i= 1;i<=T;i++)
	{
        a[0] = 0;
        a[1] = 0;
        a[2] = 0;
        a[3] = 0;
        a[4] = 0;
        a[5] = 0;
        a[6] = 0;
        a[7] = 0;
        a[8] = 0;
        a[9] = 0;
	    count = 0;
	    N = 0;
	    x=0;
	    cin>>N;
   if(N==0)
	    {
	        cout<<"Case #"<<i<<": INSOMNIA"<<endl;
	        continue;
	    }
	    Num = 0;
	     flag = 0;
	    while(1)
	    {
	        count++;
	        try
	        {
	        Num =N * count;
	        }
	        catch(exception e)
	        {
	           flag = 0;
	           break;
	        }

int v=0,temp=0;
temp= Num;
	        while(temp >0)
	        {
	            v = temp%10;
	             if(a[v] ==0)
	            {
	            a[v] = 1;
	           
	            }
	            temp = temp/10;
	        
	        }
	       
	        if(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9] == 10)
	        {
	            flag = 1;
	            break;
	        }
	    }
	    if(flag == 1)
	    {
	      cout<<"Case #"<<i<<": "<<Num<<endl;  
	    }
	    else
	    {
	        cout<<"Case #"<<i<<": INSOMNIA"<<endl; 
	    }
	    
	}
	return 0;
}
