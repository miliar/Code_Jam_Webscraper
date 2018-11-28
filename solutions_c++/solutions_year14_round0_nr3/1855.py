#include <cstdio>
#include <vector>
#include <list>
#include <utility>

using namespace std;

struct cell_t{
	bool mined;
	bool opened;
	int neighbor_mine_count;
};

typedef pair<int, int> pos_t;
typedef vector<vector<cell_t> > board_t;

void print_board(board_t& board, int r, int c, int click_r, int click_c){
	for(int rr = 0; rr < r; rr++){
		for(int cc = 0; cc < c; cc++){
			if(rr == click_r && cc == click_c){
				printf("c");
			}else{
				if(board[rr][cc].mined){
					printf("*");
				}else{
					printf(".");
				}
			}
		}
		printf("\n");
	}
}

void try_board(board_t& board, int r, int c) throw(int){
	for(int rr = 0; rr < r; rr++){
		for(int cc = 0; cc < c; cc++){
			board_t tryboard(board);
			list<pos_t> open_queue;
			open_queue.push_back(pos_t(rr, cc));
			while(open_queue.size() > 0){
				pos_t pos = open_queue.front();
				open_queue.pop_front();
				int rrr = pos.first;
				int ccc = pos.second;
				if(!tryboard[rrr][ccc].opened){
					if(!tryboard[rrr][ccc].mined){
						if(tryboard[rrr][ccc].neighbor_mine_count == 0){
							for(int rro = -1; rro <= 1; rro++){
								for(int cco = -1; cco <= 1; cco++){
									if((!(rro == 0 && cco == 0)) && rrr+rro >= 0 && rrr+rro < r && ccc+cco >= 0 && ccc+cco < c){
										open_queue.push_back(pos_t(rrr + rro, ccc + cco));
									}
								}
							}
						}
						tryboard[rrr][ccc].opened = true;
					}
				}
			}
			bool matched = true;
			for(int rr2 = 0; rr2 < r; rr2++){
				for(int cc2 = 0; cc2 < c; cc2++){
					if(!tryboard[rr2][cc2].mined && !tryboard[rr2][cc2].opened){
						matched = false;
					}
				}
			}
			if(matched){
				print_board(board, r, c, rr, cc);
				throw 1;
			}
		}
	}
}

void count_neighbor_mines(board_t& board, int r, int c){
	for(int rr = 0; rr < r; rr++){
		for(int cc = 0; cc < c; cc++){
			int count = 0;
			for(int rro = -1; rro <= 1; rro++){
				for(int cco = -1; cco <= 1; cco++){
					if((!(rro == 0 && cco == 0)) && rr+rro >= 0 && rr+rro < r && cc+cco >= 0 && cc+cco < c){
						if(board[rr+rro][cc+cco].mined){
							count++;
						}
					}
				}
			}
			board[rr][cc].neighbor_mine_count = count;
		}
	}
}

void fill_mine_and_try(board_t& board, int r, int c, int m, int rr, int cc) throw(int){
	if(cc >= c){
		rr++;
		cc = 0;
	}
	if(rr >= r){
		if(m == 0){
			count_neighbor_mines(board, r, c);
			try_board(board, r, c);
		}
		return;
	}
	if(m == 0){
		count_neighbor_mines(board, r, c);
		try_board(board, r, c);
	}else{
		board[rr][cc].mined = true;
		fill_mine_and_try(board, r, c, m - 1, rr, cc + 1);
		board[rr][cc].mined = false;
		fill_mine_and_try(board, r, c, m, rr, cc + 1);
	}
}

void init_board(board_t& board, int r, int c){
	for(int rr = 0; rr < r; rr++){
		for(int cc = 0; cc < c; cc++){
			board[rr][cc].mined = false;
			board[rr][cc].opened = false;
			board[rr][cc].neighbor_mine_count = 0u;
		}
	}
}

int main(){
	int T = 0;
	scanf("%u", &T);
	for(int case_no = 1; case_no <= T; case_no++){
		int R = 0;
		int C = 0;
		int M = 0;
		scanf("%d", &R);
		scanf("%d", &C);
		scanf("%d", &M);

		printf("Case #%u:\n", case_no);
		board_t board(R, vector<cell_t>(C));
		init_board(board, R, C);
		bool match = false;
		try{
			fill_mine_and_try(board, R, C, M, 0, 0);
		}catch(int){
			match = true;
		}
		if(!match){
			printf("Impossible\n");
		}
	}
	return 0;
}