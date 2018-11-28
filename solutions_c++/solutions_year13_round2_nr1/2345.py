#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

int main()
{
	fstream in;
	fstream out;
	in.open("A-small-attempt7.in", ios::in);
	// in.open("temp.in", ios::in);
	out.open("output.out", ios::trunc|ios::out);

	int t;
	in>>t;
	for (int repeat = 0; repeat < t; ++repeat)
	{
		out<<"Case #"<<repeat+1<<": ";
		//cout<<"Case #"<<repeat+1<<endl;
		int a,n,temp,op=0;
		vector<int> mote;
		in>>a>>n;
		for (int i = 0; i < n; ++i)
		{
			in>>temp;
			mote.push_back(temp);
		}
		sort(mote.begin(),mote.end());
		for (int i = 0; i < mote.size(); ++i)
		{
			//cout<<mote[i]<<'\t'<<a<<'\t'<<op<<endl;
			if (a==1) 
			{
				op=mote.size();
				break;
			}
			if (a>mote[i]) a+=mote[i];
			else 
			{
				int tempa=a,tempop=0;
				while (tempa<=mote[i])
				{
					tempa+=tempa-1;
					//cout<<"tempa+=tempa-1;"<<tempa<<endl;
					tempop+=1;
				}
				////cout<<"ADD"<<tempa<<"\t"<<tempop<<endl;
				if (tempop>(mote.size()-i))
				{
					op+=mote.size()-i;
					break;
				}
				else
				{
					a=tempa+mote[i];
					op+=tempop;
				}
			}
		}
		out<<op;
		out<<endl;
	}
}