#include<stdio.h>
#include<vector>
#include<string>
#include<stdlib.h>
using namespace std;

vector<long long> process(vector<long long> visited, int now){

	while (true){
		if (now < 10){
			visited[now] = 1;
			break;
		}
		else{
			visited[now % 10] = 1;
		}
		now = now / 10;
	}
	return visited;
}


int main(){

	FILE *pFile = fopen("A-large.txt", "r");
	FILE *oFile = fopen("A-large-output.txt", "w");
	int testcase;
	fscanf(pFile, "%d", &testcase);

	for (int temp = 1; temp <= testcase; temp++){

		int input;
		fscanf(pFile, "%d", &input);

		if (input == 0){
			fprintf(oFile, "Case #%d: INSOMNIA\n", temp);
		}
		else{
			int rate = 1;

			vector<long long> visited;
			visited.resize(10);

			while (true){

				long long now = rate*input;

				visited = process(visited, now);

				int count = 0;
				for (int i = 0; i < 10; i++){
					if (visited[i] == 1){
						count++;
					}
				}

				if (count == 10){
					fprintf(oFile, "Case #%d: %lld\n", temp, now);
					break;
				}
				else{
					rate++;
				}

			}
		}

	}
}
