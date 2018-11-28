#include <fstream>
using namespace std;
std::ifstream cin("input.txt");
namespace gcj 
{
	std::ofstream cout("output.txt");
}
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <thread>
#include <sstream>
#include <mutex>
#include <queue>

void init_global()
{

}

void init_thread_local()
{

}

class GCJSolverBase
{
public:
	void readData(int currentTest)
	{
		mTestNumber = currentTest;
		readTest();
	}

	std::string result()
	{
		cout << "Case #" << mTestNumber << ": ";
		solve();
		return cout.str();
	}
protected:
	std::ostringstream cout;
	int mTestNumber;

	virtual void readTest() = 0;
	virtual void solve() = 0;
};

class GCJSolver : public GCJSolverBase
{
public:
	GCJSolver()
	{

	}

private:
	int n;
	vector<int> v;

	void readTest() override
	{
		string str;
		cin >> str;
		n = int(str.length());
		v.resize(n);
		for (int i = 0; i < n; ++i)
		{
			if (str[i] == '+') v[i] = 0;
			else v[i] = 1;
		}
	}

	int bruteforce()
	{
		std::map<std::vector<int>, int> m;
		std::queue<std::vector<int>> q;
		q.push(v);
		m[v] = 0;
		while (!q.empty())
		{
			auto x = q.front();
			q.pop();

			int val = m[x];
			for (int i = 1; i <= n; ++i)
			{
				auto nx = x;
				std::reverse(nx.begin(), nx.begin() + i);
				std::transform(nx.begin(), nx.begin() + i, nx.begin(), [](int a) {return 1 - a; });
				if (m.find(nx) == m.end())
				{
					m[nx] = val + 1;
					q.push(nx);
				}
			}
		}
		return m[std::vector<int>(n, 0)];
	}

	void solve() override
	{
		int res = 0;
		for (int i = 1; i < n; ++i)
		{
			res += abs(v[i - 1] - v[i]);
		}
		res += (v[0] + res) % 2;
		cout << res;
	}
};

void thread_func(volatile int &current_test, int maxTest, std::vector<std::string> &result)
{
	init_thread_local();
	while (1)
	{
		GCJSolver s;
		int cur;
		{
			static std::mutex sInputMutex;
			std::lock_guard<std::mutex> lock(sInputMutex);
			if (current_test > maxTest) break;
			s.readData(current_test);
			cur = current_test;
			++current_test;
		}
		result[cur - 1] = s.result();
	}
}

int main()
{
	int totalTests;
	cin >> totalTests;
	init_global();
	std::vector<std::thread> vt;
	int currentTest = 1;
	std::vector<std::string> vs(totalTests);
	for (size_t i = 0; i != std::thread::hardware_concurrency(); ++i)
	{
		vt.push_back(std::thread(std::bind(thread_func, std::ref(currentTest), totalTests, std::ref(vs))));
	}
	for (auto &x : vt) x.join();
	for (auto s : vs) gcj::cout << s << '\n';
}
