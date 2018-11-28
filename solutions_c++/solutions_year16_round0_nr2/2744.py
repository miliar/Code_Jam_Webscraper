#include "pr2.h"

void _pr2_::run()
{
	std::ifstream ifs(_file_);
	std::string line;
	uint32_t N;
	uint64_t line_cnt = 0;

	if (ifs.is_open()) {
		while(std::getline(ifs,line))
		{
			if (line_cnt) {
				compute(line,line_cnt);
			}
			line_cnt++;
		}
		ifs.close();
	}

}

void _pr2_::compute(std::string& line,uint32_t tc)
{
	uint32_t flip_cnt = 0;
	char side_so_far;

  for (unsigned i = 0; i < line.length(); ++i)
  {
		if (!i) {
			side_so_far = line.at(i);
		} else {
			if (side_so_far != line.at(i)) {
				flip_cnt++;
				side_so_far = line.at(i);
			}
		}
  }
	if (side_so_far == '-') {
		flip_cnt++;
	}
	std::cout << "Case #"<<tc<<": "<<flip_cnt<<std::endl;
}

int main(int argc, char* argv[])
{
	_pr2_ pr2(argv[1]);

	pr2.run();

	return 0;
}
