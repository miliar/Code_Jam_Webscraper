#include<fstream.h>
#include<conio.h>

int main()
{
	clrscr();
	int t,smax,fi,rsl;
	char sl[1001];

	ifstream inp_file;
	inp_file.open("input.in");
	
	if(!inp_file)
	{
		cerr<<"file cannot open correctly in";
	}

	ofstream out_file("output.txt");
	if(!out_file)
	{
	cerr<<"file cannot open correctly out";
	}

	inp_file>>t;
	
	for(int i=1;i<=t;i++)
	{
		fi=0;
		inp_file>>smax;

		inp_file>>sl;
		rsl=0;
		for(int n=0;n<=smax;n++)
		{
			if((sl[n]-'0')==0&&rsl<=n)
			{
					fi++;
					rsl++;
			}
			else
			{
				rsl=rsl+(sl[n]-'0');
			}
			
		}

		out_file<<"case #"<<i<<": "<<fi<<endl;
	}

	return 0;
}
