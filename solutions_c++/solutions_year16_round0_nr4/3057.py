#include"iostream"
#include"vector"
#include"unordered_set"
#include"unordered_map"
#include"string"
#include"cmath"
#include"algorithm"
using namespace std;
vector<bool> GenerateShape(const vector<bool> &OShape, const int C, const int CurrentC)
{
	if (C == CurrentC){ return OShape; }

	const int Size = OShape.size();

	vector<bool> Shape(OShape.size() * Size);

	int Index = 0;
	for (const auto &seek : OShape)
	{
		for (int seek_o = 0; seek_o < Size; seek_o = seek_o + 1)
		{
			Shape[Index] = seek ? true : OShape[seek_o];
			Index = Index + 1;
		}
	}

	return GenerateShape(Shape, C, CurrentC + 1);
}
void GenerateAllComb(vector<bool> &Shape, const int CurrentK, const int C, vector<vector<bool>> &ShapeSet)
{
	int K = Shape.size();

	if (CurrentK < K)
	{
		Shape[CurrentK] = true;
		GenerateAllComb(Shape, CurrentK + 1, C, ShapeSet);

		Shape[CurrentK] = false;
		GenerateAllComb(Shape, CurrentK + 1, C, ShapeSet);

		return;
	}

	ShapeSet.push_back(GenerateShape(Shape, C, 1));
}
void Solve(vector<pair<int, vector<int>>> PosArray, const int MaxS, int CurrentS, const int Index, vector<bool> AvailableArray, vector<int> &Result)
{
	if (!Result.empty()){ return; }

	if (CurrentS < MaxS)
	{
		if (Index >= AvailableArray.size()){ return; }

		AvailableArray[Index] = true;
		Solve(PosArray, MaxS, CurrentS + 1, Index + 1, AvailableArray, Result);

		AvailableArray[Index] = false;
		Solve(PosArray, MaxS, CurrentS, Index + 1, AvailableArray, Result);
		return; 
	}

	if (CurrentS != MaxS){ return; }

	//Solve
	vector<int> PSet;
	for (int seek = 0; seek < AvailableArray.size(); seek = seek + 1)
	{
		if (AvailableArray[seek])
		{
			PSet.push_back(seek);
		}
	}

	unordered_set<int> CommonArray(PosArray[PSet[0]].second.begin(), PosArray[PSet[0]].second.end());

	for (int seek = 0; seek < PSet.size(); seek = seek + 1)
	{
		unordered_set<int> Current;
		
		for (const auto & v : PosArray[PSet[seek]].second)
		{
			if (CommonArray.find(v) != CommonArray.end())
			{
				Current.insert(v);
			}
		}

		CommonArray = Current;

		if (CommonArray.empty())
		{ 
			Result = PSet;
			break; 
		}
	}

	return;
}
int main()
{
	int Times = 0;
	::cin >> Times;

	for (int seek = 0; seek < Times; seek = seek + 1)
	{
		int K;
		int C;
		int S;
		::cin >> K >> C >> S;

		/*vector<vector<bool>> ShapeSet;
		vector<bool> Shape(K, false);

		GenerateAllComb(Shape, 0, C, ShapeSet);

		const int SetSize = pow(K,C);
		const int Size = ShapeSet.size() - 1;

		vector<pair<int, vector<int>>> PosArray; // PosID, ShapeMiss
		unordered_map<int, vector<int>> HashMap; // ShapeID, PosID

		for (int seek_pos = 0; seek_pos < SetSize; seek_pos = seek_pos + 1)
		{
			vector<int> LArray;
			for (int seek_s = 0; seek_s < Size; seek_s = seek_s + 1)
			{
				if (ShapeSet[seek_s][seek_pos] == false)
				{
					LArray.push_back(seek_s);
				}
				else
				{
					HashMap[seek_s].push_back(seek_pos);
				}
			}
			PosArray.push_back(make_pair(seek_pos, LArray));
		}

		std::sort(PosArray.begin(), PosArray.end(), [](const pair<int, vector<int>> &P1, const pair<int, vector<int>> &P2){return P1.second.size() < P2.second.size(); });

		vector<int> Result;

		for (int seek = 0; seek < S; seek = seek + 1)
		{
			Result.clear();
			Solve(PosArray, seek + 1, 0, 0, vector<bool>(PosArray.size(), false), Result);

			if (!Result.empty()){ break; }
		}*/

		::cout << "Case #" << seek + 1 << ":";

		if (S < K)
		{
			::cout << " INSOMNIA" << endl;
		}
		else
		{
			unsigned long long Size = pow((unsigned long long)K,(unsigned long long)C - 1);

			for (int seek = 0; seek < S; seek = seek + 1)
			{ 
				::cout << " " << seek * Size + (Size / 2) + 1; 
			}
			::cout << endl;
		}

	}

	return 0;
}