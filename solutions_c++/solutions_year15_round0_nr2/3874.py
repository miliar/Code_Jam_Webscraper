
#define PROBLEM_NAME "B"
#define PROBLEM_SMALL_INPUT "-small-attempt3"
#define PROBLEM_LARGE_INPUT "-large"

#include <set>
#include <vector>

void insertionSort(vector<int>& A)
{
   int i, key, j;
   int size = (int)A.size();
   for (i = 1; i < size; i++)
   {
       key = A[i];
       j = i-1;
 
       /* Move elements of A[0..i-1], that are greater than key, to one 
          position ahead of their current position.
          This loop will run at most k times */
       while (j >= 0 && A[j] > key)
       {
           A[j+1] = A[j];
           j = j-1;
       }
       A[j+1] = key;
   }
}

inline int min(int a, int b) { return (a>b) ? b : a; }

int FindMinimum(vector<int>& A)
{
	int back = A.back();

	if (back <= 3)
		return back;

	// 1.
	int minWithoutDividing = A.back();

	// 2.
	vector<int> B = A;
	int a = back / 2;
	int b = back - a;
	B.pop_back();
	B.push_back(a);
	B.push_back(b);
	insertionSort(B);
	int minWithDividing1 = FindMinimum(B) + 1;

	// 3.
	vector<int> C = A;
	a = back - 3;
	b = 3;
	C.pop_back();
	C.push_back(a);
	C.push_back(b);
	insertionSort(C);
	int minWithDividing2 = FindMinimum(C) + 1;

	// 4.
	//vector<int> D = A;
	//a = back - 2;
	//b = 2;
	//D.pop_back();
	//D.push_back(a);
	//D.push_back(b);
	//insertionSort(D);
	//int minWithDividing3 = FindMinimum(D) + 1;

//	return min(minWithoutDividing, min(minWithDividing1, min(minWithDividing2, minWithDividing3)));
	return min(minWithoutDividing, min(minWithDividing1, minWithDividing2));
}


//int FindMinimumNonRecursive(vector<int>& A)
//{
//	while (true)
//	{
//		int back = A.back();
//
//		if (back <= 3)
//			return back;
//
//		// 1.
//		int minWithoutDividing = A.back();
//
//		// 2.
//		int a = back / 2;
//		int b = back - a;
//		A.pop_back();
//		A.push_back(a);
//		A.push_back(b);
//		insertionSort(A);
//		int minWithDividing = FindMinimum(A) + 1;
//	}
//
//	return (minWithDividing > minWithoutDividing) ? minWithoutDividing : minWithDividing;
//}


int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		int D;
		fin >> D;

		std::vector<int> diner;
		diner.reserve(D);

		//bool isLEQ2 = false;
		int minutes = 0;
		int a;
		//int sub_minutes = 0;
		for (int i=0; i<D; ++i)
		{
			fin >> a;
			diner.push_back(a);
			//if (a >= 2)
			//{
			//	isLEQ2 = true;
			//}

			//if (a > 2)
			//{
			//	sub_minutes = (a + 1)/2 - 1;
			//	minutes += sub_minutes;
			//}
		}

		std::vector<int> A = diner;

		insertionSort(A);
		minutes = FindMinimum(A);

		//if (!isLEQ2)
		//{
		//	fout << "Case #" << cases << ": " << 1 << endl;
		//	fout << D << " isLEQ2 == false" << endl;
		//	for (size_t i=0; i<diner.size(); ++i)
		//	{
		//		fout << diner[i] << " ";
		//	}
		//	fout << endl;
		//	fout << endl;
		//}
		//else
		//{
		//	fout << "Case #" << cases << ": " << (minutes+2) << endl;
		//	fout << D << endl;
		//	for (size_t i=0; i<diner.size(); ++i)
		//	{
		//		fout << diner[i] << " ";
		//	}
		//	fout << endl;
		//	fout << endl;
		//}

		//int minutes = 0;
		//switch (maxCakes)
		//{
		//case 1: minutes = 1; break;
		//case 2: minutes = 2; break;
		//case 3: minutes = 3; break;
		//case 4: minutes = 3; break;
		//case 5: minutes = 4; break;
		//case 6: minutes = 4; break;
		//case 7: minutes = 4; break;
		//case 8: minutes = 4; break;
		//case 9: minutes = 5; break;
		//}

		fout << "Case #" << cases << ": " << minutes << endl;
		//for (size_t i=0; i<diner.size(); ++i)
		//{
		//	fout << diner[i] << " ";
		//}
		//fout << endl;
		//fout << endl;
	}

	return 0;
}
