using namespace std;
#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<string.h>
int main()
{
//clrscr();
freopen("inputR1.in","r",stdin);
freopen("outR1.out","w",stdout);
int T;
int r;
int m;
int s=0, count=0;
cin>>T;
	for(int x=1;x<=T;x++)
	{
		cin>>r>>m;
		count=0;
		s=0;
		for(int j=r; s<=m ; )
	    {
                s= s+ ((j+1)*(j+1) - (j*j));
                if((s<m) || (s==m))
                count++;
                j=j+2;
 
    	}
    	if( count==0 )
    	count++;
    	
    	 cout<<"Case #"<<x<<": "<<count;
               cout<<"\n";
              
               }

       getch();
       return 0;

	
}

