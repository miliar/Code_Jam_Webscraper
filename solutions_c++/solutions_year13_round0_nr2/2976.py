#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	fstream in;
	fstream out;
	in.open("B-large.in", ios::in);
	out.open("output.out", ios::trunc|ios::out);

	int t,n,m;

	in>>t;
	for (int i = 0; i < t; ++i)
	{	
		in>>n>>m;
			unsigned short board[100][100]={ 0 };
			unsigned short maxcolumn[100]={ 0 };	//m
			unsigned short maxrow[100]={ 0 };		//n
		for (int j = 0; j < n; ++j)
		{
			in.get();
			for (int k = 0; k < m; ++k)
			{
				unsigned short temp;
				in>>temp;
				if (temp>maxrow[j]) maxrow[j]=temp;
				if (temp>maxcolumn[k]) maxcolumn[k]=temp;
				board[j][k]=temp;
			}
		}
		//check
		enum {valid, invalid};
		int status=valid;
		//cout<<"valid"<<valid<<endl;
		//cout<<"invalid"<<invalid<<endl;
		// out<<endl;
		// for (int j = 0; j < n; ++j)
		// {
		// 	out<<maxrow[j]<<'\t';
		// }
		// out<<endl;
		// for (int k = 0; k < m; ++k)
		// {
		// 	out<<maxcolumn[k]<<'\t';
		// }
		for (int j = 0; j < n; ++j)
		{
			if (status == invalid) break;
			for (int k = 0; k < m; ++k)
			{
				//cout<<((board[j][k]==maxrow[j] || board[j][k]==maxcolumn[k]) == false);
				if ((board[j][k]==maxrow[j] || board[j][k]==maxcolumn[k]) == false)
				{
					status = invalid;
					//cout<<"status"<<status<<endl;
					break;
				}
			}
			//cout<<endl;
		}
		out<<"Case #"<<i+1<<": ";
		if (status==valid) out<<"YES";
		if (status==invalid) out<<"NO";
		out<<endl;
	}
}