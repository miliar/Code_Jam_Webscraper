#include "stdafx.h"

#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <iomanip>

namespace CookieClickerAlpha {
	class TestCase {
	public:
		static const size_t initial_cookies_per_second = 2;

	public:
		TestCase(std::istream& input_stream) {
			std::string line;
			std::getline(input_stream, line);
			auto string_stream = std::istringstream(line);
			string_stream >> cost_ >> extra_cookies_ >> finish_;
		}

	public:
		double cost_;
		double extra_cookies_;
		double finish_;
	};

	class Input {
	public:
		Input(std::istream& input_stream) {
			std::string line;
			std::getline(input_stream, line);
			int num_of_test_cases;
			std::istringstream(line) >> num_of_test_cases;
			test_cases_.reserve(num_of_test_cases);
			for (auto i = 0; i < num_of_test_cases; ++i) {
				test_cases_.emplace_back(input_stream);
			}
		}

	public:
		std::vector<TestCase> test_cases_;
	};

	class Solution {
	public:
		virtual ~Solution() {}
		virtual std::string ToString() const = 0;
	};

	class TimeSolution : public Solution {
	public:
		TimeSolution(double time)
			: time_(time) {
		}

		std::string ToString() const override {
			auto output_stream = std::ostringstream();
			output_stream << std::fixed << std::setprecision(7) << time_;
			return output_stream.str();
		}

	public:
		double time_;
	};

	class Solver {
	public:
		std::shared_ptr<Solution> Solve(const TestCase& test_case) const {
			auto cost = test_case.cost_;
			const auto extra_cookies = test_case.extra_cookies_;
			const auto finish = test_case.finish_;
			auto cookies_per_second = static_cast<double>(TestCase::initial_cookies_per_second);

			auto prev_farm_build_time = 0.0;
			auto produce_time = finish / cookies_per_second;
			auto farm_build_time = cost / cookies_per_second;
			auto produce_time_with_farm = finish / (cookies_per_second + extra_cookies);
			while (farm_build_time + produce_time_with_farm < produce_time) {
				prev_farm_build_time += farm_build_time;
				cookies_per_second += extra_cookies;
				produce_time = finish / cookies_per_second;
				farm_build_time = cost / cookies_per_second;
				produce_time_with_farm = finish / (cookies_per_second + extra_cookies);
			}
			return std::make_shared<TimeSolution>(prev_farm_build_time + produce_time);
		}
	};
}

int main(int argc, char* argv[])
{
	if (argc < 1) {
		return 1;
	}
	auto input_stream = std::ifstream(argv[1]);
	auto input = CookieClickerAlpha::Input(input_stream);

	std::vector<std::shared_ptr<CookieClickerAlpha::Solution>> solutions;
	solutions.reserve(input.test_cases_.size());

	auto solver = CookieClickerAlpha::Solver();
	for (const auto& test_case : input.test_cases_) {
		solutions.push_back(solver.Solve(test_case));
	}

	size_t num_of_case = 1;
	for (const auto& solution : solutions) {
		std::cout << "Case #" << num_of_case << ": " <<
		solution->ToString() << '\n';
		++num_of_case;
	}

	return 0;
}

