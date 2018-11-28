#ifndef __PR3_H__
#define __PR3_H__
#include <string>
#include <fstream>
#include <iostream>
#include <math.h>
#include <vector>
#include <cassert>

class _pr3_ {
	public:
		_pr3_(char* f)
		{
			_file_ = f;
		}
		~_pr3_()
		{
		}
		void run();
	private:
		void compute(std::string& line,uint32_t tc);
		void find_common_divisor(uint64_t N);
		void compute_jamcoin(uint64_t num_digits, uint64_t num_cases);
		void print_coinjam(std::vector<bool>& coinjam,uint64_t N);
		void print_dec_in_bin(uint64_t num_digits, uint64_t num, uint64_t divisor);
		uint64_t print_base2dec (uint64_t num_digits, uint64_t jamcoin,uint8_t base);
		void parse_input(std::string& line, uint64_t& num_digits, uint64_t& num_cases);
		uint64_t bit_swap(uint64_t n_bits,uint64_t num);
		void verify_result (uint64_t jamcoin, uint64_t divisor, uint64_t num_digits);
		uint64_t first_one_position(uint64_t n_bits,uint64_t num);
		uint64_t ipow(uint64_t base, uint64_t exp);

	private:
		char* _file_;
};//_pr3_

#endif //__PR3_H__
