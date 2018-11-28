# include <iostream>
# include <fstream>
# include <cmath>


using namespace std;

int main ()
{
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");

	if(!in) 
	{ cout << "Cannot open file.\n"; 
	system ("pause");
	return 1;
	}

	int a,b,ans,temp;
	double rev=0,rem=0,n;
    in>>n;
    for (int x=1; x<=n; x++)
	{
		ans=0;
		in>>a;
		in>>b;
		
		for (int i=a; i<=b; i++)
		{

			temp=i;
			rev=0;  
			while(temp>0)
			{
                rem=temp%10;
                rev=rev*10+rem;
				
                temp=temp/10;
                
                }
         
                
		if (i==rev) 
		{			
			double j= sqrt (rev);
			
			rev=0;
			int temp1=j;
    
			while(temp1>0)
			{
                rem=temp1%10;
                rev=rev*10+rem;
                temp1=temp1/10;
                
                }

			if (j==rev)
				ans ++;
		
		
		}
		}

		out<<"Case #"<<x<<":"<<" "<<ans<<endl;

	}
	system("pause");
	return 0;

}