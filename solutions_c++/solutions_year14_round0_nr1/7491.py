#include <set>
#include <vector>
#include <cstdio>
#include <string>
#include <iostream>
#include <map>

#define _DEBUG 0

using namespace std;

typedef set<int> tCardSet[4];
typedef enum { found, notfound, cheat} tenResultType;
typedef struct
{
	tCardSet cardset1;
	tCardSet cardset2;
	int row1;
	int row2;
} tstInput;
typedef struct
{
	tenResultType type;
	int cardno;
} tstResult;

void vGetInput(tstInput & in)
{
	int j,k;
	int n;
	
	cin >> in.row1;
	for (j=0;j<4;++j)
		for (k=0;k<4;++k)
		{
			cin >> n;
			in.cardset1[j].insert(n);
		}
	cin >> in.row2;
	for (j=0;j<4;++j)
		for (k=0;k<4;++k)
		{
			cin >> n;
			in.cardset2[j].insert(n);
		}
}
void vGetResult(tstInput & in, tstResult & out)
{
	set<int>::iterator it;
	out.type = notfound;
	out.cardno = -1;
	map<int,int> count;
	int totalmatch = 0;
	int lastmatch = -1;
	
	int row1 = in.row1 - 1;
	int row2 = in.row2 - 1;
	
	for (it=in.cardset1[row1].begin(); it!=in.cardset1[row1].end(); ++it)
	{
		int c = in.cardset2[row2].count(*it);
		if (c)
		{
			count[*it] += c;
			++totalmatch;
			lastmatch = *it;
#if _DEBUG
printf("%d : linematch == %d, totalmatch == %d, lastmatch = %d\n", *it, c, totalmatch, lastmatch);
#endif
		}
	}
	
	if (totalmatch == 1)
	{	
		out.type = found;
		out.cardno = lastmatch;
	}
	else if (totalmatch == 0)
	{	
		out.type = cheat;
	}
	else
	{
		out.type = notfound;
	}
}

void vPrintResult(int c, tstResult & r)
{
	cout << "Case #" << c << ": ";
	switch (r.type)
	{
		case found:
			cout << r.cardno;
			break;
		case cheat:
			cout << "Volunteer cheated!";
			break;
		default:
		case notfound:
			cout << "Bad magician!";
			break;
	}
	cout << endl;		
}

int main()
{
	int n;
	int i;
	
	cin >> n;
	
	for (i=1;i<=n;++i)
	{
		tstInput in;
		tstResult res;
		vGetInput(in);
		vGetResult(in, res);
		vPrintResult(i, res);
	}

	return 0;
}