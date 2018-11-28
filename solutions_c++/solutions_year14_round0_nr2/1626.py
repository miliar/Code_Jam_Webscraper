#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
//	freopen("B-large.in", "r", stdin);
	//freopen("demo.in", "r", stdin);
// 	freopen("Bl0.out", "w", stdout);
    int T;
    long double C,F,X;
    long double out=0.0;
    long double tmp,tmp1,tmp2; 
    cin >> T;
    for(int k=1;k<=T;k++)
    {
   		double v=0.0;
    	cin >> C>>F>>X;
		
		tmp=0;
		tmp1=X/2;
		v=2;
		
		tmp=(C/v);
		tmp2=tmp+(X/(v+F));
		v=v+F;
		
		while(tmp1>tmp2)
		{
			tmp1=tmp2;
			tmp+=(C/v);
			tmp2=tmp+(X/(v+F));
			v=v+F;
		}
		out =tmp1;
   		cout <<"Case #"<<k<<": ";
		cout<<fixed<<setprecision(7)<<out<<endl;
    }
	return 0;
}
