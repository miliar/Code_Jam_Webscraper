#include <iostream>
#include <string>
#include <fstream>
#include<iomanip>
using namespace std;
int main()
{
	string ishq;
	string num;
	double longtime[9000];
	double shorttime[9000];
	double shorty[9000];
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
		for(int tem=0;tem<900;tem++){
				 longtime[tem]=0;
				 shorttime[tem]=0;
				 shorty[tem]=0;
				 shortlong=0;
				 finalterm=0;
		}

		
		jhoom>>c;
		jhoom>>f;
		jhoom>>x;




		for(int here=0;here<9000;here++){
		shorttime[here]=(c/start);	
		longtime[here]=(x/start);
		start=start+f;
		shorty[here]=shortlong+longtime[here];
		if(here>=1&&(shorty[here]>shorty[here-1])){
			finalterm=shorty[here-1];		
			break;
		}
		
		shortlong=shortlong+shorttime[here];
		}
//		cout<<endl<<endl<<endl;
		yo<<fixed<<setprecision(7)<<"Case #"<<temp+1<<": "<<finalterm<<endl;
//		cout<<setprecision(7)<<finalterm<<endl;
	}
	
	
	
		system("pause");
	
}




