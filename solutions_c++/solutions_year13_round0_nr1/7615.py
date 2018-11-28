#include <cstddef>
#include <cstdio>
#include <cassert>

namespace {
	const std::size_t g_board_size = 4;
	const std::size_t g_x_marker = 1;
	const std::size_t g_o_marker = 256;
	const std::size_t g_t_marker = 65536;

	enum class result {
		x_wins,
		o_wins,
		draw,
		not_completed
	};

	template <std::size_t n>
	result check_lines( const std::size_t (&line)[n], result def ) {
		if( def == result::x_wins || def == result::o_wins ) {
			return def;
		}

		for( std::size_t i = 0; i < n; ++i ) {
			if( line[i] == g_x_marker * g_board_size || line[i] == g_x_marker * ( g_board_size - 1 ) + g_t_marker ) {
				return result::x_wins;
			}

			if( line[i] == g_o_marker * g_board_size || line[i] == g_o_marker * ( g_board_size - 1 ) + g_t_marker ) {
				return result::o_wins;
			}
		}

		return def;
	}

	std::size_t chr_to_marker( char c ) {
		switch( c ) {
		case 'X':
			return g_x_marker;

		case 'O':
			return g_o_marker;

		case 'T':
			return g_t_marker;

		case '.':
			return 0;

		default:
			assert( false );
		}

		return 0;
	}
}

int main() {

	std::size_t tests_num = 0;
	scanf_s( "%Iu\n", &tests_num );

	std::size_t case_num = 0;
	while( ++case_num <= tests_num ) {

		int chr = std::getchar();
		assert( chr == '\n' );

		std::size_t rows[g_board_size] = {};
		std::size_t cols[g_board_size] = {};
		std::size_t diag[2] = {};
		result res = result::draw;

		for( std::size_t y = 0; y < g_board_size; ++y ) {
			for( std::size_t x = 0; x < g_board_size; ++x ) {
				int chr = _getchar_nolock();
				
				rows[y] += chr_to_marker( chr );
				cols[x] += chr_to_marker( chr );

				if( x == y ) {
					diag[0] += chr_to_marker( chr );
				}

				if( x + y == g_board_size - 1 ) {
					diag[1] += chr_to_marker( chr );
				}

				if( chr == '.' ) {
					res = result::not_completed;
				}
			}

			chr = _getchar_nolock();
			assert( chr == '\n' );
		}

		res = check_lines( rows, res );
		res = check_lines( cols, res );
		res = check_lines( diag, res );

		char* res_str = nullptr;
		switch( res ) {
		case result::x_wins:
			res_str = "X won";
			break;

		case result::o_wins:
			res_str = "O won";
			break;

		case result::not_completed:
			res_str = "Game has not completed";
			break;

		case result::draw:
			res_str = "Draw";
			break;

		default:
			assert( false );
		}

		printf_s( "Case #%Iu: %s\n", case_num, res_str );
	}

	return 0;
}