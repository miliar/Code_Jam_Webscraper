#include <iostream>
#include <string>
#include <list>

using namespace std;

list <unsigned int> cnt;
list <list<unsigned int>> cntList;

int main()
{
	unsigned int T;
	unsigned int N;
	unsigned int len;
	unsigned int pos;
	unsigned int move;
	unsigned int med;
	unsigned int pivot, diff, finalDiff;
	string word;
	string check1, check2;
	cin >> T;

	for (unsigned int tc=1; tc <= T;tc++)
	{
		
		check1.clear();
		cnt.clear();
		cntList.clear();
		cin >> N;
		if (N == 1)
		{
			cout << "Case #" << tc << ": 0" << endl; 
		}
		else
		{
			for (unsigned int n=0;n<N;n++)
			{
				cin >> word;
				cnt.clear();
				len = word.size();
				pos = 0;
				if (n == 0)
				{
					while(pos < len)
					{
						if (check1.empty())
						{
							check1.push_back(word[pos]);
							cnt.push_back(1);
						}
						else if (word[pos] != check1.back())
						{
							check1.push_back(word[pos]);
							cnt.push_back(1);
						}
						else
						{
							cnt.back() = (cnt.back() + 1);
						}
						pos++;
					}
				}
				else
				{
					check2.clear();
					while(pos < len)
					{
						if (check2.empty())
						{
							check2.push_back(word[pos]);
							cnt.push_back(1);
						}
						else if (word[pos] != check2.back())
						{
							check2.push_back(word[pos]);
							cnt.push_back(1);
						}
						else
						{
							cnt.back() = (cnt.back() + 1);
						}
						pos++;
					}
					if (check1.compare(check2) != 0)
					{
						cout << "Case #" << tc << ": Fegla Won" << endl;
						goto __End;
					}
				}
				cntList.push_back(cnt);
			}
			// calculate min move
			move = 0;

			cntList.size();

			len = check1.size();
			pos = 0;

			while (pos < len)
			{
				cnt.clear();
				for (list<list<unsigned int>>::iterator it = cntList.begin(); it != cntList.end(); it++)
				{
					cnt.push_back((*it).front());
					(*it).pop_front();
				}
				cnt.sort();
				med = 0;
				for (list<unsigned int>::iterator itCnt = cnt.begin(); itCnt != cnt.end(); itCnt++)
				{
					med += *itCnt;
				}
				med /= cnt.size();
				
				finalDiff = 1000;
				for (list<unsigned int>::iterator itCnt = cnt.begin(); itCnt != cnt.end(); itCnt++)
				{
					diff = ((med > *itCnt) ? (med - *itCnt) : (*itCnt - med));
					if (diff < finalDiff)
					{
						finalDiff = diff;
						pivot = *itCnt;
					}
				}
				for (list<unsigned int>::iterator itCnt = cnt.begin(); itCnt != cnt.end(); itCnt++)
				{
					move += ((pivot > *itCnt) ? (pivot - *itCnt) : (*itCnt - pivot));
				}
				pos++;
			}

			cout << "Case #" << tc << ": " << move << endl;
			__End:
				;
		}
	}
	return 0;
}
