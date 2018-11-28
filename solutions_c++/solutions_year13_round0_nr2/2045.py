#include<iostream>
#include<fstream>
using namespace std;

ifstream in;
ofstream out;

int main()
{
	in.open("B-large.in");
	out.open("output.txt");

	int t,n,m;
	in>>t;
	int testcases = t;
	while(t-- > 0)
	{
		in >> n >> m;
		int arr[n][m];

		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				in >> arr[i][j];

		bool flag = true;
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				int count = 0;

				for(int k=0; k<m; k++)
				{
					if(arr[i][k] > arr[i][j])
					{
						count++;
						break;
					}
				}

				for(int k = 0; k < n; ++k)
				{
					if(arr[k][j] > arr[i][j])
					{
						count++;
						break;
					}
				}

				if(count == 2)
				{
					out << "Case #"<< (testcases-t) << ": NO" << endl;
					flag = false;
					break;
				}
			}

			if(!flag)
				break;
		}

		if(flag)
			out << "Case #"<< (testcases-t) << ": YES" << endl;

	}

	in.close();
	out.close();
	return 0;
}
