#include <iostream>
#include <string>
#include <fstream>
#include<iomanip>
using namespace std;
int main()
{
	string ishq;
	string num;
	double longtime[2];
	double shorttime[2];
	double shorty[2];
	double shortlong=0;
	double finalterm=0;
	double  c,f,x;
	double start=2;
	ifstream jhoom("smallinput1.txt");
	ofstream yo("out.txt");
	getline(jhoom,num);
	cout<<fixed<<setprecision(7);
	int total=atoi(num.c_str());
	for(int temp=0;temp<total;temp++)
	{
		c=0;
		f=0;
		x=0;
		start=2;
		for(int tem=0;tem<2;tem++){
				 longtime[tem]=0;
				 shorttime[tem]=0;
				 shorty[tem]=0;
				 shortlong=0;
				 finalterm=0;
		}

		
		jhoom>>c;
		jhoom>>f;
		jhoom>>x;




		for(int here=0;here<100000;here++){
		shorttime[1]=(c/start);	
		longtime[1]=(x/start);
		start=start+f;
		shorty[1]=shortlong+longtime[1];
		if((here)>=1&&(shorty[1]>shorty[0])){
			finalterm=shorty[0];		
			break;
		}
		shortlong=shortlong+shorttime[1];
		shorttime[0]=shorttime[1];
		longtime[0]=longtime[1];
		shorty[0]=shorty[1];
		}
//		cout<<endl<<endl<<endl;
		yo<<fixed<<setprecision(7)<<"Case #"<<temp+1<<": "<<finalterm<<endl;
//		cout<<setprecision(7)<<finalterm<<endl;
	}
	
	
	
		system("pause");
	
}




