#include<stdio.h>
#include<vector>
#include<string>
#include<fstream>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>

using namespace std;

typedef struct
{
	int BOARD[100][100];
	int N;
	int M;
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
				
				p.N = _strtoi64( split_line[0].c_str() , NULL , 10 );
				p.M = _strtoi64( split_line[1].c_str() , NULL , 10 );

				for (int i = 0; i < p.N; i++)
				{
					getline( ifs , line );
					split_line = split( line , " ");
					for (int j = 0; j < p.M; j++)
					{
						p.BOARD[i][j] = _strtoi64( split_line[j].c_str() , NULL , 10 );
					}
				}
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


bool solve(PROBLEM &p)
{
	int tempBoard[100][100];
	memcpy(tempBoard,p.BOARD,100*100*sizeof(int));

	for(int i = 1 ; i <= 100; ++i) {
		for(int s=0;s<p.N;++s) {
			bool bline = true;
			for(int t=0;t<p.M;++t) {
				if(p.BOARD[s][t]!=i){
					bline = false;
					break;
				}
			}
			if(bline){
				for(int t=0;t<p.M;++t) {
					tempBoard[s][t]=i+1;
				}
			}
		}
		for(int s=0;s<p.M;++s) {
			bool bline = true;
			for(int t=0;t<p.N;++t) {
				if(p.BOARD[t][s]!=i){
					bline = false;
					break;
				}
			}
			if(bline){
				for(int t=0;t<p.N;++t) {
					tempBoard[t][s]=i+1;
				}
			}
		}
		bool y=true;
		for(int s=0;s<p.N;++s) {
			for(int t=0;t<p.M;++t) {
				if(tempBoard[s][t]==i){
					return false;
				}
				if(tempBoard[s][t]!=i+1){
					y = false;
				}
			}
		}
		if(y) return true;
		memcpy(p.BOARD,tempBoard,100*100*sizeof(int));
	}
	return false;
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
			printf("Case #%d: YES\n",++count);
		}else{
			printf("Case #%d: NO\n",++count);
		}
	}

	return 0;
}
