#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

#define DEBUG 0

using namespace std;

int main()
{
    ofstream output;
    ifstream input ("A-small-attempt0.in");
    output.open("A-small-attempt0.out");
    string dummy;

    long long t;
	long long size;

    
    input >> t;

    for (long long i=0; i<t; i++)
    {

		vector<long long> motes;
        output << "Case #"<<i+1<<": ";
		
		//read the size
		input >> size;
			
		long long nr;
		input >> nr;

		for (long long j=0; j<nr; j++)
		{
			long long mote;
			input >> mote;
			motes.push_back(mote);
		}

		sort(motes.begin(), motes.end());

#if DEBUG
		for (long long j=0; j<nr; j++)
			cout<<motes[j]<<" ";
		cout <<endl;
#endif

		long long ops = 0;

		long long ret ;
		if (size == 1)
		{
			ret = nr;
			output<<ret;
			output << endl;
			continue;
		}

		vector<long long> add_only;
		add_only.push_back(nr);
		for(long long j=0; j<nr; j++)
		{
			while (size <= motes[j])
			{
				ops ++;
				size = 2 * size -1;
			}
			
			add_only.push_back(ops+nr-j-1);	
			size += motes[j];
		}

		sort(add_only.begin(), add_only.end());

		ret = add_only[0];

#if DEBUG
		for (long long j=0; j<nr; j++)
			cout<<add_only[j]<<" ";
		cout<<endl;
		cout << ret;
#endif
		output<<ret;
        output << endl;
    }

	return 0;
}
