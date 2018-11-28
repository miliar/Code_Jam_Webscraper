#include <stdio.h>
#include <set>
#include <algorithm>
//
//3
//2
//1 2 3 4
//5 6 7 8
//9 10 11 12
//13 14 15 16
//3
//1 2 5 4
//3 11 6 15
//9 10 7 12
//13 14 8 16
//Case #1: 7
//Case #2: Bad magician!
//Case #3: Volunteer cheated!

void solveMagicTrick()
{
	using namespace std;

	int arr1[16];
	int arr2[16];
	int N;	
	scanf("%d",&N);
	int a;
	int b;

	for(int k=1;k<=N;k++)
	{


		scanf("%d",&a);
		for(int i=0;i<16;i++)
		{
			scanf("%d",&arr1[i]);
		}
		scanf("%d",&b);
		for(int i=0;i<16;i++)
		{
			scanf("%d",&arr2[i]);
		};

		int repeat=0;
		set<int> val;
		val.insert(&arr1[(a-1)*4],&arr1[(a-1)*4+4]);
		val.insert(&arr2[(b-1)*4],&arr2[(b-1)*4+4]);
		if(val.size()>=8)
		{
			printf("Case #%d: Volunteer cheated!\n",k);
		}
		else if(val.size()==7){
			for(int c=0;c<4;c++)
			{
				int*p = std::find(&arr1[(a-1)*4],&arr1[(a-1)*4+4],arr2[(b-1)*4+c]);
				if(p!=&arr1[(a-1)*4+4])
				{
					printf("Case #%d: %d\n",k,*p);
					break;

				}

			}
		}
		else
		{
			printf("Case #%d: Bad magician!\n",k);
		}
	}
}

void solveB()
{
	int N;
	scanf("%d",&N);

	double C,F,X;

	for(int k=1;k<=N;k++)
	{

		scanf("%lf",&C);
		scanf("%lf",&F);
		scanf("%lf",&X);
		double cost=0;
		double threshold = C/F;
		double v=2;

		double remain = 0;
		double total =0;

		double t = (remain/v);
		double curCookies=0;

		while(curCookies<X)
		{
			remain = X-curCookies;

			 t = (remain/v);
			if(t<= (C-curCookies )/v+threshold)
			{
				total +=t;
				curCookies += t*v;
				break;
			}
			else{

				t = (C-curCookies )/v;
				total += t;
				curCookies =curCookies-C + t*v;
				v += F;
			}
		}
		printf("Case #%d: %.7f\n",k,total);
	}
}


int main(int argc,char*argv[])
{

	//solveMagicTrick();
	solveB();

	return 0;
}