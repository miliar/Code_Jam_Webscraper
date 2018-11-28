#include <tchar.h> 
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/join.hpp>
using namespace std;


namespace String
{
	vector<string> Split(const string& str, const string& sep)
	{
		vector<string> ret;
		boost::split(ret, str, boost::is_any_of(sep));
		return ret;
	}
	vector<string> Split(const string& str, const char sep)
	{
		char separray[2] = {sep, '\0'};
		string sepators = separray;
		return Split(str, sepators);
	}

	string Unsplit(const vector<string>& vals, const string& sep)
	{
		string str = boost::algorithm::join(vals, sep);
		return str;
	}
	string Unsplit(const vector<string>& vals, const char sep)
	{
		char separray[2] = {sep, '\0'};
		string sepators(separray);
		return Unsplit(vals, sepators);
	}
}

template<class T>
void splitstr(const string& s, vector<T>& out)
{
	stringstream in(s);
	out.clear();
	copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

int str2int(const string& str) 
{
	stringstream ss(str);
	int num;
	if ((ss >> num).fail())
	{ 
		//ERROR 
	}
	return num;
}

struct Matrix_
{
	size_t rows_, cols_;
	vector<vector<int> > m_;

	Matrix_(size_t rows, size_t cols, int val = 0)
		: rows_(rows), cols_(cols)
	{
		for (size_t i=0; i<rows_; i++)
		{
			vector<int> v(cols, val);
			m_.push_back(v);
		}
	}

	size_t Rows() const { return rows_;}
	size_t Cols() const { return cols_;}

	const int& operator() (size_t row, size_t col) const
	{
		assert(row < Rows());
		assert(col < Cols());
		return m_[row][col];
	}

	int& operator() (size_t row, size_t col)
	{
		assert(row < Rows());
		assert(col < Cols());
		return m_[row][col];
	}
};

bool CteRow(const Matrix_& m,int i, int val)
{
	bool ko = false;
	for (int j=0; !ko && j<m.Cols(); ++j)
	{
		ko = m(i,j)!=val;
	}
	return !ko;
}

bool CteCol(const Matrix_& m,int j, int val)
{
	bool ko = false;
	for (int i=0; !ko && i<m.Rows(); ++i)
	{
		ko = m(i,j)!=val;
	}
	return !ko;
}



std::ostream& operator <<(std::ostream& s, const Matrix_& m)
{
	s << "Matrix[" <<  m.Rows() << ", " << m.Cols() << "] =" << "\n";
	for (size_t i = 0 ; i < m.Rows(); i ++ )
	{
		for (size_t j = 0 ; j < m.Cols(); j ++ )
		{
			s << m(i, j) << ", ";
		}
		s << "\n";
	}
	s << "\n";
	return s;
}




string TestCase(ifstream& input)
{

	string line;
	vector<int> v;
	getline(input, line);
	splitstr(line, v);
	int N = v[0];
	int M = v[1];
	Matrix_ m(N, M, 0);
	for (int i=0; i<N; ++i)
	{
		getline(input, line);
		splitstr(line, v);
		for (int j=0; j<M; ++j)
			m(i,j) = v[j];
	}
	//cout << m << endl;

	bool ko = false;
	for (int i=0; !ko && i<N; ++i)
	{
		for (int j=0; !ko && j<M; ++j)
		{
			int val = m(i,j);
			if (m(i,j)==1)
				ko = CteRow(m,i,1)==false && CteCol(m,j,1)==false;				
		}
	}
	return ko ? "NO" : "YES";
}


int _tmain(int argc, _TCHAR* argv[])
{
	//ifstream input("B-large.in");
	ifstream input("B-small-attempt0.in");
	//ifstream input("test.in");

	ofstream myfile("result.txt");

	string line;
	getline(input, line);
	int T = str2int(line);
	cout << "number of cases : " << T << endl;

	for (int i = 0; i<T; i++)
	{
		string res = TestCase(input);
		cout << "Case #" << i+1 << ": "  << res << endl;
		myfile << "Case #" << i+1 << ": "  << res << endl;
	}
	myfile.close();

	return 0;
}
