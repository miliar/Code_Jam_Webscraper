#include <iostream>
#include <vector>

using namespace std;

int main() {
	FILE *fp = fopen("A-small-attempt0.in","r");
	//FILE *fp = fopen("test.txt","r");
	int T = 0;
	fscanf(fp, "%d", &T);
	//fread(&T,sizeof(int),1,fp);
	for (int i=1;i<=T;i++) {
		printf("Case #%d: ", i);
		
		int s;
		fscanf(fp, "%d ", &s);

		std::vector<int> myvector (s+1);

		for (int j=0;j<=s;j++) {
			char c;
			fread(&c,sizeof(char),1,fp);
			myvector[j] = c - '0';
		}
		
		//start: to determine y
		int y = 0, clap_num = 0;
		for (int j=0;j<=s;j++) {
			if (myvector[j]==0) 
				continue;

			int threshold = j;

			if (clap_num>=threshold) {
				clap_num+=myvector[j];
			} else {
				y += (threshold-clap_num);
				clap_num+=(y+myvector[j]);
			}
		}
		//end
		
		printf("%d", y);

		if (i!=T)
			printf("\n");
	}
	
	return 0;
}