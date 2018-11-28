#include<stdio.h>
#include<vector>
#include<string>
#include<fstream>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>

using namespace std;

const __int64 MAX = 10000000000000000;
const __int64 SQRTMAX = 10000000;

typedef struct
{
	__int64 A;
	__int64 B;
}PROBLEM;

vector<string> split( const string& line , const string& sep )
{
	int pos[2];
	pos[0] = pos[1] = 0;
	vector<string> split_line;
	while( ( pos[1] = line.find(sep,pos[0]) ) != string::npos )
	{
		string sub_line = line.substr( pos[0] , pos[1] - pos[0] );
		split_line.push_back(sub_line);
		pos[0] = pos[1] + 1;
	}
	string sub_line = line.substr( pos[0] );
	split_line.push_back(sub_line);
	return split_line;
}

bool read_problem( const char *fname , vector<PROBLEM>& problems )
{
	fstream ifs;
	ifs.open( fname );

	if( !ifs.is_open() ) return false;

	int T = 0;
	try{
		std::string line;
		int line_num = 0;
		while( getline( ifs , line ) ){
			if( line_num == 0 )	{
				T = strtoul( line.c_str() , NULL , 10);
			}else{
				PROBLEM p;
				
				auto split_line = split( line , " ");
				
				p.A = _strtoi64( split_line[0].c_str() , NULL , 10 );
				p.B = _strtoi64( split_line[1].c_str() , NULL , 10 );

				problems.push_back(p);
			}
			++line_num;
		}
	}catch(...){
		return false;
	}
	if( problems.size() != T ) return false;
	return true;
}

std::set<__int64> glist;

__int64 mmsqrt(__int64 a)
{
	__int64 min = 1;
	__int64 max = SQRTMAX+1;

	while(min!=max-1){
		__int64 middle = (min+max)/2;
		__int64 mmiddle = middle*middle;
		if(mmiddle<=a){
			min = middle;
		}else{
			max = middle;
		}
	}
	return min;
}

bool is_ps(__int64 m)
{
	__int64 temp = m;
	__int64 x=0;
	while(true){
		x += temp % 10;
		temp/=10;
		if(temp==0) {
			break;
		}
		x*=10;
	}
	if(m!=x) {
		return false;
	}

	__int64 mm = m*m;
	temp = mm;
	x=0;
	while(true){
		x += temp % 10;
		temp/=10;
		if(temp==0) {
			break;
		}
		x*=10;
	}
	if(mm==x) {
		return true;
	}
	return false;
}

void gen()
{
	__int64 m = mmsqrt(MAX);
	for(__int64 i=1;i<=m;++i){
		if(is_ps(i)) {
			glist.insert(i*i);
		}
	}
}

__int64 solve(PROBLEM &p)
{
	if(glist.empty()){
		gen();
	}
	auto f = glist.lower_bound(p.A);
	auto e = glist.upper_bound(p.B);
	__int64 x = std::distance(f,e);
	return x;
}

int main(int argc, char *argv[])
{
	vector<PROBLEM> problems;
	if( argc != 2 ) return -1;
	if( !read_problem( argv[1] , problems ) ) return -2;
	
	int count = 0;
	for( auto itr = problems.begin(); itr != problems.end() ; ++itr )
	{
		PROBLEM &problem = *itr;
		
		auto x = solve(problem);

		if(x){
			printf("Case #%d: %lld\n",++count,x);
		}else{
			printf("Case #%d: %lld\n",++count,x);
		}
	}

	return 0;
}
