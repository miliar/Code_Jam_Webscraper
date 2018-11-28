
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

enum{ XWON, OWON, DRAW, NOTCOMPLETE };

class Judger
{
protected:
	map<int, pair<char,int>> mapRow;
	map<int, pair<char,int>> mapColumn;
	map<int, pair<char,int>> mapDiagonal;
	bool isWon;
	char whoWon;
	int allNum;
public: 
	Judger()
	{
		for( int i = 0; i < 4; ++i  )
		{
			mapRow[i].first = ' ';
			mapRow[i].second = 0;
			mapColumn[i].first = ' ';
			mapColumn[i].second = 0;
		}

		for( int i = 0; i < 2; ++i  )
		{
			mapDiagonal[i].first = ' ';
			mapDiagonal[i].second = 0;
		}

		isWon = false;
		whoWon = ' ';
		allNum = 0;
	}
public: 
	void insert( char c, int x, int y )
	{
		if(isWon|| c == '.')
		{
			return;
		}

		allNum++;
		bool isT = c=='T';
		int dia = OnDiagonal(x,y);

		if( dia != 3)
		{
			bool iseFirst = c == mapDiagonal[0].first;
			bool iseSecond = c == mapDiagonal[1].first;
			bool isFirstPlus = iseFirst || isT;
			bool isSecondPlus = iseSecond || isT;

			switch(dia)
			{
			case 0:
				mapDiagonal[0].second = isFirstPlus ? mapDiagonal[0].second+1 : 1;
				mapDiagonal[0].first = !iseFirst ? mapDiagonal[0].first=c : mapDiagonal[0].first;
				break;
			case 1:
				mapDiagonal[1].second = isSecondPlus ? mapDiagonal[1].second+1 : 1;
				mapDiagonal[1].first = !iseSecond ? mapDiagonal[1].first=c : mapDiagonal[1].first;
				break;
			case 2:
				mapDiagonal[0].second = isFirstPlus ? mapDiagonal[0].second+1 : 1;
				mapDiagonal[1].second = isSecondPlus ? mapDiagonal[1].second+1 : 1;
				mapDiagonal[0].first = !iseFirst ? mapDiagonal[0].first=c : mapDiagonal[0].first;
				mapDiagonal[1].first = !iseSecond ? mapDiagonal[1].first=c : mapDiagonal[1].first;
				break;
			}

			bool isFirstWon = mapDiagonal[0].second == 4;
			bool isSecondWon = mapDiagonal[1].second == 4;
			isWon = isFirstWon||isSecondWon;
			if(isFirstWon||isSecondWon)
			{
				whoWon = isFirstWon? mapDiagonal[0].first : mapDiagonal[1].first;
			}
		}

		bool iseRow = c == mapRow[x].first;
		bool iseCol = c == mapColumn[y].first;
		bool isRowPlus = iseRow || isT;
		bool isColPlus = iseCol || isT;

		mapRow[x].second = isRowPlus ? mapRow[x].second+1 : 1;
		mapColumn[y].second = isColPlus ? mapColumn[y].second+1 : 1;

		bool isRowWon = mapRow[x].second == 4;
		bool isColWon = mapColumn[y].second == 4;
		isWon = isWon ? true : isRowWon || isColWon;
		if (isRowWon||isColWon)
		{
			whoWon = isRowWon? mapRow[x].first : mapColumn[y].first;
		}

		mapRow[x].first = !iseRow ? mapRow[x].first=c : mapRow[x].first;
		mapColumn[y].first = !iseCol ? mapColumn[y].first=c : mapColumn[y].first;
	}

	int OnDiagonal(int x, int y)
	{
		if(x==y && 3-x != y)
		{
			return 0;
		}
		if( x!=y && 3-x == y )
		{
			return 1;
		}
		if( x==y && 3-x ==y )
		{
			return 2;
		}

		return 3;
	}

	int judgeCase()
	{
		if(isWon)
		{
			return whoWon=='X' ? XWON : OWON;
		}

		if(allNum == 4*4)
		{
			return DRAW;
		}

		return NOTCOMPLETE;
	}
};

string printRel(int rel)
{
	switch(rel)
	{
	case XWON:
		return "X won";
		break;
	case OWON:
		return "O won";
		break;
	case DRAW:
		return "Draw";
		break;
	case NOTCOMPLETE:
		return "Game has not completed";
		break;
	}
}

int main()
{
	ifstream ifs("A-small-attempt2.in");
	
	vector<int> vecRel;
	int n;
	ifs >> n;
	for (int i = 0 ; i < n; ++i)
	{
		Judger jud;
		for( int j = 0; j < 4; ++j )
		{
			for( int k = 0; k < 4; ++k )
			{
				char c;
				ifs >> c;
				jud.insert(c,j,k);
			}
		}
		vecRel.push_back(jud.judgeCase());
	}

	ofstream ofs("A-small-attempt2.out");
	for (int i =0; i < vecRel.size(); ++i)
	{
		ofs << "Case #" << i+1 << ": " << printRel(vecRel[i]) << endl;
	}

	//system("pause");
	return 0;
}

