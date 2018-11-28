#include<conio.h>
#include<cstdio>
#include<stack>
#include<fstream>

using namespace std;
ofstream outfile;
char grid[55][55];

class mini
{
    public:

        char cell[5][5];
        bool mark[5][5];

        mini()
        {
            int i,j;

            for(i=0;i<5;i++)
            {
                for(j=0;j<5;j++)
                {
                    cell[i][j] = '.';
                    mark[i][j] = false;
                }
            }
        }
};

struct coordinate
{
    int r,c;
};

void displayMini(const mini *a, int R, int C)
{
    int i,j;

    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            printf("%c",a->cell[i][j]);
        }
        printf("\n");
    }
}

void fillMiniStack(int R, int C, int M, int index, int n, mini *a, stack <mini> *S)
{
    if(index > R*C)    //r>=R || c>=C
        return;
    if(n == M)
    {
//        displayMini(a,R,C); printf("\n"); getch();
        S->push(*a);
        return;
    }
    int i,j,r,c;
    j = R*C;
    for(i=index; i<j; i++)
    {
        r = i/C;
        c = i%C;
//        printf("mark %d,%d\n",r,c);
        a->cell[r][c] = '*';
        fillMiniStack(R,C,M,i+1,n+1, a, S);
        a->cell[r][c] = '.';
    }
//    for(i=r;i<R;i++)
//    {
//        for(j=c;j<C;j++)
//        {
//            printf("mark %d,%d\n",i,j);
//            a->cell[i][j] = '*';
//            fillMiniStack(R,C,M,i+(j+1)/C,(j+1)%C,n+1, a, S);
//            a->cell[i][j] = '.';
//        }
//    }
}

coordinate makeCoordinate(int r, int c)
{
    coordinate x;

    x.r = r;
    x.c = c;

    return x;
}

bool valid(coordinate x, int R, int C)
{
    if(x.c<0 || x.r<0 || x.c>=C || x.r>=R)
        return false;
    return true;
}

void findAllVertices(mini *a, coordinate c, int R, int C, stack <coordinate> *P)
{
    int turnr[] = {-1,-1,-1, 0, 0, 1, 1, 1};
    int turnc[] = {-1, 0, 1,-1, 1,-1, 0, 1};

    int i;
    coordinate x;

    //check if this is a '0' or its neighbouring cells contain mine
    for(i=0;i<8;i++)
    {
        x.r = c.r + turnr[i];
        x.c = c.c + turnc[i];

        if(valid(x,R,C)==true && a->cell[x.r][x.c] == '*')
        {
            return;
        }
    }

    for(i=0;i<8;i++)
    {
        x.r = c.r + turnr[i];
        x.c = c.c + turnc[i];

        if(valid(x,R,C)==true && a->mark[x.r][x.c] == false)
        {
            P->push(x);
        }
    }
}

void resetMarkMini(mini *a, int R, int C)
{
    int i,j;

    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            a->mark[i][j] = false;
        }
    }
}

bool checkContinuityMini(mini *a, coordinate c, int R, int C)
{
    stack <coordinate> P;
    int i,j;
    coordinate x;

    P.push(c);
    resetMarkMini(a,R,C);

    while(!P.empty())
    {
        x = P.top();
        P.pop();
        if(a->cell[x.r][x.c] == '.')
        {
            a->mark[x.r][x.c] = true;
            findAllVertices(a, x, R, C, &P);
        }
    }

    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            if(a->cell[i][j] == '.' && a->mark[i][j] == false)
                return false;
        }
    }

    return true;
}

bool checkPossibleMini(mini *a, int R, int C)
{
    //for all possible sources, check continuity
    stack <coordinate> P;
    int i,j;
    coordinate c;
    //identify all sources
    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            if(a->cell[i][j] == '.')
            {
                P.push(makeCoordinate(i,j));
//                printf("source = %d,%d\n",i,j);
            }
        }
    }

//    displayMini(a,R,C);

    while(!P.empty())
    {
        c = P.top();
        P.pop();

        if(checkContinuityMini(a,c,R,C) == true)
        {
            a->cell[c.r][c.c] = 'c';
            return true;
        }
        else
        {
//            printf("%d,%d failed\n");   getch();
        }
    }
    return false;
}

void bruteForce(int R, int C, int M)    //R<=3 && C<=3
{
    //place M mines
    //apply BFS to check continuity
    mini a;
    stack <mini> S;
    fillMiniStack(R,C,M,0,0,&a,&S); //stack 'S' is filled with all possible combinations of mines on the grid

    //for each object in stack, for all possible sources, check if it can be solved in a single click
    while(!S.empty())
    {
        a = S.top();
        S.pop();
        //check if 'a' is possible to solve
        if(checkPossibleMini(&a,R,C)==true)
        {
            //display & exit();
            int i,j;
            for(i=0;i<R;i++)
            {
                for(j=0;j<C;j++)
                    outfile<<a.cell[i][j];  //printf("%c",a.cell[i][j]);
                outfile<<endl;  //printf("\n");
            }
            return;
        }
        else
        {
//            printf("\nFailed\n");
//            displayMini(&a,R,C); getch();
        }
    }
    outfile<<"Impossible\n";    //printf("Impossible\n");
}

int main()
{
//	freopen("input.txt","r",stdin);
	outfile.open("outputS.txt");
	int i,j,k,t,R,C,M;

	scanf("%d",&t);

	for(i=1;i<=t;i++)
	{
	    scanf("%d%d%d", &R, &C, &M);
        outfile<<"Case #"<<i<<":\n";  //printf("Case #%d:\n",i);

//	    if(R>3 && C>3)
//	    {
//	        //there has to be a general solution for greater dimensions
//            printf("Not implemented yet.\n");
//	    }
//	    else
//	    {
	        //apply brute force
	        //for all possible combinations of mines, check if any can be solved via 1 click
	        bruteForce(R,C,M);
//	    }
	}
	return(0);
}
