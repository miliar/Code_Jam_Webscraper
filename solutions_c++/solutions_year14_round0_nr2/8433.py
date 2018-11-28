#include"iomanip"
using namespace std;
#include"iostream"
using namespace std;
#include"fstream"
void main()
{
	fstream file,out;
	file.open("B-large.in",ios::in);
	if(file.fail()) cout<<"can not open file B-large.in";
	else
	{
		out.open("output.txt",ios::out);
		out.setf(ios::fixed | ios::showpoint);
		double t=0,f,h,a,c,x;
		file>>a;
		for(int i=1;i<=a;i++)
		{
			file>>c;
			file>>f;
			file>>x;
			h=2;t=0.0;
			while((x/h)>(c/h+x/(h+f)))
			{
				t=t+double(c/h);
				h=h+f;
			}
			t=t+double(x/h);
			out<<"Case #"<<i<<": "<<setprecision(7)<<t<<endl;
		}
	out.close();
	file.close();
	}
}