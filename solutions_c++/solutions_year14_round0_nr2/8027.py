#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main()
{
	ifstream ifs("B-small-attempt0.in");
	ofstream ofs("result.txt");
	cin.rdbuf(ifs.rdbuf());
	cout.rdbuf(ofs.rdbuf());
    int T;
	double c,f,x;
    cin>>T;
    for(int j=0;j<T;j++)
    {
		cin>>c>>f>>x;
		double rate=x/c-2/f;
		long pre=(long)rate;
		long next=pre+1;
		double result=0;
		for(long i=1;i<=pre;i++)
		{
			result += 1/((i-1)*f+2);
		}
		result *= c;
		double temp=c/((i-1)*f+2)+x/(f*i+2)-x/(f*(i-1)+2);
		if(temp>0)
		{
			result += x/(f*(i-1)+2);
		}else
		{
			result += c/((i-1)*f+2)+x/(f*i+2); 
		}
		cout<<"Case #"<<(j+1)<<": "<< fixed << setprecision(7)<<result<<endl;
	}
	ifs.close();
	ofs.close();
	return 0;
}