#include <iostream>
using namespace std;

int arr[1000];	
int j;

int main()
{


bool cmp();
int t,n;
int on;
cin>>t;
cout<<"\n";
	for(int i=1;i<=t;i++)
	{

	cin>>on;

for(int x=0;x<1000;x++)
arr[x]=-1;
int k=0;
j=1;
int cn;
bool val=false;
while(j<1000 && val!=true )
{
		
		n=on*j;
		cn=n;
		//cout<<"\t\n"<<n<<"\t\n"<<on;
		while (n!=0)
		{
		arr[k]=n%10;
		n/=10;
		k++;	
		}
	val=cmp();
		
	j++;
}	

		if(val==true &&on!=0)
		{
		cout<<"Case #"<<i<<": "<<cn<<endl;
		}
		else	
		cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
//	for(int y=0;y<100;y++)
//cout<<arr[y]<<"\t";
//cout<<"\n\n"<<k;
		}

}


bool cmp()
{
int ret[10]={0,0,0,0,0,0,0,0,0,0};

for(int ic = 0; ic < 10; ic++) 

{ 

    for (int jc = 0; jc < 1000; jc++) 
{ 
      if (arr[jc]==ic) 
{
	  ret[ic]=11;
	  
      }
    }
//cout<<"\n\n\n"<<ic<<"\t"<<ret[ic];

  }

bool allEqual=true;

for (int z=0; z<9; z++) {
    if (ret[z] != ret[z+1])
        allEqual=false;
}
//cout<<"\n\nThe "<<allEqual;
if (allEqual==true)
{

return true;
j=1000;
}
else
return false;
}
