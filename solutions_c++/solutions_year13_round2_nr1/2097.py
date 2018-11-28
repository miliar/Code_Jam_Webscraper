#include <iostream>
#include <vector>

using namespace std;

int solve(int note, vector<int> notes)
{
	int ops = 0;
		
	while (!notes.empty())
	{
		int min = 10000000;
		int minPos = 0;
		for (int j = 0; j < (int) notes.size(); j++)
		{
			if (notes[j] < min)
			{
				min = notes[j];
				minPos = j;
			}
		}
		
		if (min < note)
		{
			note += min;
			notes.erase(notes.begin() + minPos);
		}
		else
		{
			vector<int> newNotes(notes);
			if (note >= 2)
			{
				newNotes.push_back(note - 1);
				int ops1 = solve(note, newNotes) + 1;
				newNotes.pop_back();
				newNotes.erase(newNotes.begin() + minPos);
				int ops2 = solve(note, newNotes) + 1;
				
				if (ops1 < ops2) return ops1;
				else return ops2;
			}
			else
			{
				newNotes.erase(newNotes.begin() + minPos);
				return solve(note, newNotes) + 1;
			}
		}
			
	}
	
	return ops;
}

int main()
{
	int cases;
	cin >> cases;
	
	for (int i = 1; i <= cases; ++i)
	{
		int note;
		int nrOfNotes;
		cin >> note >> nrOfNotes;
		vector<int> notes;
		
		for (int j = 0; j < nrOfNotes; j++)
		{
			int n;
			cin >> n;
			notes.push_back(n);
		}
		
		int ops = solve(note, notes);
		
		cout << "Case #" << i << ": " << ops << endl;		
		
	}
	
	return 0;
}
