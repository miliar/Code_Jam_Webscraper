// Haircut.cpp : Defines the entry point for the console application.
#include <fstream>
#include "stdint.h"
#include <iterator>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>
#include <queue>
#include <iterator>
#include <set>
#include <string>

//The first line of the input file contains integer number T - the number of test cases. 
//For each test case, the first line contains integer number n. 
//The next two lines contain n integers each, giving the coordinates of v1 and v2 respectively. 
template <typename T>
struct TestCase
{
	std::string pancakes_;
   
	friend std::istream& operator>>(std::istream & is, TestCase &test_case)
	{
	   std::string line;
	   //std::getline(is, line);

	   //parseNumOfData(line, test_case);

	   std::getline(is, line);
	   TestCase::parseData(line,test_case);

	   return is;
	}

	static void parseData(const std::string &line, 
		TestCase &test_case)
	{
		std::istringstream iss(line);
		T item;
		size_t i = 0;
		while (iss >> item)
		{
			test_case.pancakes_=item;
		}

		return ;
	}

};

template <typename T>
class TestCaseResult
{
	std::vector<T> data_;

	friend std::ostream& operator<<(std::ostream &os,
		const TestCaseResult<T> & result)
	{
			std::copy(
				result.data_.begin(),
				result.data_.end(),
				std::ostream_iterator<T>(os, " "));

			return os;
	}

  public:
	  void addResult(const T& result)
	  {
		  data_.push_back(result);
	  }

};

template<typename In,typename Out>
class Pancakes
{
public:
	TestCaseResult<Out> operator()(TestCase<In> &test_case)
	{
		TestCaseResult<Out> test_case_result;

		size_t count_changes = 0;
		char prev_char;
		auto it = test_case.pancakes_.begin();
		if (it!=test_case.pancakes_.end())
		{
			prev_char = *it;
		}
		
		for(auto & current_char : test_case.pancakes_)
		{
			if (current_char!=prev_char)
			{
				++count_changes;
			}
			prev_char = current_char;
		}

		auto rit = test_case.pancakes_.rbegin();
		if (*rit == '-')
		{
			++count_changes;
		}

		
		test_case_result.addResult(std::to_string(count_changes));

		return test_case_result;
	}
};


template <typename In,typename Out>
class ProblemSolver
{
private:
	std::vector<TestCase<In>> test_cases_;
	std::vector<TestCaseResult<Out>> test_case_results_;
	std::string input_file_name_;
	std::string output_file_name_;
	std::function <TestCaseResult<Out>(TestCase<In>&)> algorithm_;
    
	void parseTestCases()
	{
		std::ifstream input_file(input_file_name_);
		uint64_t num_of_test_cases = 0;
		
		if (input_file.is_open())
		{
			std::string line;

			std::getline(input_file, line);
			std::istringstream iss(line);
			iss >> num_of_test_cases;

			for (uint64_t count = 0; count < num_of_test_cases; ++count)
			{
				std::copy(
					std::istream_iterator<TestCase<In>>(input_file),
					std::istream_iterator<TestCase<In>>(),
					std::back_inserter(test_cases_));
			}
			input_file.close();
		}
	}

	void applyAlgorithm()
	{		
		std::transform(begin(test_cases_), end(test_cases_),
			std::back_inserter(test_case_results_),algorithm_ );
	}

	void printResults()
	{
		//Print results
		std::ofstream output_file(output_file_name_);
		size_t result_num = 0;

		for (auto & result : test_case_results_)
		{
			output_file << "Case #" << ++result_num << ": " 
				<< result << std::endl;;
		}
		output_file.close();
	}


public:
	ProblemSolver(const char *input_file_name,
		const char *output_file_name,
		std::function <TestCaseResult<Out>(TestCase<In>&)> algorithm) :
		input_file_name_(input_file_name),
		output_file_name_(output_file_name),
		algorithm_(algorithm)
	{}

	void run()
	{
		parseTestCases();
		applyAlgorithm();
		printResults();
	}

};



int main(int argc, char* argv[])
{

	if (argc < 2)
	{
		std::cout << 
			"File name must be provided as a programm argument!" <<
			std::endl;

		return 1;
	}

	ProblemSolver<std::string, std::string> solver(argv[1], "output.txt",
												Pancakes<std::string, std::string>());

	solver.run();

	return 0;
}

