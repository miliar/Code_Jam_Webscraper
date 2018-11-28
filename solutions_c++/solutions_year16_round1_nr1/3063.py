#include <fstream>
#include <iostream>
#include <list>


class pr1 {
	public:
		pr1(char* file_)
		{
			file = file_;
		}
		~pr1(){};
		void run()
		{
			std::ifstream ifs(file);
			std::string line;
			std::string::iterator itr;
			uint64_t line_cnt = 0;
			std::list<char>::iterator itr_c;

			if (ifs.is_open()) {
				while(std::getline(ifs,line))
				{
					if (line_cnt) {
						output.clear();
						for(itr=line.begin();itr!=line.end();++itr)
						{
							compute(*itr);
						}
						std::cout << "Case #"<<line_cnt<<": ";
						for(itr_c = output.begin();itr_c != output.end();++itr_c)
						{
							std::cout << *itr_c;
						}
						std::cout << std::endl;
					}
					line_cnt++;
				}
			}
		}
	private:
		void compute(char c)
		{
			if (output.size() == 0) {
				output.push_back(c);
			} else {
				if (c >= *(output.begin())) {
					output.push_front(c);
				} else {
					output.push_back(c);
				}
			}
		}
		
	private:
		std::list<char> output;
		char* file;
};

int main(int argc, char* argv[])
{
	pr1 _pr1(argv[1]);
	_pr1.run();
	return 0;
}
