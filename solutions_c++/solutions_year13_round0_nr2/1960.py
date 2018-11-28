#include<stdio.h>

int testCount;
int testStatus;
int N,M;//рядки. стовпчики
int test[100][100];
int rows[100],columns[100];

void readData(){
	//printf("readData\n");
	scanf("%d %d",&N,&M);
	for(int i = 0; i < N; i++){
		for(int j = 0;j < M; j++){
			scanf("%d",&test[i][j]);
		}
	}
}

void writeData(){
	printf("writeData\n");
	printf("N = %d  M = %d\n",N,M);
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			printf(" %d",test[i][j]);
		}
		printf("\n");
	}
}

void solve(){
	//printf("Solve\n");
	int minElem = 101,maxElem = 1;//знайти найбільший та найменший елемент
	for(int i = 0; i < N; i++){
		for(int j = 0;j < M; j++){
			if(minElem>test[i][j])minElem = test[i][j];
			if(maxElem<test[i][j])maxElem = test[i][j];
		}
	}

	bool result = true;
	//printf("Min = %d  max = %d\n",minElem,maxElem);
	for(int i=minElem; i<maxElem; i++)//пошук рядків
	{
		
		//printf("Iteratia %d\n",i);
		bool potoch = true;
		//printf("Rows\n");
		for(int j = 0; j < N; j++){//пройдемося по рядках
			rows[j]=0;
			if(test[j][0]==i){//якщо починається на потрібний номер
				rows[j] = 1;
				for(int z = 1; z < M; z++){
					if(test[j][z]!=i){
						rows[j]=0;
						break;
					}
				}

			}
			//if(rows[j]==1) printf("row %d\n",j);
		}
		//printf("Columns\n");
		for(int j = 0; j < M; j++){//пройдемося по стовпчиках
			columns[j]=0;
			if(test[0][j]==i){//якщо починається на потрібний номер
				columns[j] = 1;
				for(int z = 1; z < N; z++){
					if(test[z][j]!=i){
						columns[j]=0;
						break;
					}
				}

			}
			//if(columns[j]==1) printf("column %d\n",j);
		}

		
		//writeData();
		for(int j=0;j<N;j++)
		{
			for(int z=0;z<M;z++)
			{
				if(test[j][z]==i){
					if(rows[j]==0 && columns[z]==0){
						potoch = false;
						//printf("Error if y = %d  x = %d\n",j,z);
					}// printf("Correct if y = %d  x = %d\n",j,z);
					test[j][z]=i+1;
				}
			}
		}
		if(!potoch)result = false;
		//writeData();
	}
	if(result) testStatus = 1;
	else testStatus = 2;
}



int main(){
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	scanf("%d",&testCount);
	for(int i=0;i<testCount; i++)
	{
		readData();
		//writeData();
		solve();
		printf("Case #%d: ",i+1);
		if(testStatus==1) printf("YES\n");
		else printf("NO\n");
		
	}
	return 0;
}

