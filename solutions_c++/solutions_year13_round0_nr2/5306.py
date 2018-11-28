// tictac.cpp : Defines the entry point for the console application.
//


#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <ctime>

using namespace std;

#define _MAX(a,b)	(a>b)?a:b
#define _MIN(a,b)	(a<b)?a:b

#define MAX_R 100
#define MAX_C 100

#define XDBG 0
#if XDBG
#define DBG std::cout
#else
#define DBG if(0) cout 
#endif

std::ofstream oF;
std::ifstream iF;
int ROWS,COLS;



void process(int i);

int main(int argc, char * argv[])
{
	iF.open("D:\\lawn_in.dat",ios::in);
	oF.open("D:\\lawn_out.txt",ios::out);

	int cases=0;
	iF>>cases;

	DBG<<"Starting..."<<cases<<"\n";
	clock_t t=clock();

	for(int i=0;i<cases;)
	{
		process(++i);
	}

	iF.close();
	oF.close();

	clock_t t2 = clock();
	DBG<<"time taken = "<<(t2-t)/18.2<<"\n";

	return 0;
}

int TARGET[MAX_R][MAX_C];
int CURR[MAX_R][MAX_C];
int RMIN[MAX_R] = {101};
int CMIN[MAX_C] = {101};
int RMAX[MAX_R] = {0};
int CMAX[MAX_C] = {0};

bool COL_PROB = false;
bool ROW_PROB = false;


void set_new()
{
	DBG<<"\nNew Table#\n";
	for(int i=0;i<ROWS;i++){
		for(int j=0;j<COLS;j++){
			CURR[i][j] = _MAX(RMAX[i],CMAX[j]);
			DBG<<CURR[i][j]<<"\t";
		}
		DBG<<"\n";
	}

}
void print_new()
{
	DBG<<"\nTarget Table#\n";
	for(int i=0;i<ROWS;i++){
		for(int j=0;j<COLS;j++){
			DBG<<TARGET[i][j]<<"\t";
		}
		DBG<<"\n";
	}
	DBG<<"\nNew Table#\n";
	for(int i=0;i<ROWS;i++){
		for(int j=0;j<COLS;j++){
			DBG<<CURR[i][j]<<"\t";
		}
		DBG<<"\n";
	}

}

int check_if_all_okay_row(int d, int r,int c)
{
	if(ROW_PROB)
	{
		return -1;
	}
	for(int j=0;j<COLS; j++)
	{
		if(TARGET[r][j] >d)
		{
			DBG<<"Problem : "<<r<<":"<<c<<"\n";
			ROW_PROB = true;
			if(COL_PROB)
			{
				return -1;
			}
		}
	}
	return 0;

}

int check_if_all_okay_col(int d, int r,int c)
{
	if(COL_PROB)
	{
		return -1;
	}
	for(int i=0;i<ROWS; i++)
	{
		if(TARGET[i][c] >d)
		{
			DBG<<"Problem : "<<r<<":"<<c<<"\n";
			COL_PROB = true;
			if(ROW_PROB)
			{
				return -1;
			}

			//			return -1;
		}
	}
	return 0;

}


void set_col(int c, int new_val)
{
	for(int i=0;i<ROWS;i++)
	{
		if(CURR[i][c] > new_val){
			CURR[i][c] = new_val;
		}
	}
}
void set_row(int r, int new_val)
{
	for(int j=0;j<COLS;j++)
	{
		if(CURR[r][j] > new_val){
			CURR[r][j] = new_val;
		}
	}
}

