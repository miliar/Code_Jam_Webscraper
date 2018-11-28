#include "iostream"

using namespace std;

struct entity{
	
	int d ;
	int graph[4][4];

};
void graph_process(int test_num){
	
	entity gra[2];
	int count = 0;
	int matched_num;
	for(int k=0;k<2;k++)
	{
		cin>>gra[k].d;
		for(int i=0;i<4; i++)
			for(int j=0;j<4; j++)
			cin>>gra[k].graph[i][j];
	}
	for(int i=0; i< 4;i++)
	{
			for(int j=0;j<4;j++)
		{
			int a = gra[0].graph[gra[0].d - 1][i];
			int b = gra[1].graph[gra[1].d - 1][j];
			if( a == b)
			{
				count++;
				matched_num = a ;
			}

		}
	}
	if(count == 0 ) printf("Case #%d: Volunteer cheated!\n", test_num);
	else if(count == 1) printf("Case #%d: %d\n", test_num, matched_num);
	else if(count > 1) {printf("Case #%d: Bad magician!\n", test_num); } 
	return;
}

int main(){
	int test_num = 0;
	cin>>test_num;
	for(int i= 0 ; i< test_num; i++)
	graph_process(i+1);

}