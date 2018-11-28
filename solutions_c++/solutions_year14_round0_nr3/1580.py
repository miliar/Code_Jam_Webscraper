#include <iostream>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;

int kXInc[] = { -1, 0, 1, -1, 1, -1, 0, 1 };
int kYInc[] = { -1, -1, -1, 0, 0, 1, 1, 1 };

unsigned R, C, M;

class Node {
public:
	char grid[50][50];
	unsigned x, y;
	unsigned click_x, click_y;
	unsigned nrVisible;

public:
	Node()
	{
		memset(grid, 1, sizeof(grid));
		x = 0;
		y = 0;
		nrVisible = 0;
		click_x = 0;
		click_y = 0;
	}
	Node(Node* n)
	{
		memcpy(grid, n->grid, sizeof(grid));
		x = n->x;
		y = n->y;
		nrVisible = n->nrVisible;
		click_x = n->click_x;
		click_y = n->click_y;
	}

	void SetStart(unsigned set_x, unsigned set_y)
	{
		click_x = set_x;
		click_y = set_y;
		SetNull(set_x, set_y);
	}

	void SetNull(unsigned set_x, unsigned set_y)
	{
		x = set_x;
		y = set_y;
		
		if (grid[y][x])
		{
			nrVisible++;
		}

		// Merkkaa koko ympäristö
		grid[y][x] = 0;

		// Extend the visible area
		for(unsigned i = 0; i < 8; i++)
		{
			int incx = kXInc[i] + x;
			int incy = kYInc[i] + y;

			if (incx >= 0 && incx < C && incy >= 0 && incy < R)
			{
				if (grid[incy][incx])
				{
					nrVisible++;
				}

				grid[incy][incx] = 0;
			}
		}
	}	

	void Dump()
	{
		grid[click_y][click_x] = 2;

		for(unsigned i = 0; i < R; i++)
		{
			for(unsigned j = 0; j < C; j++)
			{
				switch(grid[i][j])
				{
				case 0:
					cout << ".";
					break;

				case 1:
					cout << "*";
					break;

				case 2:
					cout << "c";
					break;
				}
			}
			cout << "\n";
		}
	}
};




int main(int argc, char *argv[])
{
	unsigned nrTCs = 0;
	cin >> nrTCs;

	for(unsigned i = 0; i < nrTCs; i++)
	{
		cin >> R >> C >> M;

		unsigned targetVisible = R*C-M;

		Node *n = new Node;
		n->SetStart(0,0);
		queue<Node*> theQueue;
		theQueue.push(n);
		Node *n2 = new Node;
		n2->SetStart(C/2, R/2);
		theQueue.push(n2);
		Node *n3 = new Node;
		n3->SetStart(0, R/2);
		theQueue.push(n3);
		Node *n4 = new Node;
		n4->SetStart(C/2, 0);
		theQueue.push(n4);

		bool solutionFound = false;	

		if (targetVisible == 1)
		{
			solutionFound = true;
			n = new Node;
			n->click_x = 0;
			n->click_y = 0;
		}

		while(!theQueue.empty() && !solutionFound)
		{
			n = theQueue.front();
			theQueue.pop();

			if (n->nrVisible > targetVisible)
			{
				continue;
			} else if (n->nrVisible == targetVisible)
			{
				solutionFound = true;
				break;
			}

			// Extend the visible area
			for(unsigned i = 0; i < 8; i++)
			{
				int x = n->x + kXInc[i];
				int y = n->y + kYInc[i];

				if (x >= 0 && x < C && y >= 0 && y < R)
				{
					Node *newNode = new Node(n);
					newNode->SetNull(x, y);
					if (newNode->nrVisible > n->nrVisible)
					{
						theQueue.push(newNode);
					} else
					{
						delete newNode;
					}
				}
			}

			delete n;
		}

		// 
		cout << "Case #" << (i + 1) << ": \n";
		if (!solutionFound)
		{
			cout << "Impossible\n";
		} else
		{
			n->Dump();
		}


	}

	return 0;
}