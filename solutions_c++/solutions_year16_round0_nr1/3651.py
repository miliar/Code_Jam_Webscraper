#include <iostream>
using namespace std;

int check(int A[10])
{
    int x=0;
    for(int i=0;i<10;i++)
    {
        if(A[i]==0)
            x++;
    }
    
    if(x==0)
     return 1;
    else
     return 0;
}
int main() {
	int t;
	cin>>t;
	int q=t;
	while(t>0)
	{
	    int A[10]={0};
	    long long int n;
	    cin>>n;
	    if(n!=0){
	      
	    long long int y=n;
	    while(1)
	    {
	        long long int i=n;
	        
	        
	        while(i>0)
	        {
	          int r=i%10;
	          A[r-0]++;
	          i=i/10;
	        }
	        
	        int z=check(A);
	        if(z==1)
	         {
	             cout<<"Case #"<<q-t+1<<": "<<n<<endl;
	             break;
	         }
	         else
	        n+=y;
	    }
	    }
	    else
	    cout<<"Case #"<<q-t+1<<": INSOMNIA"<<endl;
	    t--;
	}
	return 0;
}

