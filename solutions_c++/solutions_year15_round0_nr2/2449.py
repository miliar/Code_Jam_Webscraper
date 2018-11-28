#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void quickSort(vector<int>&,int,int);

int partition(vector<int>&, int,int);

void quickSort(vector<int>& A, int p,int q)
{
    int r;
    if(p<q)
    {
        r=partition(A, p,q);
        quickSort(A,p,r);
        quickSort(A,r+1,q);
    }
}

int partition(vector<int>& A, int p,int q)
{
    int x= A[p];
    int i=p;
    int j;

    for(j=p+1; j<q; j++)
    {
        if(A[j]<=x)
        {
            i=i+1;
            swap(A[i],A[j]);
        }

    }
    swap(A[i],A[p]);
    return i;
}

int decision2(vector<int> list)
{
	int ans = list.back();
	int optimal_split;
	int i;
	int split_cost;

	optimal_split = 2;
	while( optimal_split < ans )
	{
		split_cost = 0;
		for(i = 0; i < list.size(); i++)
		{
			split_cost += (list[i] - 1)/optimal_split;
		}

		ans = min(ans, split_cost + optimal_split);

		optimal_split++;
	}

	return ans;
}


int decision(vector<int> list)
{
	int result;
	int eat_time, special_time, search_time;
	int i;
	int tmp;
	vector<int> eat_list;
	vector<int> search_list;

	if(list.back() == 0)
		return 0;
	else if(list.back() == 1)
		return 1;

	//1. eat time
	for(i = 0; i < list.size(); i++)
	{
		if(list[i])
		{
			eat_list.push_back( list[i] - 1 );
		}
		else
		{
			eat_list.push_back(0);
		}
	}
	eat_time = 1 + decision(eat_list);

	//2. special time
	tmp = list.back();
	list.pop_back();


	if( tmp > 3)
	{
		special_time = 9999;

		for(i = 2; i <= tmp/2; i++)
		{
			search_list.clear();
			search_list = list;
			//printf("tmp = %d, i = %d\n", tmp, i);
			search_list.push_back( tmp - i );
			search_list.push_back( i );
			sort(search_list.begin(), search_list.end());
			search_time = decision(search_list);
			special_time = min(special_time, search_time);
		}
	}
	else
	{

		list.push_back( tmp/2 );
		list.push_back( tmp/2 + (tmp % 2 ? 1 : 0 ) );


		//quickSort(list, 0, list.size());
		sort(list.begin(), list.end());
		special_time = decision(list);

	}

	special_time+=1;

	return min(eat_time, special_time);
}

int cakeTime(FILE *fp)
{
    //int minutes = 0;
    int D;
    char readBuf[128];
    int i;
    int val;
    char ch;
    vector<int> dinners;

    //1. read Num of D
    fgets(readBuf, sizeof(readBuf), fp);
    D = atoi(readBuf);

    for(i = 0; i < D; i++)
    {
    	dinners.push_back(0);

        do{
            ch = fgetc(fp);
            if( ch == ' ' || ch == '\n' || ch == EOF)
                break;
            dinners[i] = dinners[i]*10 + ch - '0';

        }while(1);
    }
/*
    for(i = 0; i < dinners.size(); i++)
    {
    	printf(" %d ", dinners[i]);
    }
    printf("\n");
*/
    // algorithm here

    //quickSort(dinners, 0, dinners.size());
    sort(dinners.begin(), dinners.end());
    //return decision(dinners);
    return decision2(dinners);
}

int main(int argc, char **argv)
{
    FILE *fp;
    int numCase;
    char readBuf[16];
    int i;
    vector<int> cost_tmp;

    if(argc != 2)
    {
    	printf("no input\n");
        return -1;
    }

    fp = fopen(argv[1], "r");

    if( fp == NULL )
    {
        printf("Can not open file\n");
        return -1;
    }

    if(fgets(readBuf, sizeof(readBuf), fp ) != NULL)
    {
        numCase = atoi(readBuf);
    }
    else
    {
        printf("Can not read file\n");
        return 0;
    }
    //printf("%d\n", numCase);

    for( i = 1; i <= numCase; i++)
    {
    	//cakeTime(fp);
        printf("Case #%d: %d\n", i, cakeTime(fp));
    }

    fclose(fp);

    return 0;
}
