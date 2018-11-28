#include <iostream>
using namespace std;

int main(){
	//int N = 32;
	freopen("out", "w", stdout);
	printf("Case #%d:\n",1);
	int i1=1;
	int i2=3;
	int j1=2;
	int j2=4;
	string cur = "10000000000000000000000000000001";
	printf("%s %d %d %d %d %d %d %d %d %d\n", cur.c_str(), 3, 4, 5, 6, 7, 8, 9, 10, 11);
	for(int t=0; t<499; t++){
		cur = "10000000000000000000000000000001";
		cur[i1] = '1';
		cur[i2] = '1';
		cur[j1] = '1';
		cur[j2] = '1';
		printf("%s %d %d %d %d %d %d %d %d %d\n", cur.c_str(), 3, 4, 5, 6, 7, 8, 9, 10, 11);
		if(j2<30){
			j2+=2;
		}
		else{
			if(j1<28){
				j1+=2;
				j2 = j1 + 2;
			}
			else{
				j1 = 2;
				j2 = 4;
				if(i2<30){
					i2+=2;
				}
				else{
					if(i1<28){
						i1+=2;
						i2 = i1 + 2;
					}
				}
			}
		}
	}
}