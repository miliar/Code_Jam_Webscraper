#include <iostream>

using namespace std;

enum caseStatus{
	EMPTY,
	X,
	O,
	T
};

enum tableStatus{
	DRAW,
	XWIN,
	OWIN,
	GAMENOTCOMPLETED
};

tableStatus checkTable(caseStatus* table){
	tableStatus result = GAMENOTCOMPLETED;
	int statusCount[4] = {0};

	//check rows
	for(int row = 0; row < 4; row++){
		for(int col = 0; col < 4; col++){
			caseStatus a = *(table+row*4+col);
			statusCount[*(table+row*4+col)]++;
		}
		if(statusCount[X] == 4 || (statusCount[X] == 3 && statusCount[T] == 1))
			return XWIN;
		else if(statusCount[O] == 4 || (statusCount[O] == 3 && statusCount[T] == 1))
			return OWIN;
		fill(statusCount+1, statusCount+4, 0);
	}

	//check cols
	for(int col = 0; col < 4; col++){
		for(int row = 0; row < 4; row++){
			caseStatus a = *(table+row*4+col);
			statusCount[*(table+row*4+col)]++;
		}
		if(statusCount[X] == 4 || (statusCount[X] == 3 && statusCount[T] == 1))
			return XWIN;
		else if(statusCount[O] == 4 || (statusCount[O] == 3 && statusCount[T] == 1))
			return OWIN;
		fill(statusCount+1, statusCount+4, 0);
	}

	//check diags (only two diags are 4 cases long) : {{0,0}, {1,1}, {2,2}, {3,3}} and {{0,3}, {1,2}, {2,1}, {3,0}}
	statusCount[*(table+4*0+0)]++;
	statusCount[*(table+4*1+1)]++;
	statusCount[*(table+4*2+2)]++;
	statusCount[*(table+4*3+3)]++;
	if(statusCount[X] == 4 || (statusCount[X] == 3 && statusCount[T] == 1))
		return XWIN;
	else if(statusCount[O] == 4 || (statusCount[O] == 3 && statusCount[T] == 1))
		return OWIN;
	fill(statusCount+1, statusCount+4, 0);

	statusCount[*(table+4*0+3)]++;
	statusCount[*(table+4*1+2)]++;
	statusCount[*(table+4*2+1)]++;
	statusCount[*(table+4*3+0)]++;
	if(statusCount[X] == 4 || (statusCount[X] == 3 && statusCount[T] == 1))
		return XWIN;
	else if(statusCount[O] == 4 || (statusCount[O] == 3 && statusCount[T] == 1))
		return OWIN;
	fill(statusCount+1, statusCount+4, 0);

	if(statusCount[EMPTY] == 0)
		return DRAW;
	else
		return GAMENOTCOMPLETED;
}

int main(void){
	caseStatus table[4][4];
	int nbTables;
	char caractere;

	cin >> nbTables;

	tableStatus* status = new tableStatus[nbTables];

	for(int tableIndex = 0; tableIndex<nbTables; tableIndex++){
		for(int row = 0; row < 4; row++){
			for(int col = 0; col < 4; col++){
				cin >> caractere;
				switch (caractere)
				{
				case 'X':
					table[row][col] = X;
					break;
				case 'O':
					table[row][col] = O;
					break;
				case 'T':
					table[row][col] = T;
					break;
				case '.':
					table[row][col] = EMPTY;
					break;
				default:
					break;
				}
			}
			//cin >> caractere;
		}

		status[tableIndex] = checkTable(*table);
	}

	for(int tableIndex = 0; tableIndex < nbTables; tableIndex++){
		switch (status[tableIndex])
		{
		case DRAW:
			cout << "Case #" << tableIndex + 1 << ": Draw" << endl;
			break;
		case XWIN:
			cout << "Case #" << tableIndex + 1 << ": X won" << endl;
			break;
		case OWIN:
			cout << "Case #" << tableIndex + 1 << ": O won" << endl;
			break;
		case GAMENOTCOMPLETED:
			cout << "Case #" << tableIndex + 1 << ": Game has not completed" << endl;
			break;
		default:
			break;
		}
	}

	delete[] status;

	return 0;
}