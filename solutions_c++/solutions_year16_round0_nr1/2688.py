#ifndef __PR1__H__
#define __PR1__H__

#include <vector>
#define MAX_DIGITS 64
#define INIT_MSD_POSITION 6

class _pr1_ {
	public:
		_pr1_(char* file_name) : _msd_position_(INIT_MSD_POSITION), _file_(file_name)
		{
			_digit_map_.resize(10);
			_digits_.resize(MAX_DIGITS);
			_init_digits_.resize(MAX_DIGITS);
			initialize();
		}
		~_pr1_(){}
		void run();
	private:
		void compute_digits(uint32_t N,uint32_t test_case);
		void compute_initial_digits(uint32_t N);
		uint8_t compute_msd_position(uint32_t N);
		uint8_t compute_carry (uint64_t iter_cnt, uint64_t pos);
		uint8_t compute_digit (uint64_t k, uint64_t position);
		uint8_t compute_ith_digit (uint32_t N, uint8_t i);
		void initialize()
		{
			for(uint8_t i = 0;i < MAX_DIGITS;++i)
			{
				_digits_[i] = 0;
				_init_digits_[i] = 0;
				if (i < 10) {
					_digit_map_[i] = false;
				}
			}
		}
		bool _check_digit_map_()
		{
			bool result = true;
			for(uint8_t i = 0;i < 10;++i)
			{
				result &= _digit_map_[i];
			}
			return result;
		}
	private:
		std::vector<uint8_t> _digits_;
		std::vector<uint8_t> _init_digits_;
		std::vector<bool> _digit_map_;
		uint64_t _msd_position_;
		uint32_t _init_N_;
		char* _file_;

}; // _pr1_

#endif //__PR1__H__

