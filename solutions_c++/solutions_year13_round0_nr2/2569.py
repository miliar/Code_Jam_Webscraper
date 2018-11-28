// STL
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

/*
 * --------------------------------------------------
 *  GLOBALS
 * --------------------------------------------------
 */

void
get_graph_from_input(
		std::istream & __in,
		const std::size_t __row,
		const std::size_t __col,
		std::size_t *__graph_buffer);

bool
process_graph(
		const std::size_t __row,
		const std::size_t __col,
		const std::size_t *__graph_buffer);

int main() {
	/*
	 * --------------------------------------------------
	 *  INIT
	 * --------------------------------------------------
	 */
#ifdef DEBUG
	std::ifstream INPUT("file.in");
#else
	std::istream & INPUT = std::cin;
#endif// DEBUG

	std::size_t __case_size;
	INPUT >> __case_size;

	std::size_t Nrows;
	std::size_t Mcols;

	/*
	 * --------------------------------------------------
	 *  MAIN LOGIC
	 * --------------------------------------------------
	 */
	for(std::size_t __case_iter = 1lu;
			__case_iter <= __case_size;
			++__case_iter)
	{
		INPUT >> Nrows;
		INPUT >> Mcols;

		std::size_t * __graph_buffer = new std::size_t[Nrows * Mcols];

		get_graph_from_input(INPUT, Nrows, Mcols, __graph_buffer);

		bool __state = process_graph(Nrows, Mcols, __graph_buffer);

		if(__state == true) {
			std::cout << "Case #" << __case_iter << ": YES" << std::endl;
		} else {
			std::cout << "Case #" << __case_iter << ": NO" << std::endl;
		}//if-else

		delete[] __graph_buffer;
	}//for

	/*
	 * --------------------------------------------------
	 *  CLEAN UP
	 * --------------------------------------------------
	 */
#ifdef DEBUG
	INPUT.close();
#endif
}//main

void
get_graph_from_input(
		std::istream & __in,
		const std::size_t __row,
		const std::size_t __col,
		std::size_t *__graph_buffer)
{
	for(auto __i_row = 0lu; __i_row < __row; ++__i_row) {
		for(auto __j_col = 0lu; __j_col < __col; ++__j_col) {
			__in >> *(__graph_buffer + __col * __i_row + __j_col);
		}//for
	}//for
}//get_graph_from_input(__row, __col, __graph_buffer)

bool
process_graph(
		const std::size_t __row,
		const std::size_t __col,
		const std::size_t *__graph_buffer)
{
	for(auto __i = 0lu; __i < __row; ++__i) {
		for(auto __j = 0lu; __j < __col; ++__j) {
			std::size_t __cur = *(__graph_buffer + __col * __i + __j);
			//in cur row
			bool check_col = false;
			for(auto __k = 0lu; __k < __col; ++__k) {
				std::size_t __other = *(__graph_buffer + __col * __i + __k);
				if(__other > __cur)
					check_col = true;
			}//for

			if(check_col == true) {
				for(auto __m = 0lu; __m < __row; ++__m) {
					std::size_t __other = *(__graph_buffer + __col * __m + __j);
					if(__other > __cur)
						return false;
				}//for
			}//if
		}//for
	}//for
	return true;
}//process_graph(__row, __col, __graph_buffer)

