#include "iostream"
using namespace std;
void sort(double* UnsortArray,int length){
	double min ;
	int min_index ;
	for(int i = 0 ; i < length; i++)
	{
		min = UnsortArray[i];
		min_index = i;
		double tmp ;
		for(int j = i + 1 ; j < length ; j++ )
		{
			if( UnsortArray[j] < min){
				min = UnsortArray[j];
				min_index = j;
			}
		}
		tmp = UnsortArray[i];
		UnsortArray[i] = UnsortArray[min_index];
		UnsortArray[ min_index ] =  tmp;
	}
	

}
int noDeceit(double *Blocks_N , double *Blocks_K, int length){
	int N_score = 0;
	int *Mark = new int[length];
	int flag =0 ;
	for (int i = 0; i < length; ++i)
		Mark[i] = 0;
	for(int i = 0 ; i < length ; i++)
	{	
		for (int j = 0; j < length; ++j)
		{
			if( Mark[ j ] == 1 )
				continue;
			if( Blocks_K[j] > Blocks_N[i] && Mark[j] == 0)
			{
				Mark[j] = 1;
				flag = 1;
				break;
			}
		}
		if(flag == 0) N_score++;
		else flag = 0;
	}
return N_score;

}
int Deceit(double *Blocks_N , double *Blocks_K, int length){
	int N_score = 0;
	int *Mark = new int[length];
	for (int i = 0; i < length; ++i)
		Mark[i] = 0;
	for(int i = 0 ; i < length ; i++)
	{	
		if(Blocks_N[i] > Blocks_K[i])
		{	N_score ++;
			Mark[i] = 1;
		}		
	}
	//cout<< N_score <<endl;
	// for (int i = 0; i < length; ++i)
	// {
	// 	cout<< Mark[i]<<" ";
	// }
	//cout<<endl;
	int j = 0;
	for(int i = 0 ; i < length ; i++)
	{	
		while(Mark[j]!=0) j++;

		if(Mark[i] == 0 && Blocks_N[i] > Blocks_K[j])
		{	
			N_score++;
			j++;
			while(Mark[j]!=0) j++;
		}		
	}
	return N_score;



}
void read_process(int order){
	int blockNum = 0;
	cin>> blockNum;
	double *Naomi, *Ken;
	Naomi = new double[blockNum];
	Ken = new double[blockNum];
	for(int i = 0 ; i< blockNum; i++)
		cin>> Naomi[i];
	for(int i = 0 ; i< blockNum; i++)
		cin>> Ken[i];
	sort(Naomi,blockNum);
	sort(Ken,blockNum);
	// for (int i = 0; i < blockNum; ++i)
	// {
	// 	cout<< Naomi[i]<<" ";
	// }
	// cout<<endl;
	// for (int i = 0; i < blockNum; ++i)
	// {
	// 	cout<< Ken[i]<<" ";
	// }
	cout << "Case #"<<order<<": "<< Deceit(Naomi, Ken, blockNum) <<" "<< noDeceit(Naomi, Ken, blockNum) <<endl;
}

int main(){
	int test_num = 0;
	cin>>test_num;
	for(int i= 0 ; i< test_num; i++)
	read_process(i+1);

}