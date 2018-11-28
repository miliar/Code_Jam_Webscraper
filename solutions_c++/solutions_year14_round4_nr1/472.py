#include <iostream>
#include <map>
using namespace std;

void print_args(){}

template <typename T, typename... Args>
void print_args(const T & val, Args... args)
{
	cout << val << " ";
	print_args(args...);
}

template <typename... Args>
void print_case(int test_case, Args... args)
{
	cout << "Case #" << test_case << ": ";
	print_args(args...);
	cout << endl;
}

int main()
{
	int num_cases;
	cin >> num_cases;
	for(int c = 0; c < num_cases; c++)
	{
		int num_files, disc_size;
		cin >> num_files >> disc_size;
		map<int,int> files;
		for(int n = 0; n < num_files; n++)
		{
			int file;
			cin >> file;
			files[file]++;
		}
		int num_discs = 0;
		while(!files.empty())
		{
			auto p = *files.rbegin();
			auto r = files.rbegin();
			r->second--;
			if( r->second == 0 )
				files.erase(files.find(r->first));
			num_discs++;
			if( files.empty() )
				continue;
			int target = disc_size - p.first;
			auto hi = files.upper_bound(target);
			if( hi == files.begin() )
				continue;
			hi--;
			hi->second--;
			if( hi->second == 0 )
				files.erase(hi);
		}
		print_case(c+1, num_discs);
	}
	return 0;
}
