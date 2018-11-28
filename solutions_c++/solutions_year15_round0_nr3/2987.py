#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <map>
#include <math.h>

using namespace std;

char enc[9] = "1ijk-pqr";

char table[8][8] = { {0,1,2,3,4,5,6,7}, {1,4,3,6,5,0,7,2}, {2,7,4,1,6,3,0,5},
               {3,2,5,4,7,6,1,0}, {4,5,6,7,0,1,2,3}, {5,0,7,2,1,4,3,6},
	      {6,3,0,5,2,7,4,1}, {7,6,1,0,3,2,5,4}};

int toint(char c)
{
	int i;
	for (i=0;i<8;i++)
		if (c==enc[i])
			return i;
	return -1;
}

char evaluate(char *LX, int a, int b)
{
	int i;
	int n;
	char *tmp;
	n = b-a+1;
	tmp = (char*)malloc(sizeof(char)*n);
	for (i=a;i<=b;i++)
		tmp[i-a] = LX[i];
	for (i=0;i<n-1;i++)
	{
		tmp[i+1] = enc[table[toint(tmp[i])][toint(tmp[i+1])]];
	}

	return tmp[n-1];
}

int main()
{
    int T,L,X;
    int i,j,x,y,z;
    int N;
    int m,n;
    int p1, p2;
    char ri,rj,rk;

    int vp1[10000];
    int vp2[10000];
    int cvp1,cvp2;

    char LS[10000];

    cin >> T;
    
    for (x=0;x<T;x++)
    {

	cin >> L;
	cin >> X;

	cin >> LS;

	N = L*X;

	cvp1 = 0;
	for (i=0;i<10000;i++)
		vp2[i]=0;	
	ri = evaluate(LS,0,0);
	if (ri=='i')
		vp1[cvp1++] = 0;
	for (p1=1;p1<N-2;p1++)
	{
		ri = enc[table[toint(ri)][toint(LS[p1%L])]];
		if (ri=='i')
			vp1[cvp1++] = p1;
	}

	rk = evaluate(LS,L-1,L-1);
	if (rk=='k')
		vp2[N-2] = 1;
	for (p2=N-3;p2>=1;p2--)
	{	
		rk = enc[table[toint(LS[(p2+1)%L])][toint(rk)]];
		if (rk=='k')
			vp2[p2] = 1;
	}

	for (p1=0;p1<cvp1;p1++)
	{
		i = vp1[p1]+1;
		rj = LS[i%L];
		if (rj=='j' && vp2[i])
		{
       			printf("Case #%d: YES\n",x+1);
			goto END;
		}
		for (i++;i<N-2;i++)
		{
			rj = enc[table[toint(rj)][toint(LS[i%L])]];
			if (rj=='j' && vp2[i])
			{	
       				printf("Case #%d: YES\n",x+1);
				goto END;
			}
		}
		
	}
			
       	printf("Case #%d: NO\n",x+1);
		
	END: ;
    }
}
