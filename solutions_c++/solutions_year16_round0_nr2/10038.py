#include <iostream>
#include <string>

using namespace std;

class BitArray
{
public:
	BitArray()
	{
		m_data_low = 0;
		m_data_high = 0;
	}
	void setSize(int size)
	{
		m_size = size;
	}
	bool getBit(int num)
	{
		if (num >= 64) {
			return (m_data_high & (1 << num - 64));
		}
		return (m_data_low & (1 << num));
	}
	void setBit(int num)
	{
		if (num >= 64) {
			m_data_high |= (1 << num - 64);
			return;
		}
		m_data_low |= (1 << num);
	}
	void clearBit(int num)
	{
		if (num >= 64) {
			m_data_high &= ~(1 << num - 64);
			return;
		}
		m_data_low &= ~(1 << num);
	}
	bool isZero()
	{
		return m_data_low == 0 && m_data_high == 0;
	}
	void flip(int flip_end)
	{
		BitArray original(*this);
		for (int i = flip_end; i < m_size; i++) {
			if (original.getBit(m_size - 1 - i + flip_end)) {
				clearBit(i);
			} else {
				setBit(i);
			}
		}
	}
	int m_size;
	unsigned long long m_data_low;
	unsigned long long m_data_high;
};

class Solver
{
public:
	Solver()
	{
		flip_count = 0;
	}
	void getInput()
	{
		string raw;
		cin >> raw;
		m_array.setSize(raw.size());
		for (int i = 0; i < raw.size(); i++) {
			if (raw[raw.size() - i - 1] == '-')
				m_array.setBit(i);
		}
	}
	void solve()
	{
		int not_zero_tail = 0;
		while (!m_array.isZero()) {
			while (!m_array.getBit(not_zero_tail)) {
				not_zero_tail++;
			}
			if (m_array.getBit(m_array.m_size-1)) {
				m_array.flip(not_zero_tail);
			} else {
				int flip_end = m_array.m_size-1;
				while (!m_array.getBit(flip_end-1)) {
					flip_end--;
				}
				m_array.flip(flip_end);
			}
			flip_count++;
		}
		cout << flip_count;
	}
	BitArray m_array;
	int flip_count;
};

int main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		Solver mySolver;
		mySolver.getInput();
		cout << "Case #" << i + 1 << ": ";
		mySolver.solve();
		cout << endl;
	}
	return 0;
}