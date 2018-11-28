
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <map>
#include <set>
#include <sstream>

using namespace std;

#define Log(x) std::cerr << x
#define Error(x) std::cerr << x; return false

template <typename T>
std::string Vector2String(const std::vector<T>& v)
{
	std::stringstream ss;
	std::vector<T>::const_iterator ite = v.begin();
	for(; ite != v.end(); ++ite)
	{
		ss << *ite << ", ";
	}
	return ss.str();
}

#define BOARD_SIZE_W (4)
#define BOARD_SIZE_H (4)
class Board
{
public:
	char data[4][5];
	std::string m_CaseName;
	typedef enum {
		GAME_STATE_X_WON,
		GAME_STATE_O_WON,
		GAME_STATE_NOT_END,
	} GameState;
	typedef enum {
		END_STATE_X_WON,
		END_STATE_O_WON,
		END_STATE_DRAW,
		END_STATE_NOT_COMPLETED,
	} EndState;

	Board(const Board& other)
		: m_CaseName(other.m_CaseName)
	{
		memcpy(data, other.data, sizeof(data));
	};
	Board(int n)
	{
		std::stringstream ss;
		ss << "Case #" << n << ": ";
		m_CaseName = ss.str();
	};
	bool AssignData(std::istream& input)
	{
		std::vector<std::string> lines;
		std::string line;
		for(int l = 0; l < BOARD_SIZE_H && std::getline(input, line); ++l)
		{
			lines.push_back(line);
		}
		if(lines.size() != BOARD_SIZE_H)
		{
			Error("データを読み込もうとして4行ありませんでした。");
		}
		for(int i = 0; i < BOARD_SIZE_H; ++i)
		{
			data[i][4] = '\0';
			if(lines[i].size() != BOARD_SIZE_W)
			{
				Error("何行目かのデータの長さが4ではありませんでした。");
			}
			for(int n = 0; n < BOARD_SIZE_W; ++n)
			{
				data[i][n] = lines[i].c_str()[n];
			}
		}
		return true;
	}

	std::string GetAnswer()
	{
		std::stringstream ss;
		ss << m_CaseName << EndState2String(CalcEndState());
		return ss.str();
	}

	std::string GetDescription()
	{
		std::stringstream out_stream;
		out_stream << m_CaseName;
		switch (CheckGameState())
		{
			case GAME_STATE_O_WON:
				out_stream << "O won";
				break;
			case GAME_STATE_X_WON:
				out_stream << "X won";
				break;
			default:
				break;
		}
		out_stream << std::endl;
		for(int i = 0; i < BOARD_SIZE_H; ++i)
		{
			out_stream << data[i] << std::endl;
		}
		out_stream << "X -> " << Vector2String(CalcLastCount('X')) << std::endl;
		out_stream << "O -> " << Vector2String(CalcLastCount('O')) << std::endl;
		out_stream << "EndState -> " << EndState2String(CalcEndState()) << std::endl;
		return out_stream.str();
	}

	std::string EndState2String(const EndState s)
	{
		switch(s)
		{
		case END_STATE_DRAW:
			return "Draw";
			break;
		case END_STATE_NOT_COMPLETED:
			return "Game has not completed";
			break;
		case END_STATE_X_WON:
			return "X won";
			break;
		case END_STATE_O_WON:
			return "O won";
			break;
		default:
			break;
		}
		return "Unknown";
	}

	// CalcLastCount() を使って、どちらが勝つかを計算します。
	EndState CalcEndState()
	{
		std::vector<int> X_state = CalcLastCount('X');
		std::vector<int> O_state = CalcLastCount('O');

		if(X_state[0] > 0)
		{
			return END_STATE_X_WON;
		}
		if(O_state[0] > 0)
		{
			return END_STATE_O_WON;
		}
		for( int i = 1 ; i < 3; ++i)
		{
			if(X_state[i] > i+0 && O_state[i-1] <= 0)
			{
				return END_STATE_X_WON;
			}
			if(O_state[i] > i+1 && X_state[i-1] <= 0)
			{
				return END_STATE_O_WON;
			}
		}
		if(X_state[5] == 10 && O_state[5] == 10)
		{
			return END_STATE_DRAW;
		}

		return END_STATE_NOT_COMPLETED;
	}

