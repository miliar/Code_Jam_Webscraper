#include<iostream>
#include<vector>
#include<algorithm>
#define PIPT std::pair<int,Point>
#define VECPIPT std::vector<PIPT>
#define VECINT std::vector<int>
#define VV std::vector< VECINT >

class Point{
	public:
		Point(): x(0),y(0) {}
		Point(int x_in, int y_in): x(x_in),y(y_in) {}
		int x;
		int y;
};

bool PRED(const PIPT & p1, const PIPT & p2);
bool otoczenie(const PIPT & p, const VV & plansza);

int main(){
	std::ios_base::sync_with_stdio(false);
	
	int T;
	std::cin >> T;
	
	for(int i=0; i < T; ++i){
		int N,M;
		std::cin >> N >> M;
		VECPIPT P;
		VV plansza (N, VECINT(M,0));
		P.reserve(N*M);
		for(int y = 0 ; y < N; ++y)
			for(int x=0; x < M; ++x){
				std::cin >> plansza[y][x];
				P.push_back(PIPT(plansza[y][x],Point(x,y)));
			}
		
		std::sort(P.begin(),P.end(),PRED);
		
		bool R = true;
		for(unsigned int j = 0 ; j < P.size() && R; ++j)
			if(!otoczenie(P[j],plansza))
				R = false;

		if(R)
			std::cout << "Case #" << (i+1) << ": " << "YES"<<std::endl;
		else
			std::cout << "Case #" << (i+1) << ": " << "NO" << std::endl;
	}
	
	return 0;
}

bool otoczenie( const PIPT & p, const VV & plansza){
	bool R1,R2;
	R1 = R2 = true;
	for(unsigned int i = 0; i < plansza[p.second.y].size(); ++i)
		if(plansza[p.second.y][i]>p.first)
			R1 = false;
			
	for(unsigned int i = 0; i < plansza.size(); ++i)
		if(plansza[i][p.second.x]>p.first)
			R2 = false;
			
	return (R1||R2);
}


bool PRED(const PIPT & p1, const PIPT & p2){
	return p1.first<p2.first;
}
