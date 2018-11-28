#include <iostream>
using namespace std;

int main() {
	
	int t;
	scanf("%d",&t);
	int caseno=1;
	while(t--)
	{
		double c,f,x,result,s=0;
		double t=0;
		cin>>c>>f>>x;
		double k,check=x/2.0;
		int n,i=0,found=0;
	//	bool it =true;
		while(1)
		{
			s = s + c/(2 + i*f);
			//cout<<"s "<<s<<endl;
			i++;
			k = x/(2+i*f);
		//	cout<<k<<" k \n"<<i<<endl;
			//cout<<"sk "<<s+k<<endl;
			
			if(s+k >check)
			{
				break;
			}else
			{
				check = s+k ;
			}
			
		}
		
		cout.setf(ios::fixed);
		cout.setf(ios::showpoint);
		cout.precision(7);
	
	cout<<"Case #"<<caseno++<<": "<<check<<endl;

		
	}
	
	return 0;
}