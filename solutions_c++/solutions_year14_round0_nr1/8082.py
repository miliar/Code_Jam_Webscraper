#include "stdafx.h"

#include <array>
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <fstream>
#include <memory>
#include <set>

namespace MagicTrick {
	class CardGuess {
	public:
		static const size_t square_size = 4;

	public:
		CardGuess(std::istream& input_stream) {
			std::string line;
			std::getline(input_stream, line);
			std::istringstream(line) >> answer_;
			for (auto& row : cards_) {
				std::getline(input_stream, line);
				auto string_stream = std::istringstream(line);
				auto stream_iterator = std::istream_iterator<int>(string_stream);
				std::copy(stream_iterator, std::istream_iterator<int>(), row.begin());
			}
		}

	public:
		int answer_;
		std::array<std::array<int, square_size>, square_size> cards_;
	};

	class TestCase {
	public:
		TestCase(std::istream& input_stream)
			: first_guess_(input_stream)
			, second_guess_(input_stream)
		{
		}

	public:
		CardGuess first_guess_;
		CardGuess second_guess_;
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

	class SingleSolution : public Solution {
	public:
		SingleSolution(int card)
			: card_(card) {
		}

		std::string ToString() const override {
			auto output_stream = std::ostringstream();
			output_stream << card_;
			return output_stream.str();
		}

	public:
		int card_;
	};

	class MultipleSolution : public  Solution {
	public:
		std::string ToString() const override {
			return "Bad magician!";
		}
	};

	class NoSolution : public Solution {
	public:
		std::string ToString() const override {
			return "Volunteer cheated!";
		}
	};

	class Solver {
	public:
		std::shared_ptr<Solution> Solve(const TestCase& test_case) const {
			const auto& first_row = test_case.first_guess_.cards_[test_case.first_guess_.answer_ - 1];
			const auto& second_row = test_case.second_guess_.cards_[test_case.second_guess_.answer_ - 1];
			auto first_cards = std::set<int>(first_row.begin(), first_row.end());
			auto second_cards = std::set<int>(second_row.begin(), second_row.end());
			auto intersection = std::vector<int>();
			std::set_intersection(first_cards.begin(), first_cards.end(),
				second_cards.begin(), second_cards.end(),
				std::back_inserter(intersection));

			if (intersection.size() == 1) {
				return std::make_shared<SingleSolution>(intersection.at(0));
			}
			else if (intersection.empty()) {
				return std::make_shared<NoSolution>();
			}
			else {
				return std::make_shared<MultipleSolution>();
			}
		}
	};
}


int main(int argc, char* argv[])
{
	if (argc < 1) {
		return 1;
	}
	auto input_stream = std::ifstream(argv[1]);
	auto input = MagicTrick::Input(input_stream);

	std::vector<std::shared_ptr<MagicTrick::Solution>> solutions;
	solutions.reserve(input.test_cases_.size());

	auto solver = MagicTrick::Solver();
	for (const auto& test_case : input.test_cases_) {
		solutions.push_back(solver.Solve(test_case));
	}

	size_t num_of_case = 1;
	for (const auto& solution : solutions) {
		std::cout << "Case #" << num_of_case << ": " << solution->ToString() << '\n';
		++num_of_case;
	}

	return 0;
}

