#include<fstream>
#include<conio.h>
using namespace std;
int main()
{
	int T,t,r,n,i,a,j=1;
	ifstream fin;
	ofstream fout;
	fin.open("abc.in",ios::in);
	fout.open("out.out",ios::out);
	fin>>T;
	while(T--)
	{
		fin>>r>>t;
		i=1;
		n=0;
		while(t>=0)
		{
			a=((r+i)*(r+i))-((r+i-1)*(r+i-1));
			t-=a;
			n++;
			i+=2;
		}
		n--;
		fout<<"Case #"<<j++<<": "<<n<<endl;
	}
	getch();
	return 0;
}