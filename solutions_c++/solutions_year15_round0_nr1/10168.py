#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,i,j;
	long int total,need;
	int smax;
	char a[1005];
	cin>>t;
	for(j=1;j<=t;j++)
	{ need = 0;
	cin>>smax;
	cin>>a;
    total = a[0]-'0';
    for(i=1;i<=smax;i++)
    {
       if(total>=i)
         {
         total = total+(a[i]-'0');
         //cout<<"i="<<i<<"\t"<<total<<"\n";
         }
        else
        {
        total = total +1;
        total = total+(a[i]-'0');
        need=need+1;
        //cout<<"i="<<i<<"\t"<<total<<"\t"<<"need"<<need<<"\n";
        
        
        }
    
    
    }
    cout<<"Case #"<<j<<": "<<need<<"\n";
	}
	
	return 0;
}
