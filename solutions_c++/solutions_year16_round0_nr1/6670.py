#include <fstream>
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

	void readTest() override
	{
		cin >> n;
	}

	void solve() override
	{
		if (n == 0)
		{
			cout << "INSOMNIA";
			return;
		}
		bool f[10];
		int total = 0;
		for (int i = 0; i < 10; ++i) f[i] = false;
		int i = 1;
		while (total < 10)
		{
			int x = n * i;
			while (x)
			{
				int d = x % 10;
				if (!f[d])
				{
					f[d] = true;
					++total;
				}
				x /= 10;
			}
			++i;
		}
		cout << n * (i - 1);
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
