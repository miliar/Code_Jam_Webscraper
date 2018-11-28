#include <iostream>
using namespace std;
void initialize(int * array)
{int i;
    for(i=0;i<=9;i++)
    {
        array[i]=0;
    }
}
int check(int * array)
{   int i;
    for(i=0;i<10;i++)
    {
        if(array[i]==0)
            return 0;
    }
    return 1;
    
}
int main() {
	int t,rem,k;
	long long int num;
	int array [10];
	cin>> t;int temp=t;
	int numc;
	while (t--)
	{   
	    initialize(array);
	    k=1;
	    cin>> num;
	    numc=num;
	while(num<numc*1000)
	{
	    while(num>0)
	    {
	        rem=num%10;
	        array[rem]=1;
	        num=num/10;
	    }
	    
	    if(check(array))
	    {   cout<<"Case #"<<temp-t<<": "<<numc*k<<"\n";
	        break;
	        
	    }
	    else
	    num=numc*++k;
	    }
	   if(!check(array))
	    cout<<"Case #"<<temp-t<<": "<<"INSOMNIA\n";
	}
	return 0;
}

