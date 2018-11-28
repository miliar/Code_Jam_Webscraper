#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

struct Position
{
	unsigned x, y;
	Position(unsigned x, unsigned y) : x(x), y(y) {} // Prevent partial initialization
};

class Lawn
{
	std::vector<std::vector<unsigned>> m_matrix;

public:
	Lawn(const unsigned w, const unsigned h) :
		m_matrix()
	{
		m_matrix.resize(h);
		for (auto &row : m_matrix)
			row.resize(w);
	}

	unsigned getHeight() const
	{
		return m_matrix.size();
	}

	unsigned getWidth() const
	{
		if (!getHeight())
			return 0;

		return m_matrix[0].size();
	}

	unsigned getSquare(const Position &position) const
	{
		return m_matrix[position.y][position.x];
	}

	void setSquare(const Position &position, unsigned v)
	{
		m_matrix[position.y][position.x] = v;
	}
};

bool isSquarePossible(const Lawn &lawn, const Position &position)
{
	const auto highestPossibleHeight = lawn.getSquare(position);

	const bool isRowPossible = [&] ()
	{
		for (unsigned x = 0; x < lawn.getWidth(); ++x)
		{
			const auto currentHeight = lawn.getSquare({x, position.y});
			if (currentHeight > highestPossibleHeight)
				return false;
		}
		return true;
	}();

	const bool isColumnPossible = [&] ()
	{
		for (unsigned y = 0; y < lawn.getHeight(); ++y)
		{
			const auto currentHeight = lawn.getSquare({position.x, y});
			if (currentHeight > highestPossibleHeight)
				return false;
		}
		return true;
	}();

	return isRowPossible || isColumnPossible;
}

bool isLawnPossible(const Lawn &lawn)
{
	for (unsigned row = 0; row < lawn.getHeight(); ++row)
	{
		for (unsigned column = 0; column < lawn.getWidth(); ++column)
		{
			if (!isSquarePossible(lawn, {column, row}))
				return false;
		}
	}
	return true;
}

void test(const unsigned id)
{
	unsigned HEIGHT, WIDTH;
	std::cin >> HEIGHT >> WIDTH; // N x M
	Lawn lawn(WIDTH, HEIGHT);
	for (unsigned row = 0; row < HEIGHT; ++row)
	{
		for (unsigned column = 0; column < WIDTH; ++column)
		{
			unsigned grassHeight;
			std::cin >> grassHeight;
			lawn.setSquare({column, row}, grassHeight);
		}
	}

	std::cout << "Case #" << id << ": ";
	switch (isLawnPossible(lawn))
	{
	case true:
		std::cout << "YES" << std::endl;
		break;
	case false:
		std::cout << "NO" << std::endl;
		break;
	}
}

int main()
{
	unsigned testCount;
	std::cin >> testCount;

	for (unsigned i = 0; i < testCount; ++i)
		test(i+1);

	return 0;
}
