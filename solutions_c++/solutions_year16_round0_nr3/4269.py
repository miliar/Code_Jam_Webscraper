#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <bitset>
#include <algorithm>
#include <functional>
#include <unordered_map>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <assert.h>
#include <string.h>
#include <thread>
#include <mutex>
#include <memory>
#include <chrono>
using namespace std;

#define MAX 1000000

long long GetDivisor(long long n)
{
	for(long long i=2; i <= n/i; i++)
		if(n%i == 0)
		{
			return i;
		}

	return -1;
}

long long ConvertToBase10(string s, int base)
{
	long long p=1, res=0;
	for(int i=0; i < s.size(); i++)
	{
		if(s[i]=='1')
			res += p;

		p*=base;
	}

	return res;
}

vector<pair<string, vector<long long>>> out;
void Process(string s)
{
	vector<long long> divs;
	for (int i=2; i <= 10; i++)
	{
		long long divisor = GetDivisor(ConvertToBase10(s, i));

		if(divisor == -1)
			return ;

		divs.push_back(divisor);
	}

	reverse(s.begin(), s.end());
	out.push_back(pair<string,vector<long long>>(s, divs));
}

void generate(string s, int idx, int n, int j)
{
	if(out.size() < j)
	{
		if (idx >= n)
		{
			Process("1"+s+"1");
			return ;
		}

		generate("0"+s, idx+1, n, j);
		generate("1"+s, idx+1, n, j);
	}
}

int main()
{
#ifndef ONLINE_JUDGE
#pragma warning (disable : 4996)
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin>>t;

	for(int i=1; i <= t; i++)
	{
		int j,n;
		cin>>n>>j;

		cout<<"Case #"<<i<<": "<<endl;
		generate("", 0, n-2, j);

		for(int i=0; i<out.size(); i++)
		{
			cout<<out[i].first<<" ";
			for(int j=0; j < out[i].second.size(); j++)
			{
				if(j != 0)
					cout<<" ";
				cout<<out[i].second[j];
			}
			cout<<endl;
		}
	}
}

/*
mutex barrier;
void sum(int a, int &sum)
{
	lock_gaurd<mutex> mylock(barrier);

	sum+=a;
}

int main()
{
	int thesum=0;
	int arr[] = {1,2,3,4};
	vector<thread> threads;

	for(int i=0; i < 4; i++)
	{
		//thread sumthread(sum, arr[i], thesum);
		threads.push_back(thread(sum,arr[i], sum));
	}

	for(int i=0; i < 4; i++)
	{
		threads[i].join();
	}

	ifstream input;
	input.open("bigfile.txt");

	int sum=0, a=0;
	while(input>>a)
	{
		sum+=a;
	}

	ofstream output;
	output.open("resultfile.txt");

	output<<sum<<endl;
}
*/

/*
int main()
{
	vector<vector<string> > tmp = { {"a", "b", "c"}, {"d", "e", "f"}, {"g", "h", "k"} };

	for each (vector<string> list in tmp)
	{
		cout << [list]()
		{
			string x = "";
			for each(string elm in list)
			{
				x += elm;
			}

			return x;
		}()
		<< endl;
	}
}
*/

/*
std::mutex m;
std::condition_variable cv;
std::string dataa;
bool ready = false;
bool processed = false;

void worker_thread()
{
	// Wait until main() sends data
	std::unique_lock<std::mutex> lk(m);
	cv.wait(lk, [] {return ready; });

	// after the wait, we own the lock.
	std::cout << "Worker thread is processing data\n";
	dataa += " after processing";

	// Send data back to main()
	processed = true;
	std::cout << "Worker thread signals data processing completed\n";

	// Manual unlocking is done before notifying, to avoid waking up
	// the waiting thread only to block again (see notify_one for details)
	lk.unlock();
	cv.notify_one();
}

int main()
{
	std::thread worker(worker_thread);

	dataa = "Example data";
	// send data to the worker thread
	{
		std::lock_guard<std::mutex> lk(m);
		ready = true;
		std::cout << "main() signals data ready for processing\n";
	}
	cv.notify_one();

	// wait for the worker
	{
		std::unique_lock<std::mutex> lk(m);
		cv.wait(lk, [] {return processed; });
	}
	std::cout << "Back in main(), data = " << dataa << '\n';

	worker.join();
}
*/

/*
static const int num_threads = 10;
mutex testMutex;

//This function will be called from a thread

void call_from_thread(int tid, int k) {
	//{
		lock_guard<mutex> myLockGaurd(testMutex);
	//}

	cout << "Launched by thread " << tid << endl;
}

int main() {
	thread t[num_threads];

	//Launch a group of threads
	for (int i = 0; i < num_threads; ++i) {
		t[i] = thread(call_from_thread, i, 0);
	}

	//cout << "Launched from the main" << endl;

	//Join the threads with the main thread
	for (int i = 0; i < num_threads; ++i) {
		t[i].join();
	}

	return 0;
}
*/

/*
// How to use Mutex
static std::mutex barrier;

//This function will be called from a thread

void dot_product(const std::vector<int> &v1, const std::vector<int> &v2, int &result, int L, int R)
{
	int partial_sum = 0;
	for (int i = L; i < R; ++i)
	{
		partial_sum += v1[i] * v2[i];
	}

	std::lock_guard<std::mutex> block_threads_until_finish_this_job(barrier);
	result += partial_sum;
}

int main() {
	int nr_elements = 100000;
	int nr_threads = 2;
	int result = 0;
	std::vector<std::thread> threads;

	//Fill two vectors with some constant values for a quick verification
	// v1={1,1,1,1,...,1}
	// v2={2,2,2,2,...,2}
	// The result of the dot_product should be 200000 for this particular case
	std::vector<int> v1(nr_elements, 1), v2(nr_elements, 2);

	//Split nr_elements into nr_threads parts
	std::vector<int> limits;
	for (int i = 0; i <= nr_elements; i += (nr_elements / nr_threads))
	{
		limits.push_back(i);
	}

	//Launch nr_threads threads:
	for (int i = 0; i < nr_threads; ++i) {
		threads.push_back(std::thread(dot_product, std::ref(v1), std::ref(v2), std::ref(result), limits[i], limits[i + 1]));
	}

	//Join the threads with the main thread
	for (auto &t : threads) {
		t.join();
	}

	//Print the result
	std::cout << result << std::endl;

	return 0;
}
*/

/*
template <typename T>
T reserve(unsigned int size)
{
	return (T)(malloc(size));
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
#ifndef ONLINE_JUDGE
#pragma warning (disable : 4996)
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
#endif

	int* x = reserve<int*>(sizeof(int [5]));

	cout << x << endl;
}
*/
