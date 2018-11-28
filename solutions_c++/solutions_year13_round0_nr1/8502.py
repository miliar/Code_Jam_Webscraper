#include <string>
#include <fstream>
#include <vector>
#include <sstream>
#include <iostream>

class BoardInspector;

class Board
{
	public:

		Board( const std::string& rawState )
		{
			for ( unsigned int row = 0; row < 4; ++row )
			{
				for ( unsigned int col = 0; col < 4; ++col )
				{
					m_state[row][col] = rawState.at( ( 4 * row ) + col );
				}
			}
		}

	private:

		// Row, Column
		friend BoardInspector;
		char m_state[4][4];
};

class BoardInspector
{
	public:

		enum class Result { X_WON, O_WON, DRAW, INCOMPLETE };

	private:

		enum class WonResult { X_WON, O_WON, NO_WIN };

	public:

		static Result Inspect( const Board& board )
		{
			WonResult win = IsAnyWin( board );

			if ( win == WonResult::X_WON )
			{
				return Result::X_WON;
			}

			if ( win == WonResult::O_WON )
			{
				return Result::O_WON;
			}

			if ( IsBoardFull( board ) )
			{
				return Result::DRAW;
			}

			return Result::INCOMPLETE;
		}

	private:

		static WonResult IsAnyWin( const Board& board )
		{
			//
			// Horizontals
			//
			for ( unsigned int row = 0; row < 4; ++row )
			{
				char firstChar = board.m_state[row][0];
				if ( firstChar == T_CH )
				{
					firstChar = board.m_state[row][1];
				}

				if ( firstChar == E_CH )
				{
					continue;
				}

				bool won = true;

				for ( unsigned int col = 0; col < 4; ++col )
				{
					if ( ( board.m_state[row][col] != T_CH ) && ( board.m_state[row][col] != firstChar ) )
					{
						won = false;
						break;
					}
				}

				if ( won )
				{
					return firstChar == X_CH ? WonResult::X_WON : WonResult::O_WON;
				}
			}

			//
			// Verticals
			//
			for ( unsigned int col = 0; col < 4; ++col )
			{
				char firstChar = board.m_state[0][col];
				if ( firstChar == T_CH )
				{
					firstChar = board.m_state[1][col];
				}

				if ( firstChar == E_CH )
				{
					continue;
				}

				bool won = true;

				for ( unsigned int row = 0; row < 4; ++row )
				{
					if ( ( board.m_state[row][col] != T_CH ) && ( board.m_state[row][col] != firstChar ) )
					{
						won = false;
						break;
					}
				}

				if ( won )
				{
					return firstChar == X_CH ? WonResult::X_WON : WonResult::O_WON;
				}
			}

			//
			// Right Diagonal
			//
			char firstChar = board.m_state[0][0];
			if ( firstChar == T_CH )
			{
				firstChar = board.m_state[1][1];
			}

			if ( firstChar != E_CH )
			{
				bool won = true;

				for ( unsigned int row = 0, col = 0; row < 4, col < 4; ++row, ++col )
				{
					if ( ( board.m_state[row][col] != T_CH ) && ( board.m_state[row][col] != firstChar ) )
					{
						won = false;
						break;
					}
				}

				if ( won )
				{
					return firstChar == X_CH ? WonResult::X_WON : WonResult::O_WON;
				}
			}

			//
			// Left Diagonal
			//
			firstChar = board.m_state[0][3];
			if ( firstChar == T_CH )
			{
				firstChar = board.m_state[1][2];
			}

			if ( firstChar != E_CH )
			{
				bool won = true;

				for ( unsigned int row = 0, col = 3; row < 4, col > 0; ++row, --col )
				{
					if ( ( board.m_state[row][col] != T_CH ) && ( board.m_state[row][col] != firstChar ) )
					{
						won = false;
						break;
					}
				}

				if ( won )
				{
					return firstChar == X_CH ? WonResult::X_WON : WonResult::O_WON;
				}
			}

			return WonResult::NO_WIN;
		}

		static bool IsBoardFull( const Board& board )
		{
			for ( unsigned int row = 0; row < 4; ++row )
			{
				for ( unsigned int col = 0; col < 4; ++col )
				{
					if ( board.m_state[row][col] == E_CH )
					{
						return false;
					}
				}
			}

			return true;
		}

	private:

		static const char X_CH = 'X';
		static const char O_CH = 'O';
		static const char T_CH = 'T';
		static const char E_CH = '.';
};

class FileLoader
{
	public:

		void Load( const std::string& fileStr )
		{
			std::ifstream file( fileStr.c_str() );
			std::string line;

			if ( !file.is_open() )
			{
				return;
			}

			while ( file.good() )
			{
				std::getline( file, line );
				lines.push_back( line );
			}

			file.close();
		}

		void CollapseEmptyLines()
		{
			for ( auto it = lines.begin(); it != lines.end(); ++it )
			{
				if ( it->empty() )
				{
					it = lines.erase( it );
					if ( it == lines.end() )
					{
						return;
					}
				}
			}
		}

	public:

		static std::vector<std::string> Split( const std::string& str, char delim )
		{
			std::vector<std::string> result;
			std::string tempStr;

			std::stringstream ss( str );

			while ( std::getline( ss, tempStr, delim ) )
			{
				result.push_back( tempStr );
			}

			return std::move( result );
		}

	public:

		std::vector<std::string> lines;
};

int main()
{

	FileLoader loader;
	loader.Load( "input.txt" );

	std::stringstream ss( loader.lines.at( 0 ) );
	unsigned int numCases = 0;
	ss >> numCases;

	for ( unsigned int curCase = 0; curCase < numCases; ++curCase )
	{
		std::string l1 = loader.lines.at( curCase * 5 + 1 );
		std::string l2 = loader.lines.at( curCase * 5 + 2 );
		std::string l3 = loader.lines.at( curCase * 5 + 3 );
		std::string l4 = loader.lines.at( curCase * 5 + 4 );

		Board board( l1 + l2 + l3 + l4 );

		BoardInspector::Result result = BoardInspector::Inspect( board );

		std::cout << "Case #" << ( curCase + 1 ) << ": ";

		switch ( result )
		{
			case BoardInspector::Result::X_WON:
			{
				std::cout << "X won";
			}
			break;

			case BoardInspector::Result::O_WON:
			{
				std::cout << "O won";
			}
			break;

			case BoardInspector::Result::DRAW:
			{
				std::cout << "Draw";
			}
			break;

			case BoardInspector::Result::INCOMPLETE:
			{
				std::cout << "Game has not completed";
			}
			break;
		}
		
		if ( curCase != ( numCases -1 ) )
		{
			std::cout << std::endl;
		}
	}

	return 0;
}