	// c 側の後？手で終了、という方向の数を数えます。0手、1手、2手、3手、4手、5手(5手はその方向はもう駄目)かかるそれぞれの数を返します。
	std::vector<int> CalcLastCount(const char checker)
	{
		std::vector<int> counts;
		counts.resize(6, 0);
		// 横
		for(int y = 0; y < BOARD_SIZE_H; ++y)
		{
			int num = 0;
			char c = 'T';
			for(int x = 0; x < BOARD_SIZE_W; ++x)
			{
				if(data[y][x] == 'T' || data[y][x] == checker)
				{
					num++;
				}
				else if(data[y][x] != '.')
				{
					num = -1;
					break;
				}
			}
			counts[BOARD_SIZE_H - num]++;
		}
		// 縦
		for(int x = 0; x < BOARD_SIZE_W; ++x)
		{
			int num = 0;
			char c = 'T';
			for(int y = 0; y < BOARD_SIZE_H; ++y)
			{
				if(data[y][x] == 'T' || data[y][x] == checker)
				{
					num++;
				}
				else if(data[y][x] != '.')
				{
					num = -1;
					break;
				}
			}
			counts[BOARD_SIZE_H - num]++;
		}
		// 斜め \ 方向
		do {
			int num = 0;
			for(int y = 0; y < BOARD_SIZE_H; ++y)
			{
				char c = 'T';
				if(data[y][y] == 'T' || data[y][y] == checker)
				{
					num++;
				}
				else if(data[y][y] != '.')
				{
					num = -1;
					break;
				}
			}
			counts[BOARD_SIZE_H - num]++;
		}while(false);
		// 斜め / 方向
		do {
			int num = 0;
			for(int y = 0; y < BOARD_SIZE_H; ++y)
			{
				char c = 'T';
				if(data[3-y][y] == 'T' || data[3-y][y] == checker)
				{
					num++;
				}
				else if(data[3-y][y] != '.')
				{
					num = -1;
					break;
				}
			}
			counts[BOARD_SIZE_H - num]++;
		}while(false);

		return counts;
	}

	GameState CheckGameState()
	{
		// 横
		for(int y = 0; y < BOARD_SIZE_H; ++y)
		{
			char c = 'T';
			for(int x = 0; x < BOARD_SIZE_W; ++x)
			{
				if(data[y][x] == 'T')
				{
					continue;
				}
				if((c == 'T' || c == 'X') && data[y][x] == 'X')
				{
					c = 'X';
					continue;
				}
				if((c == 'T' || c == 'O') && data[y][x] == 'O')
				{
					c = 'O';
					continue;
				}
				c = '.';
				break;
			}
			if(c == 'X')
			{
				return GAME_STATE_X_WON;
			}
			if(c == 'O')
			{
				return GAME_STATE_O_WON;
			}
		}

		// 縦
		for(int x = 0; x < BOARD_SIZE_W; ++x)
		{
			char c = 'T';
			for(int y = 0; y < BOARD_SIZE_W; ++y)
			{
				if(data[y][x] == 'T')
				{
					continue;
				}
				if((c == 'T' || c == 'X') && data[y][x] == 'X')
				{
					c = 'X';
					continue;
				}
				if((c == 'T' || c == 'O') && data[y][x] == 'O')
				{
					c = 'O';
					continue;
				}
				c = '.';
				break;
			}
			if(c == 'X')
			{
				return GAME_STATE_X_WON;
			}
			if(c == 'O')
			{
				return GAME_STATE_O_WON;
			}
		}

		// 斜め \ 向き
		{
			char c = 'T';
			for(int xy = 0; xy < BOARD_SIZE_W; ++xy)
			{
				if(data[xy][xy] == 'T')
				{
					continue;
				}
				if((c == 'T' || c == 'X') && data[xy][xy] == 'X')
				{
					c = 'X';
					continue;
				}
				if((c == 'T' || c == 'O') && data[xy][xy] == 'O')
				{
					c = 'O';
					continue;
				}
				c = '.';
				break;
			}
			if(c == 'X')
			{
				return GAME_STATE_X_WON;
			}
			if(c == 'O')
			{
				return GAME_STATE_O_WON;
			}
		}

		// 斜め / 向き
		{
			char c = 'T';
			for(int xy = 0; xy < BOARD_SIZE_W; ++xy)
			{
				if(data[3-xy][xy] == 'T')
				{
					continue;
				}
				if((c == 'T' || c == 'X') && data[3-xy][xy] == 'X')
				{
					c = 'X';
					continue;
				}
				if((c == 'T' || c == 'O') && data[3-xy][xy] == 'O')
				{
					c = 'O';
					continue;
				}
				c = '.';
				break;
			}
			if(c == 'X')
			{
				return GAME_STATE_X_WON;
			}
			if(c == 'O')
			{
				return GAME_STATE_O_WON;
			}
		}

		return GAME_STATE_NOT_END;
	}
};

class ProblemA
{
public:
	ProblemA()
	{
	}

	bool ReadProblem(std::istream& input, std::vector<Board>& out_problems)
	{
		std::string buf;

		if( ! std::getline(input, buf) )
		{
			Error("一行目の読み込みに失敗");
		}
		int n = atoi(buf.c_str());
		if( n <= 0 )
		{
			Error("一行目が数値に変換しても 0 でした。");
		}

		for(int i = 0; i < n; ++i)
		{
			Board b(i+1);
			if( ! b.AssignData(input) )
			{
				return false;
			}
			out_problems.push_back(b);

			// 一行は空白が来ます。
			if( ! std::getline(input, buf) )
			{
				break;
			}
		}
		return true;
	}

	bool Main()
	{
		std::vector<Board> problem_list;
		if( ! ReadProblem(std::cin, problem_list) )
		{
			return false;
		}
		std::vector<Board>::iterator ite = problem_list.begin();
		for(; ite != problem_list.end(); ++ite)
		{
			//std::cout << ite->GetDescription();
			std::cout << ite->GetAnswer() << std::endl;
		}

		return true;
	}
};



int main(int argc, char *argv[])
{
	ProblemA p;
	p.Main();
	return 0;
}
