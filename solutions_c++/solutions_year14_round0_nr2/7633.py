#include <iostream>
#include <iomanip>
using namespace std;

 int main()
 {double C,R=2,F,X,tot=0;
	 int T;
	 cin>>T;
	 for(int num=0;num<T;num++)
	 {tot=0;R=2;
		 cin>>C>>F>>X;
		 while((X/R)>((C/R)+(X/(F+R))))
		 {tot+=C/R;
			 R+=F;
			
			 }
		 tot+=X/R;
		 
		 cout<<"Case #"<<(num+1)<<": "<<setprecision(11)<<tot<<endl;
		 
		 }
	 
	 
	 
	 
	 return 0;
	 }
