# include <fstream>
# include <iostream>
# include <cmath>
# include <set>
using namespace std;
int t;
long long a, b;
set< pair<long long, int> >S;

int pal (long long n)
{
	long long c=n, nr=0;
	while(n)
	{
		nr=nr*10+n%10;
		n/=10;
	}
	
	if (c==nr)
		return 1;
	
	return 0;
}

int main ()
{
	ifstream fin ("f.in");
	ofstream fout ("f.out");

	int cnt = 0;
	for(long long i=1;i<=10000000;++i)
		if (pal(i) && pal(i*i))
		{
			S.insert(make_pair(i*i, ++cnt));
		}

	fin>>t;
	for(int nt=1;nt<=t;++nt)
	{
		fin>>a>>b;
		
		pair<long long, int> pa=*(S.upper_bound(make_pair(a, 0)));
		pair<long long, int> pb=*(S.upper_bound(make_pair(b, 0)));
		
		cout<<pa.first<<" "<<pa.second<<"    "<<pb.first<<" "<<pb.second<<endl;
		
		int sol = pb.second - pa.second + 1;
		
		if (pa.first < a || pa.first >b)--sol;
		if (pa!=pb && (pb.first < a || pb.first >b))--sol;
		
		fout<<"Case #"<<nt<<": "<<sol<<"\n";
	}
	
	return 0;
}
