/* common *********************************************************************/
#define _CRT_SECURE_NO_WARNINGS
#define ASC 0
#define DESC 1
#include<iostream>
#include<sstream>
#include<fstream>

#include<string>
#include<vector>
#include<list>
#include<map>
#include<algorithm>

#include<exception>
#include<stdexcept>
#include<locale>

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>

using namespace std;

void calc();

void GenerateFilename(char* out, char* in, char* add){
	char* p;
	sprintf(out, "%s", in);
	for(p=out+strlen(out)-1; p>=out; p--){
		if(*p=='/' )break;
		if(*p=='\\')break;
		if(*p=='.' ){*p='\0'; break;}
	}
	sprintf(out+strlen(out), "%s", add);
}

void main(int argc, char* argv[]){
	char fname_o[_MAX_PATH];
	GenerateFilename(fname_o, argv[1], "_out.txt");
	FILE* fp_i = freopen(argv[1], "r", stdin);
	FILE* fp_o = freopen(fname_o, "w", stdout);

	int T;
	cin >> T;
	for(int No=1; No<=T; No++){
		cout << "Case #" << No << ": ";
		calc();
	}
	fclose(fp_i);
	fclose(fp_o);
}

/******************************************************************************/

typedef struct ST_CELL ST_CELL;
struct ST_CELL{
	int row;
	int col;
	vector <ST_CELL*> neigbors;
	char val;
};

vector< vector<ST_CELL>> board(50, vector<ST_CELL>(50));

void clearBoard(int R, int C){
	for(int row=0; row<R; row++){
		for(int col=0; col<C; col++){
			board[row][col].row = row;
			board[row][col].col = col;
			board[row][col].val = '*';

			board[row][col].neigbors.clear();
			for(int row2=row-1; row2<=row+1; row2++){
				if(row2 < 0) continue;
				if(row2 >=R) continue;
				for(int col2=col-1; col2<=col+1; col2++){
					if(col2 < 0) continue;
					if(col2 >=C) continue;
					if(row2==row && col2==col) continue;
					board[row][col].neigbors.push_back(&(board[row2][col2]));
				}
			}
		}
	}
}

void setBoard(vector <ST_CELL*> *cell0List){
	for(vector <ST_CELL*>::iterator cell0 = (*cell0List).begin(); cell0 != (*cell0List).end(); cell0++){
		(*cell0)->val = '.';
		for(vector <ST_CELL*>::iterator neigbor = (*cell0)->neigbors.begin(); neigbor != (*cell0)->neigbors.end(); neigbor++){
			(*neigbor)->val = '.';
		}
	}
	(*((*cell0List).begin()))->val = 'c';
}

void writeBoard(int R, int C){
	for(int row=0; row<R; row++){
		for(int col=0; col<C; col++){
			cout << board[row][col].val;
		}
		cout << endl;
	}
}


bool find1click(vector <ST_CELL*> *cell0List, int goal){
	vector <ST_CELL*> neigborList;

	neigborList.clear();
	for(vector <ST_CELL*>::iterator cell0 = (*cell0List).begin(); cell0 != (*cell0List).end(); cell0++){
		for(vector <ST_CELL*>::iterator neigbor = (*cell0)->neigbors.begin(); neigbor != (*cell0)->neigbors.end(); neigbor++){
			if(find((*cell0List).begin(),   (*cell0List).end(),   *neigbor) != (*cell0List).end()  ) continue;
			if(find(neigborList.begin(), neigborList.end(), *neigbor) != neigborList.end()) continue;
			neigborList.push_back(*neigbor);
		}
	}
	
	int nonBombSize = (*cell0List).size()+neigborList.size();
	if(nonBombSize == goal) return true;
	if(nonBombSize  > goal) return false;

	for(vector <ST_CELL*>::iterator neigbor = neigborList.begin(); neigbor != neigborList.end(); neigbor++){
		(*cell0List).push_back(*neigbor);
		if(find1click(cell0List, goal)) return true;
		(*cell0List).pop_back();
	}

	return false;
}

void calc(){
	int R;
	int C;
	int M;

	cin >> R;
	cin >> C;
	cin >> M;

	clearBoard(R, C);
	vector <ST_CELL*> cell0List;
	cell0List.push_back(&(board[0][0]));
	int goal = R*C-M;
	if(goal == 1){
		(*(cell0List.begin()))->val = 'c';
		cout << endl;
		writeBoard(R, C);
	}else if(find1click(&cell0List, goal)){
		setBoard(&cell0List);
		cout << endl;
		writeBoard(R, C);
	}else{
		cout << endl << "Impossible" << endl;
	}
}
