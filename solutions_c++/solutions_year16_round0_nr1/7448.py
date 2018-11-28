#include <iostream>
#include <fstream>
#include <list>

using namespace std;

void initializeArray( bool arr[9])
{
	for (int i = 0; i < 10 ; i++)
	{
		arr[i] = false;
	}
}

void addToList(list<int> &v, bool arr[9], int N)
{
	int num;
	while(N != 0)
	{
		num = N%10;
		if(arr[num] == false)
		{
			v.push_back(num);
			arr[num] = true;
		}
		N = N/10;
	}
}

int main()
{
	ifstream in("A-large.in");
	if(!in)
	{
		cout<<"Input file does not exist";
	}
	else
	{
		int T, N;
		in>>T;
		if(T >= 1 && T <= 100)
		{
			bool arr[10];
			list<int> v;
			ofstream out("output.txt", ios::app);
			int caseNo = 1;
			initializeArray(arr);
			int j = 0;
			while(j < T)
			{
				in>>N;
				if(N == 0)
				{
					out<<"Case #"<<caseNo++<<": INSOMNIA"<<endl;
				}
				else
				{
					int i = 1;
					int ans;
					while(v.size() != 10)
					{
						ans = i*N;
						addToList(v, arr, ans);
						//v.sort();
						i++;
					}
					out<<"Case #"<<caseNo++<<": "<<ans<<endl;
				}
				v.clear();
				initializeArray(arr);
				j++;
			}
			out.close();
		}
	}
	in.close();
	return 0;
}