#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>

#define VECTOR_RESERVE_SIZE	1000
#define USE_BRUTEFORCE

#ifdef USE_BRUTEFORCE
#ifndef _DEBUG
#define MULTITHREADED
#endif
#endif

#ifdef MULTITHREADED
#define NB_THREADS	8

#include <thread>
#include <mutex>
#endif

using namespace std;



int getMaxInRange(const vector<int>& pancakes, int start, int end)
{
	int max = INT_MIN;
	for (int i = start; i < end; i++)
	{
		int val = pancakes[i];
		if (val > max)
			max = val;
	}
	return max;
}
int getWaitingCost(const vector<int>& pancakes)
{
	return getMaxInRange(pancakes, 0, (int)pancakes.size());
}
ostream& operator<<(ostream& os, const vector<int>& vect)
{
	int vectSize = vect.size();
	for (int i = 0; i < vectSize; i++)
	{
		os << vect[i];
		if (i != vectSize - 1)
			os << " ";
	}
	return os;
}
#ifdef USE_BRUTEFORCE
int bruteforce(vector<int>& pancakes, int wordIdx = 0)
{
	if (wordIdx >= (int)pancakes.size())
		return getWaitingCost(pancakes);
	//cerr << pancakes << endl;

	// Cas i = 0 : Pas d'ajout de valeur
	int minVal = bruteforce(pancakes, wordIdx + 1);

	// Cas i > 0 : On démarre à partir de la plus grande valeur à notre gauche
	int initialVal = pancakes[wordIdx];
	int startVal = 1;
	if (wordIdx > 0)
		startVal = getMaxInRange(pancakes, 0, wordIdx);
	for (int i = startVal; i < initialVal; i++)
	{
		int res = INT_MAX;
		if (i > 0)
		{
			pancakes[wordIdx] = i;
			pancakes.push_back(initialVal - i);

			res = bruteforce(pancakes, wordIdx + 1) + 1;

			pancakes.pop_back();
			pancakes[wordIdx] = initialVal;
		}
		else
			res = bruteforce(pancakes, wordIdx + 1);

		if (res < minVal)
			minVal = res;
	}
	return minVal;
}
#else
bool shouldDivide(vector<int>& pancakes, vector<int>::iterator& outMaxElt)
{
	outMaxElt = max_element(pancakes.begin(), pancakes.end());
	int lastVal = *outMaxElt;
	(*outMaxElt) -= lastVal / 2;
	int newMaxVal = *max_element(pancakes.begin(), pancakes.end());
	(*outMaxElt) = lastVal;
	return (newMaxVal + 1 < lastVal);
}
void divideByHalf(vector<int>& pancakes, vector<int>::iterator& elt)
{
	int movedQtty = (*elt) / 2;
	(*elt) -= movedQtty;
	pancakes.push_back(movedQtty);
}
#endif

#ifdef MULTITHREADED
struct Input
{
	bool used;
	vector<int> pancakes;

	int eval;

	Input() : used(false), eval(0) { }
};
Input inputs[100];
int results[100];
mutex workList_mutex;
vector<int> workList;
int workEval(const vector<int>& pancakes)
{
	int size = pancakes.size();
	int eval = size;
	for (int i = 0; i < size; i++)
	{
		int val = pancakes[i];
		eval += val;
	}
	return eval;
}
int getWork()
{
	workList_mutex.lock();

	int work = -1;
	int workListSize = workList.size();
	if (workListSize > 0)
	{
		work = workList[workListSize - 1];
		workList.pop_back();
	}

	workList_mutex.unlock();

	return work;
}
void threadCompute()
{
	int work = getWork();
	while (work != -1)
	{
		results[work] = bruteforce(inputs[work].pancakes);
		cerr << work + 1 << " done." << endl;

		work = getWork();
	}
}
class WorkComparator
{
public:
	bool operator()(int left, int right) const
	{
		return inputs[left].eval < inputs[right].eval;
	}
};
void sortWorks()
{
	workList.reserve(100);
	for (int i = 0; i < 100; i++)
	{
		if (inputs[i].used)
		{
			workList.push_back(i);
			inputs[i].eval = workEval(inputs[i].pancakes);
		}
	}

	WorkComparator wc;
	sort(workList.begin(), workList.end(), wc);
}
/*
void threadCompute(const vector<int>& workList)
{
	int workListSize = (int)workList.size();
	for (int i = 0; i < workListSize; i++)
	{
		int idx = workList[i];
		results[idx] = bruteforce(inputs[idx].pancakes);
		cerr << idx + 1 << " done." << endl;
	}
}
int argmin(int* tab, int size)
{
	int minVal = tab[0];
	int minIdx = 0;
	for (int i = 0; i < size; i++)
	{
		int val = tab[i];
		if (val < minVal)
		{
			minVal = val;
			minIdx = i;
		}
	}
	return minIdx;
}
void assignWorkLists(vector<int>* workLists)
{
	int workTotal[NB_THREADS] = { 0 };
	for (int i = 0; i < NB_THREADS; i++)
		workLists[i].reserve(100);
	for (int i = 0; i < 100; i++)
	{
		if (!inputs[i].used)
			return;

		int minIdx = argmin(workTotal, NB_THREADS);
		int eval = workEval(inputs[i].pancakes);
		workLists[minIdx].push_back(i);
		workTotal[minIdx] += eval;
	}
}
*/
#endif
int main()
{
	int nbTests;
	cin >> nbTests;
#ifndef MULTITHREADED
	for (int testId = 0; testId < nbTests; testId++)
	{
		vector<int> pancakes;
		pancakes.reserve(VECTOR_RESERVE_SIZE);
		int D;
		cin >> D;
		pancakes.resize(D);
		for (int i = 0; i < D; i++)
			cin >> pancakes[i];

		// Trie la liste des pancakes
		sort(pancakes.begin(), pancakes.end(), greater<>());

#ifndef USE_BRUTEFORCE
		int turnsCount = 0;
		vector<int>::iterator maxElt;
		while (shouldDivide(pancakes, maxElt))
		{
			divideByHalf(pancakes, maxElt);
			turnsCount++;
		}
		turnsCount += getWaitingCost(pancakes);
		cout << "Case #" << testId + 1 << ": " << turnsCount << endl;
#else
		cout << "Case #" << testId + 1 << ": " << bruteforce(pancakes) << endl;
#endif
	}
#else
	for (int testId = 0; testId < nbTests; testId++)
	{
		inputs[testId].used = true;
		inputs[testId].pancakes.reserve(VECTOR_RESERVE_SIZE);
		int D;
		cin >> D;
		inputs[testId].pancakes.resize(D);
		for (int i = 0; i < D; i++)
			cin >> inputs[testId].pancakes[i];

		// Trie la liste des pancakes
		sort(inputs[testId].pancakes.begin(), inputs[testId].pancakes.end(), greater<>());
	}

	//vector<int> workLists[NB_THREADS];
	//assignWorkLists(workLists);

	sortWorks();

	thread* threads[NB_THREADS];
	const int resultsPerThread = nbTests / NB_THREADS;
	for (int i = 0; i < NB_THREADS; i++)
		threads[i] = new thread(threadCompute);

	for (int i = 0; i < NB_THREADS; i++)
	{
		threads[i]->join();
		delete (threads[i]);
	}

	for (int testId = 0; testId < nbTests; testId++)
		cout << "Case #" << testId + 1 << ": " << results[testId] << endl;
#endif

#ifdef _DEBUG
	_CrtDbgBreak();
#endif
	return EXIT_SUCCESS;
}
