#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstdio>
#include <assert.h>
using namespace std;

unordered_map<int, void (*)(ifstream&, ofstream&)> ProblemSet;

void solve()
{
	string file;
	string path = "C:\\Users\\Ben\\Downloads\\";
	int problemNum = 0;
	cin >> problemNum;
	getline (cin,file);
    ifstream infile;
	ofstream outfile;
	infile.open (path + file + ".in");
	outfile.open (file + ".out");
	int testCount;
	infile >> testCount;
	for(int i = 0; i < testCount; i++)
	{
		outfile << "Case #" << i+1 << ":";
		ProblemSet[problemNum](infile, outfile);
	}
	infile.close();
	outfile.close();
}
/*
class bigInt
{
public:
	bigInt ()
	{
		isPositive = true;
	}
	bigInt(int i)
	{
		isPositive = (i >= 0);
		digits.push_back(isPositive? i : -1*i);
	}
	bigInt operator++(int)
	{
		bigInt tmp(*this);
		operator++();
		return tmp;
	}
	bigInt operator--(int)
	{
		bigInt tmp(*this);
		operator--();
		return tmp;
	}
	bigInt (bigInt& other);
	int operator[](int idx) const;
	bigInt& operator=(bigInt rhs);
	bigInt& operator++();
	bigInt& operator--();
	bigInt& operator+=(const bigInt& rhs);
	bigInt& operator-=(const bigInt& rhs);
	inline bigInt& operator*=(const bigInt& rhs)
	{
		*this = *this * rhs;
		return *this;
	}
	bigInt& operator/=(bigInt rhs)
	{
		*this = *this / rhs;
		return *this;
	}
	bigInt& operator%=(bigInt rhs);
	friend istream& operator>> (istream &ist, bigInt& val);
	friend ostream& operator<< (ostream &ost, bigInt& val);
	friend inline bool operator==(const bigInt& lhs, const bigInt& rhs);
	friend inline bool operator< (const bigInt& lhs, const bigInt& rhs);
	friend inline bool operator!=(const bigInt& lhs, const bigInt& rhs){return !operator==(lhs,rhs);}
	friend inline bool operator> (const bigInt& lhs, const bigInt& rhs){return  operator< (rhs,lhs);}
	friend inline bool operator<=(const bigInt& lhs, const bigInt& rhs){return !operator> (lhs,rhs);}
	friend inline bool operator>=(const bigInt& lhs, const bigInt& rhs){return !operator< (lhs,rhs);}
	friend inline bigInt operator+(bigInt lhs, const bigInt& rhs)
	{
		lhs += rhs;
		return lhs;
	}
	friend inline bigInt operator-(bigInt lhs, const bigInt& rhs)
	{
		lhs -= rhs;
		return lhs;
	}
	friend bigInt operator*(const bigInt& lhs, const bigInt& rhs);
	friend bigInt operator/(bigInt lhs, bigInt rhs);
	friend inline bigInt operator%(bigInt lhs, bigInt rhs)
	{
		lhs %= rhs;
		return lhs;
	}
	
private:
	bigInt& add(const bigInt& rhs);
	bigInt& sub(const bigInt& rhs);
	void leftShift();
	void rightShift();
	bool greaterMagnitudeThan(const bigInt& rhs) const;
	vector<unsigned long long> digits;
	bool isPositive;
};
*/
template <class T>
class graph
{
public:
	graph()
	{
		nodeCount = 0;
	}
	void addEdge(T a, T b, int weight, bool bidirectional)
	{
		if(nodeNames.count(a) < 1)
		{
			nodeNames[a] = nodeCount++;
			getNames.push_back(a);
		}
		if(nodeNames.count(b) < 1)
		{
			nodeNames[b] = nodeCount++;
			getNames.push_back(b);
		}
		int na = nodeNames[a];
		int nb = nodeNames[b];
		if(edges.size() <= na)
			edges.resize(na + 1);
		if(edges.size() <= nb)
			edges.resize(nb + 1);
		edges[nodeNames[a]].push_back(make_pair(nodeNames[b], weight));
		if(bidirectional)
			edges[nodeNames[b]].push_back(make_pair(nodeNames[a], weight));
		if(weight > largestWeight)
			largestWeight = weight;
	}
	void addEdge(T a, T b, bool bidirectional)
	{
		addEdge(a, b, 1, bidirectional);
	}
	vector<T> shortestPath(T a, T b, bool weightsAreLengths)
	{
		assert(nodeNames.count(a) > 0);
		assert(nodeNames.count(b) > 0);
		int start = nodeNames[a];
		int finish = nodeNames[b];
		vector<int> lengths(nodeCount, -1);
		vector<int> source(nodeCount, -1);
		lengths[finish] = 0;
		bool changed = true;
		int iterations = 0;
		while(changed)
		{
			changed = false;
			for(int i = 0; i < nodeCount; i++)
			{
				for(int j = 0; j < edges[i].size(); j++)
				{
					int w = weightsAreLenghts? edges[i][j].second : 1;
					w += lengths[edges[i][j].first];
					if(w < lengths[i] || lengths[i] < 0)
					{
						lenghts[i] = w;
						source[i] = edges[i][j].first;
						changed = true;
					}
				}
			}
			iterations++;
			assert(iterations <= nodeCount);
		}
		vector<T> answer;
		while(start >= 0)
		{
			answer.push_back(getNames[start]);
			start = source[start];
		}
	}
	int maxFlow(T a, T b)
	{
		int answer = 0;
		assert(nodeNames.count(a) > 0);
		assert(nodeNames.count(b) > 0);
		int start = nodeNames[a];
		int finish = nodeNames[b];
		while(true)
		{
			vector<int> lengths(nodeCount, 0);
			vector<int> source(nodeCount, -1);
			lengths[finish] = largestWeight;
			bool changed = true;
			while(changed)
			{
				changed = false;
				for(int i = 0; i < nodeCount; i++)
				{
					for(int j = 0; j < edges[i].size(); j++)
					{
						int w = edges[i][j].second;
						assert(w >= 0);
						if(lengths[edges[i][j].first] < w)
							w = lengths[edges[i][j].first];
						if(w > lengths[i])
						{
							lengths[i] = w;
							source[i] = j;
							changed = true;
						}
					}
				}
			}
			int cap = lengths[start];
			if(cap <= 0)
				break;
			answer += cap;
			int curr = start;
			while(true)
			{
				if(source[curr] < 0)
					break;
				int n = edges[curr][source[curr]].second;
				int next = edges[curr][source[curr]].first;
				
				edges[curr][source[curr]] = make_pair(next, n - cap);
				int i;
				for(i = 0; i < edges[next].size(); i++)
				{
					if(edges[next][i].first == curr)
					{
						edges[next][i] = make_pair(curr, edges[next][i].second + cap);
						break;
					}
				}
				if(i >= edges[next].size())
					edges[next].push_back(make_pair(curr, cap));
				curr = next;
			}
		}
		return answer;
	}
private:
	vector<vector<pair<int, int> > > edges;
	unordered_map<T, int> nodeNames;
	vector<T> getNames;
	int nodeCount;
	int largestWeight;
};