int can_reduce(int r,int c,int new_ht)
{

	int rval=0;
	bool can_reduce_col = true;
	bool can_reduce_row = true;

	for(int i=0;i<ROWS;i++)
	{
		if(TARGET[i][c] > new_ht)
		{
			can_reduce_col = false;
			DBG<<"Not possible to reduce from Col "<<c<<"\n";
			break;
		}
	}
	for(int j=0;j<COLS;j++)
	{
		if(TARGET[r][j] > new_ht)
		{
			can_reduce_row = false;
			DBG<<"Not possible to reduce from Row#"<<r<<"\n";
			break;
		}
	}
	if(can_reduce_col == false && can_reduce_row == false)
	{
		return -1;
	}

	if(can_reduce_col)
	{
			set_col(c,new_ht);
	}
	else if(can_reduce_row)
	{
			set_row(r,new_ht);
	}

	return 0;
}



void process(int CASE){
	oF<<"Case #"<<CASE<<":";
	iF>>ROWS>>COLS;
	DBG<<"Case: "<<CASE<<":"<<ROWS<<":"<<COLS<<"\n";
	int i,j,d;
#if 0
	if(ROWS==1 || COLS==1)
	{
		for(i=0;i<ROWS;i++){
			for(j=0;j<COLS;j++){
				iF>>d;
			}
		}
		oF<<" YES\n";
		return;
	}
#endif

	COL_PROB = false;
	ROW_PROB = false;
	for(i=0;i<ROWS;i++){
		RMIN[i] = 101;
	}
	for(j=0;j<COLS;j++){
		CMIN[j] = 101;
	}
	for(i=0;i<ROWS;i++){
		for(j=0;j<COLS;j++){
			iF>>d;
			DBG<<d<<"\t";
			if(RMIN[i] >= d)
				RMIN[i] = d;

			if(CMIN[j] >= d)
				CMIN[j] = d;

			if(RMAX[i] < d)
				RMAX[i] = d;

			if(CMAX[j] <= d)
				CMAX[j] = d;

			TARGET[i][j] = d;
		}
		DBG<<"\n";
	}


	DBG<<"\nRow Min: ";
	for(i=0;i<ROWS;i++)
	{
		DBG<<RMIN[i]<<"\t";
	}

	DBG<<"\nCol Min: ";
	for(i=0;i<COLS;i++)
	{
		DBG<<CMIN[i]<<"\t";
	}
	DBG<<"\n";
	DBG<<"\nRow Max: ";
	for(i=0;i<ROWS;i++)
	{
		DBG<<RMAX[i]<<"\t";
	}

	DBG<<"\nCol Max: ";
	for(i=0;i<COLS;i++)
	{
		DBG<<CMAX[i]<<"\t";
	}
	set_new();

	for(i=0;i<ROWS;i++){
		for(j=0;j<COLS;j++){
			DBG<<"Handling: "<<i<<":"<<j<<"\n";
			if(TARGET[i][j] > CURR[i][j])
			{
				DBG<<"something wrong happened in "<<i<<""<<j<<"\n";
				oF<<" NO\n";
				return;
			}
			if(TARGET[i][j] != CURR[i][j])
			{
    				int new_ht = TARGET[i][j];
					DBG<<"Reducing to"<<new_ht<<" in from row#"<<i<<":: or coln = "<<j<<"\n";
					if(can_reduce(i,j,new_ht)==-1)
					{
						oF<<" NO\n";
						return;
					}
					print_new();
			}
		}
	}
	oF<<" YES\n";
#ifdef DBG
	oF.flush();
#endif
}


#if 0
d = TARGET[i][j];
if(d==RMIN[i])	// only for local minima's
{
	if(-1== check_if_all_okay_row(d,i,j))
	{

		DBG<<"Failure at "<<i<<":"<<j<<"\n";
		oF<<" NO\n";
#ifdef DBG
		oF.flush();
#endif
		return;
	}
}
if(d==CMIN[j])	// only for local minima's
{
	if(-1== check_if_all_okay_col(d,i,j))
	{

		DBG<<"Failure at "<<i<<":"<<j<<"\n";
		oF<<" NO\n";
#ifdef DBG
		oF.flush();
#endif
		return;
	}
}
		}
		}
		if(COL_PROB && ROW_PROB)

			oF<<"NO\n";
		else
			oF<<" YES\n";

#endif
